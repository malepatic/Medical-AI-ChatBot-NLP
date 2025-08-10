#!/usr/bin/env python3
"""
Create Ultimate Combined Knowledge Base
Combines PubMedQA (research-grade) + MedQuAD (patient-friendly) datasets
for comprehensive medical coverage
"""

import pandas as pd
import os

def load_pubmedqa_datasets():
    """Load and process all 3 PubMedQA datasets"""
    
    print("LOADING PUBMEDQA DATASETS")
    print("="*40)
    
    pubmedqa_datasets = [
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
    
    all_pubmedqa_dfs = []
    total_pubmedqa = 0
    
    for dataset in pubmedqa_datasets:
        print(f"Loading {dataset['name']}...")
        
        if not os.path.exists(dataset['path']):
            print(f"  SKIPPED: File not found - {dataset['path']}")
            continue
        
        try:
            df = pd.read_parquet(dataset['path'])
            
            if 'question' in df.columns and 'long_answer' in df.columns:
                processed_df = df[['question', 'long_answer']].rename(columns={
                    'question': 'prompt',
                    'long_answer': 'completion'
                })
                
                # Add source identifier
                processed_df['source'] = f'pubmedqa_{dataset["name"]}'
                
                # Clean data
                processed_df = processed_df.dropna()
                processed_df = processed_df[
                    (processed_df['completion'].str.len() >= 30) & 
                    (processed_df['completion'].str.len() <= 2000)
                ]
                
                all_pubmedqa_dfs.append(processed_df)
                total_pubmedqa += len(processed_df)
                
                print(f"  SUCCESS: {len(processed_df):,} entries from {dataset['name']}")
            else:
                print(f"  SKIPPED: Missing required columns in {dataset['name']}")
                
        except Exception as e:
            print(f"  ERROR: {e}")
    
    if all_pubmedqa_dfs:
        combined_pubmedqa = pd.concat(all_pubmedqa_dfs, ignore_index=True)
        print(f"\nTotal PubMedQA entries: {len(combined_pubmedqa):,}")
        return combined_pubmedqa
    else:
        print("No PubMedQA datasets loaded successfully")
        return None

def load_medquad_dataset():
    """Load and process MedQuAD dataset"""
    
    print("\nLOADING MEDQUAD DATASET")
    print("="*40)
    
    medquad_path = '/medical_chatbot_project/data/medquad_lavita_MedQuAD.csv'
    
    print(f"Loading MedQuAD from: {medquad_path}")
    
    if not os.path.exists(medquad_path):
        print(f"ERROR: MedQuAD file not found at {medquad_path}")
        print("Run medquad_downloader.py first")
        return None
    
    try:
        df = pd.read_csv(medquad_path)
        
        if 'question' in df.columns and 'answer' in df.columns:
            processed_df = df[['question', 'answer']].rename(columns={
                'question': 'prompt',
                'answer': 'completion'
            })
            
            # Add source identifier
            processed_df['source'] = 'medquad_nih'
            
            # Clean data
            processed_df = processed_df.dropna()
            processed_df = processed_df[
                (processed_df['completion'].str.len() >= 50) & 
                (processed_df['completion'].str.len() <= 3000)
            ]
            
            print(f"SUCCESS: {len(processed_df):,} entries from MedQuAD")
            return processed_df
        else:
            print(f"ERROR: Expected columns not found in MedQuAD")
            return None
            
    except Exception as e:
        print(f"ERROR loading MedQuAD: {e}")
        return None

def create_ultimate_knowledge_base():
    """Combine PubMedQA and MedQuAD into ultimate knowledge base"""
    
    print("\nCREATING ULTIMATE COMBINED KNOWLEDGE BASE")
    print("="*60)
    
    # Load PubMedQA datasets
    pubmedqa_df = load_pubmedqa_datasets()
    
    # Load MedQuAD dataset
    medquad_df = load_medquad_dataset()
    
    # Combine datasets
    datasets_to_combine = []
    total_entries = 0
    
    if pubmedqa_df is not None:
        datasets_to_combine.append(pubmedqa_df)
        total_entries += len(pubmedqa_df)
        print(f"Adding PubMedQA: {len(pubmedqa_df):,} entries")
    
    if medquad_df is not None:
        datasets_to_combine.append(medquad_df)
        total_entries += len(medquad_df)
        print(f"Adding MedQuAD: {len(medquad_df):,} entries")
    
    if not datasets_to_combine:
        print("ERROR: No datasets available to combine")
        return None
    
    # Combine all datasets
    print(f"\nCombining {len(datasets_to_combine)} datasets...")
    ultimate_df = pd.concat(datasets_to_combine, ignore_index=True)
    
    print(f"Combined total: {len(ultimate_df):,} entries")
    
    # Remove duplicates based on questions
    print("Removing duplicate questions...")
    before_dedup = len(ultimate_df)
    ultimate_df = ultimate_df.drop_duplicates(subset=['prompt'], keep='first')
    after_dedup = len(ultimate_df)
    
    print(f"After deduplication: {after_dedup:,} entries")
    print(f"Removed duplicates: {before_dedup - after_dedup:,}")
    
    # Show final composition
    print(f"\nFINAL DATASET COMPOSITION:")
    print("-" * 40)
    composition = ultimate_df['source'].value_counts()
    for source, count in composition.items():
        percentage = (count / len(ultimate_df)) * 100
        print(f"  {source}: {count:,} entries ({percentage:.1f}%)")
    
    # Show sample entries from each source
    print(f"\nSAMPLE ENTRIES BY SOURCE:")
    print("-" * 40)
    
    for source in ultimate_df['source'].unique():
        source_data = ultimate_df[ultimate_df['source'] == source]
        if len(source_data) > 0:
            sample = source_data.iloc[0]
            print(f"\nSOURCE: {source}")
            print(f"Question: {sample['prompt']}")
            print(f"Answer: {sample['completion'][:200]}...")
            print(f"Length: {len(sample['completion'])} characters")
    
    # Remove source column for final output
    final_df = ultimate_df[['prompt', 'completion']]
    
    # Backup current knowledge base
    current_kb_path = '/medical_chatbot_project/data/knowledge_base_final.csv'
    if os.path.exists(current_kb_path):
        backup_path = '/medical_chatbot_project/data/knowledge_base_final_previous_backup.csv'
        if os.path.exists(backup_path):
            os.remove(backup_path)
        os.rename(current_kb_path, backup_path)
        print(f"\nBacked up previous knowledge base to: {backup_path}")
    
    # Save ultimate knowledge base
    final_df.to_csv(current_kb_path, index=False)
    
    # Calculate quality metrics
    avg_question_length = final_df['prompt'].str.len().mean()
    avg_answer_length = final_df['completion'].str.len().mean()
    uniqueness_ratio = final_df['completion'].nunique() / len(final_df)
    
    print(f"\nULTIMATE KNOWLEDGE BASE CREATED")
    print("="*50)
    print(f"Output file: {current_kb_path}")
    print(f"Total entries: {len(final_df):,}")
    print(f"Unique questions: {final_df['prompt'].nunique():,}")
    print(f"Unique completions: {final_df['completion'].nunique():,}")
    print(f"Uniqueness ratio: {uniqueness_ratio:.1%}")
    print(f"Average question length: {avg_question_length:.1f} characters")
    print(f"Average answer length: {avg_answer_length:.1f} characters")
    
    print(f"\nCONTENT DIVERSITY:")
    print(f"  Research-grade content: PubMedQA (peer-reviewed)")
    print(f"  Patient-friendly content: MedQuAD (NIH patient education)")
    print(f"  Combined coverage: Basic patient questions + advanced medical topics")
    
    return current_kb_path, len(final_df)

def show_restart_instructions():
    """Show how to restart system with new knowledge base"""
    
    print(f"\nRESTART INSTRUCTIONS:")
    print("="*30)
    print("1. Clear all cache files:")
    print("   find . -name '*.pt' -delete")
    print("2. Stop current server (Ctrl+C)")
    print("3. Restart server:")
    print("   python3 app.py")
    print("4. Monitor startup messages for entry count")
    print("5. Test with medical questions")
    
    print(f"\nEXPECTED BENEFITS:")
    print("- Research-backed answers for complex questions")
    print("- Patient-friendly explanations for common conditions") 
    print("- Comprehensive medical knowledge coverage")
    print("- Reduced repetitive/template responses")

def main():
    """Main function to create ultimate combined knowledge base"""
    
    print("ULTIMATE MEDICAL KNOWLEDGE BASE CREATOR")
    print("="*70)
    print("Combining PubMedQA (research) + MedQuAD (patient education)")
    print("="*70)
    
    try:
        output_path, entry_count = create_ultimate_knowledge_base()
        
        if output_path:
            show_restart_instructions()
            
            print(f"\nULTIMATE SYSTEM READY:")
            print(f"Knowledge base: {entry_count:,} combined medical entries")
            print(f"Quality: Research-grade + Patient-friendly content")
            print(f"Coverage: Comprehensive medical knowledge")
            print(f"Ready for production testing")
        
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
