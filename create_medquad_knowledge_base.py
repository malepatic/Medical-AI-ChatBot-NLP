#!/usr/bin/env python3
"""
Create Patient-Friendly Knowledge Base from MedQuAD
Replace technical PubMedQA content with NIH patient education content
"""

import pandas as pd
import os

def create_medquad_knowledge_base():
    """Create patient-friendly knowledge base from MedQuAD dataset"""
    
    print("CREATING PATIENT-FRIENDLY KNOWLEDGE BASE FROM MEDQUAD")
    print("="*60)
    
    # Load the best MedQuAD dataset
    medquad_path = '/medical_chatbot_project/data/medquad_lavita_MedQuAD.csv'
    
    print(f"Loading MedQuAD dataset...")
    print(f"Source: {medquad_path}")
    
    if not os.path.exists(medquad_path):
        print(f"ERROR: MedQuAD file not found at {medquad_path}")
        print("Run the medquad_downloader.py script first")
        return None
    
    # Load the dataset
    df = pd.read_csv(medquad_path)
    
    print(f"Loaded: {len(df):,} entries")
    print(f"Columns: {list(df.columns)}")
    
    # Select question and answer columns
    if 'question' in df.columns and 'answer' in df.columns:
        knowledge_df = df[['question', 'answer']].rename(columns={
            'question': 'prompt',
            'answer': 'completion'
        })
    else:
        print("ERROR: Expected 'question' and 'answer' columns not found")
        return None
    
    # Clean the data
    print(f"\nCleaning data...")
    
    # Remove empty entries
    knowledge_df = knowledge_df.dropna()
    print(f"After removing empty entries: {len(knowledge_df):,}")
    
    # Filter for reasonable answer lengths
    min_length = 50
    max_length = 3000  # Allow longer answers for patient education
    
    before_filter = len(knowledge_df)
    knowledge_df = knowledge_df[
        (knowledge_df['completion'].str.len() >= min_length) & 
        (knowledge_df['completion'].str.len() <= max_length)
    ]
    after_filter = len(knowledge_df)
    
    print(f"After length filtering ({min_length}-{max_length} chars): {after_filter:,}")
    print(f"Removed: {before_filter - after_filter:,} entries")
    
    # Remove duplicates
    before_dedup = len(knowledge_df)
    knowledge_df = knowledge_df.drop_duplicates(subset=['prompt'], keep='first')
    after_dedup = len(knowledge_df)
    
    print(f"After deduplication: {after_dedup:,}")
    print(f"Removed duplicates: {before_dedup - after_dedup:,}")
    
    # Reset index
    knowledge_df = knowledge_df.reset_index(drop=True)
    
    # Show sample of what we're creating
    print(f"\nSAMPLE KNOWLEDGE BASE ENTRIES:")
    print("-" * 60)
    
    for i in range(min(5, len(knowledge_df))):
        row = knowledge_df.iloc[i]
        print(f"ENTRY {i+1}:")
        print(f"Question: {row['prompt']}")
        print(f"Answer: {row['completion'][:300]}...")
        print(f"Length: {len(row['completion'])} characters")
        print("-" * 40)
    
    # Backup current knowledge base
    current_kb_path = '/medical_chatbot_project/data/knowledge_base_final.csv'
    if os.path.exists(current_kb_path):
        backup_path = current_kb_path.replace('.csv', '_pubmedqa_backup.csv')
        if os.path.exists(backup_path):
            os.remove(backup_path)
        os.rename(current_kb_path, backup_path)
        print(f"\nBacked up PubMedQA knowledge base to: {backup_path}")
    
    # Save new patient-friendly knowledge base
    knowledge_df.to_csv(current_kb_path, index=False)
    
    print(f"\nSUCCESS - PATIENT-FRIENDLY KNOWLEDGE BASE CREATED")
    print("="*60)
    print(f"Output file: {current_kb_path}")
    print(f"Total entries: {len(knowledge_df):,}")
    print(f"Source: NIH MedlinePlus (patient education)")
    print(f"Content type: Patient-friendly medical information")
    
    # Quality metrics
    avg_question_length = knowledge_df['prompt'].str.len().mean()
    avg_answer_length = knowledge_df['completion'].str.len().mean()
    
    print(f"\nQUALITY METRICS:")
    print(f"Average question length: {avg_question_length:.1f} characters")
    print(f"Average answer length: {avg_answer_length:.1f} characters")
    print(f"Uniqueness ratio: {knowledge_df['completion'].nunique() / len(knowledge_df):.1%}")
    
    # Compare to previous systems
    print(f"\nCOMPARISON:")
    print(f"ChatDoctor:  138K entries, 345 unique (21.8% unique), poor quality")
    print(f"PubMedQA:    273K entries, 273K unique (100% unique), too technical")
    print(f"MedQuAD:     {len(knowledge_df):,} entries, {knowledge_df['completion'].nunique():,} unique ({knowledge_df['completion'].nunique() / len(knowledge_df):.1%} unique), patient-friendly")
    
    return current_kb_path, len(knowledge_df)

def show_next_steps():
    """Show configuration and restart steps"""
    
    print(f"\nCONFIGURATION UPDATE:")
    print("-" * 30)
    print("Your app.py should already be configured correctly:")
    print("  db_path = 'data/knowledge_base_final.csv'")
    print("This file has been updated with MedQuAD content")
    
    print(f"\nRESTART PROCESS:")
    print("-" * 20)
    print("1. Clear embedding cache:")
    print("   rm chatbot_core/kb_embeddings.pt")
    print("2. Stop current server (Ctrl+C if running)")
    print("3. Restart server:")
    print("   python3 app.py")
    print("4. Test with patient questions")
    
    print(f"\nEXPECTED IMPROVEMENT:")
    print("-" * 25)
    print("BEFORE (PubMedQA): Technical research fragments")
    print("AFTER (MedQuAD):   Clear, patient-friendly explanations")

def main():
    """Main function to create MedQuAD knowledge base"""
    
    try:
        output_path, entry_count = create_medquad_knowledge_base()
        
        if output_path:
            show_next_steps()
            
            print(f"\nREADY FOR TESTING:")
            print(f"Your RAG system now has {entry_count:,} patient-friendly medical entries")
            print(f"Responses should be clear, helpful, and appropriate for general public")
            
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
