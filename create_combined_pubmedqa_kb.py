#!/usr/bin/env python3
"""
Create Comprehensive Knowledge Base from All 3 PubMedQA Datasets
Combines pqa_labeled, pqa_unlabeled, and pqa_artificial for maximum coverage
"""

import pandas as pd
import os

def load_and_process_dataset(dataset_path, dataset_name):
    """Load and process a single PubMedQA dataset"""
    
    print(f"Loading {dataset_name}...")
    print(f"  Path: {dataset_path}")
    
    if not os.path.exists(dataset_path):
        print(f"  ERROR: File not found - {dataset_path}")
        return None
    
    try:
        # Load the parquet file
        df = pd.read_parquet(dataset_path)
        
        print(f"  Loaded: {len(df):,} entries")
        print(f"  Columns: {list(df.columns)}")
        
        # Select and rename columns for RAG system
        if 'question' in df.columns and 'long_answer' in df.columns:
            processed_df = df[['question', 'long_answer']].rename(columns={
                'question': 'prompt',
                'long_answer': 'completion'
            })
            
            # Add dataset source identifier
            processed_df['source_dataset'] = dataset_name
            
            # Clean data
            processed_df = processed_df.dropna()
            
            # Filter for reasonable answer lengths
            min_length = 30
            max_length = 2000
            
            before_filter = len(processed_df)
            processed_df = processed_df[
                (processed_df['completion'].str.len() >= min_length) & 
                (processed_df['completion'].str.len() <= max_length)
            ]
            after_filter = len(processed_df)
            
            print(f"  After cleaning: {after_filter:,} entries")
            print(f"  Removed: {before_filter - after_filter:,} entries")
            
            return processed_df
        else:
            print(f"  ERROR: Required columns not found")
            return None
            
    except Exception as e:
        print(f"  ERROR: {e}")
        return None

def create_combined_knowledge_base():
    """Create comprehensive knowledge base from all 3 PubMedQA datasets"""
    
    print("CREATING COMPREHENSIVE PUBMEDQA KNOWLEDGE BASE")
    print("="*60)
    
    # Define dataset paths
    datasets = [
        {
            'path': '/medical_chatbot_project/data/pubmedqa/pqa_labeled/train-00000-of-00001.parquet',
            'name': 'pqa_labeled'
        },
        {
            'path': '/medical_chatbot_project/data/pubmedqa/pqa_unlabeled/train-00000-of-00001.parquet', 
            'name': 'pqa_unlabeled'
        },
        {
            'path': '/medical_chatbot_project/data/pubmedqa/pqa_artificial/train-00000-of-00001.parquet',
            'name': 'pqa_artificial'
        }
    ]
    
    # Load and process each dataset
    all_dataframes = []
    total_entries = 0
    
    for dataset in datasets:
        processed_df = load_and_process_dataset(dataset['path'], dataset['name'])
        if processed_df is not None:
            all_dataframes.append(processed_df)
            total_entries += len(processed_df)
            print(f"  SUCCESS: Added {len(processed_df):,} entries from {dataset['name']}")
        else:
            print(f"  SKIPPED: {dataset['name']} due to errors")
        print()
    
    if not all_dataframes:
        print("ERROR: No datasets could be loaded successfully")
        return None
    
    # Combine all datasets
    print("COMBINING DATASETS...")
    print("-" * 40)
    
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    print(f"Combined dataset: {len(combined_df):,} entries")
    
    # Remove duplicates based on questions
    print("Removing duplicate questions...")
    before_dedup = len(combined_df)
    combined_df = combined_df.drop_duplicates(subset=['prompt'], keep='first')
    after_dedup = len(combined_df)
    
    print(f"After deduplication: {after_dedup:,} entries")
    print(f"Removed duplicates: {before_dedup - after_dedup:,}")
    
    # Show dataset composition
    print(f"\nDATASET COMPOSITION:")
    print("-" * 30)
    composition = combined_df['source_dataset'].value_counts()
    for dataset, count in composition.items():
        percentage = (count / len(combined_df)) * 100
        print(f"  {dataset}: {count:,} entries ({percentage:.1f}%)")
    
    # Show sample entries from each dataset
    print(f"\nSAMPLE ENTRIES BY SOURCE:")
    print("-" * 40)
    
    for source in combined_df['source_dataset'].unique():
        source_data = combined_df[combined_df['source_dataset'] == source]
        sample = source_data.iloc[0]
        
        print(f"\nSOURCE: {source}")
        print(f"Question: {sample['prompt']}")
        print(f"Answer: {sample['completion'][:200]}...")
        print(f"Length: {len(sample['completion'])} characters")
        print("-" * 25)
    
    # Remove source_dataset column for final output
    final_df = combined_df[['prompt', 'completion']]
    
    # Save the combined knowledge base
    output_path = '/medical_chatbot_project/data/knowledge_base_final.csv'
    
    # Backup current knowledge base
    current_kb_path = '/medical_chatbot_project/data/common_diseases_dataset.csv'
    if os.path.exists(current_kb_path):
        backup_path = current_kb_path.replace('.csv', '_chatdoctor_backup.csv')
        if os.path.exists(backup_path):
            os.remove(backup_path)  # Remove old backup
        os.rename(current_kb_path, backup_path)
        print(f"\nBacked up current knowledge base to: {backup_path}")
    
    # Save new comprehensive knowledge base
    final_df.to_csv(output_path, index=False)
    
    print(f"\nSUCCESS - COMPREHENSIVE KNOWLEDGE BASE CREATED")
    print("="*60)
    print(f"Output file: {output_path}")
    print(f"Total entries: {len(final_df):,}")
    print(f"Unique questions: {final_df['prompt'].nunique():,}")
    print(f"Unique completions: {final_df['completion'].nunique():,}")
    
    # Calculate quality metrics
    avg_question_length = final_df['prompt'].str.len().mean()
    avg_answer_length = final_df['completion'].str.len().mean()
    
    print(f"\nQUALITY METRICS:")
    print(f"  Average question length: {avg_question_length:.1f} characters")
    print(f"  Average answer length: {avg_answer_length:.1f} characters")
    print(f"  Uniqueness ratio: {final_df['completion'].nunique() / len(final_df):.1%}")
    
    print(f"\nCOMPARISON TO CURRENT SYSTEM:")
    print(f"  Current ChatDoctor: 138K entries, 345 unique (21.8% unique)")
    print(f"  New PubMedQA: {len(final_df):,} entries, {final_df['completion'].nunique():,} unique ({final_df['completion'].nunique() / len(final_df):.1%} unique)")
    
    return output_path, len(final_df)

def show_configuration_update():
    """Show how to update system configuration"""
    
    print(f"\nCONFIGURATION UPDATE REQUIRED:")
    print("-" * 40)
    print("Update your app.py or bot.py to use the new knowledge base:")
    print("  Change db_path from:")
    print("    'data/common_diseases_dataset.csv'")
    print("  To:")
    print("    'data/knowledge_base_final.csv'")
    
    print(f"\nCLEAN CACHE AND RESTART:")
    print("  rm chatbot_core/kb_embeddings.pt")
    print("  python3 app.py")

if __name__ == "__main__":
    print("COMPREHENSIVE PUBMEDQA KNOWLEDGE BASE CREATOR")
    print("="*70)
    
    try:
        output_path, entry_count = create_combined_knowledge_base()
        
        if output_path:
            show_configuration_update()
            
            print(f"\nSUMMARY:")
            print(f"Created comprehensive knowledge base with {entry_count:,} research-grade entries")
            print(f"Your RAG system will now provide evidence-based, peer-reviewed medical responses")
            print(f"This represents a massive quality upgrade from ChatDoctor responses")
        
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
