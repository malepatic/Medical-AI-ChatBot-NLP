import pandas as pd
from sklearn.utils import resample

print("Creating the FINAL (simplified) intent classification dataset...")

# Load all our question sources
common_df = pd.read_csv('../data/common_diseases_dataset.csv').dropna()
medqa_df = pd.read_json('../data/medqa/phrases_no_exclude_train.jsonl', lines=True).dropna(subset=['question'])
medqa_df = medqa_df.rename(columns={'question': 'prompt'})

# Combine all medical questions under one intent
medical_questions_df = pd.concat([common_df[['prompt']], medqa_df[['prompt']]], ignore_index=True)
medical_questions_df['intent'] = 'medical_question'
medical_questions_df = medical_questions_df.rename(columns={'prompt': 'text'})

# Create synthetic data for other intents
emergency_data = {'emergency': ["I am having severe chest pain.", "My chest hurts badly.", "I can't breathe.", "I am having trouble breathing.", "I think I'm having a heart attack.", "Uncontrollable bleeding.", "I think I'm having a stroke.", "My vision suddenly went blurry.", "I am having suicidal thoughts.", "Someone is unconscious.", "My speech is slurred.", "I'm choking.", "severe burn"]}
emergency_df = pd.DataFrame(emergency_data['emergency'], columns=['text'])
emergency_df['intent'] = 'emergency'

greeting_data = {'greeting': ["Hello", "Hi", "Hey", "Good morning", "How are you?", "Thanks", "Thank you", "Bye", "Goodbye", "Who are you?", "What can you do?"]}
greeting_df = pd.DataFrame(greeting_data['greeting'], columns=['text'])
greeting_df['intent'] = 'greeting'

# Oversample the small classes
n_samples_minority = 1000
emergency_oversampled = resample(emergency_df, replace=True, n_samples=n_samples_minority, random_state=42)
greeting_oversampled = resample(greeting_df, replace=True, n_samples=n_samples_minority, random_state=42)

# Combine and save
final_df = pd.concat([medical_questions_df, emergency_oversampled, greeting_oversampled], ignore_index=True)
final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)
output_path = '../data/intent_training_dataset_v3_final.csv'
final_df.to_csv(output_path, index=False)

print("\nFINAL Intent dataset creation complete!")
print(f"Saved to: {output_path}")
print("\nFinal intent distribution:")
print(final_df['intent'].value_counts())
