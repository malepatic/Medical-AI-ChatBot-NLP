# /medical_chatbot_project/chatbot_core/data_processor.py

import pandas as pd
import re

def process_chatdoctor(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the ChatDoctor dataframe into a 'prompt' and 'completion' format.
    Also sanitizes the completion to be guidance, not diagnosis.
    """
    print("Processing ChatDoctor...")
    
    df['prompt'] = df.apply(lambda row: f"{row['instruction']} {row['input']}", axis=1)
    
    # A simple example of sanitizing the output. This would need to be more robust.
    df['completion'] = df['output'].apply(lambda x: re.sub(r"It seems you have|The most likely cause is", "The symptoms described could be related to", x))
    df['completion'] = df['completion'] + " For an accurate diagnosis, please consult a healthcare professional."
    
    return df[['prompt', 'completion']]

def process_medqa(df: pd.DataFrame) -> pd.DataFrame:
    """Processes the MedQA dataframe into a 'prompt' and 'completion' format."""
    print("Processing MedQA...")
    
    df['prompt'] = "Question: " + df['question']
    df['completion'] = "The correct answer is: " + df['answer']
    
    return df[['prompt', 'completion']]

def process_pubmedqa(df: pd.DataFrame) -> pd.DataFrame:
    """Processes the PubMedQA dataframe into a 'prompt' and 'completion' format."""
    print("Processing PubMedQA...")
    
    # The context is a dictionary, we need to extract the text.
    df['context_text'] = df['context'].apply(lambda x: ' '.join(x['contexts']))
    df['prompt'] = "Based on the following text: " + df['context_text'] + " Question: " + df['question']
    df['completion'] = df['long_answer']

    return df[['prompt', 'completion']]

if __name__ == '__main__':
    # Load raw datasets
    chatdoctor_df = pd.read_parquet('../data/ChatDoctor/data/train-00000-of-00001-5e7cb295b9cff0bf.parquet')
    medqa_df = pd.read_json('../data/medqa/phrases_no_exclude_train.jsonl', lines=True)
    pubmedqa_df = pd.read_parquet('../data/pubmedqa/pqa_labeled/train-00000-of-00001.parquet')

    # Process each dataset
    processed_chatdoctor = process_chatdoctor(chatdoctor_df)
    processed_medqa = process_medqa(medqa_df)
    processed_pubmedqa = process_pubmedqa(pubmedqa_df)

    # Combine into one unified dataset
    unified_df = pd.concat([processed_chatdoctor, processed_medqa, processed_pubmedqa], ignore_index=True)

    # Save the final dataset
    output_path = '../data/unified_training_data.csv'
    unified_df.to_csv(output_path, index=False)
    
    print(f"\nProcessing complete!")
    print(f"Unified dataset shape: {unified_df.shape}")
    print(f"Saved unified dataset to: {output_path}")
    print("\nSample of the unified data:")
    print(unified_df.sample(5))
