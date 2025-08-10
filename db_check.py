#!/usr/bin/env python3
"""
MedQuAD Dataset Downloader and Inspector
Downloads and analyzes multiple MedQuAD dataset versions
"""

import pandas as pd
import sys
import os
import subprocess
from datasets import load_dataset

def download_medquad_options():
    """Download and compare different MedQuAD dataset options"""
    
    print("MEDQUAD DATASET DOWNLOADER AND INSPECTOR")
    print("="*60)
    
    # Available MedQuAD datasets from search results
    medquad_datasets = [
        {
            'name': 'lavita/MedQuAD',
            'description': 'Converted version, some content removed for copyright',
            'note': 'Missing some MedlinePlus content'
        },
        {
            'name': 'Amirkid/MedQuad-dataset', 
            'description': '32.8k rows, 8.76 MB',
            'note': 'Good size, full format'
        },
        {
            'name': 'keivalya/MedQuad-MedicalQnADataset',
            'description': '16.4k rows, question-answer format',
            'note': 'Smaller but clean format'
        },
        {
            'name': 'Tonic/medquad',
            'description': '15.5k rows, parquet format',
            'note': 'Compact version'
        }
    ]
    
    successful_downloads = []
    
    for dataset_info in medquad_datasets:
        dataset_name = dataset_info['name']
        print(f"\nTrying to download: {dataset_name}")
        print(f"Description: {dataset_info['description']}")
        print("-" * 50)
        
        try:
            # Try to load the dataset
            print(f"Loading {dataset_name}...")
            dataset = load_dataset(dataset_name)
            
            if 'train' in dataset:
                df = dataset['train'].to_pandas()
            else:
                # Get the first available split
                split_name = list(dataset.keys())[0]
                df = dataset[split_name].to_pandas()
            
            print(f"SUCCESS: Loaded {len(df):,} entries")
            print(f"Columns: {list(df.columns)}")
            
            # Analyze the structure
            analyze_medquad_structure(df, dataset_name)
            
            # Save locally for comparison
            output_path = f"/medical_chatbot_project/data/medquad_{dataset_name.replace('/', '_')}.csv"
            df.to_csv(output_path, index=False)
            
            successful_downloads.append({
                'name': dataset_name,
                'df': df,
                'path': output_path,
                'size': len(df)
            })
            
            print(f"Saved to: {output_path}")
            
        except Exception as e:
            print(f"FAILED: {e}")
    
    return successful_downloads

def analyze_medquad_structure(df, dataset_name):
    """Analyze MedQuAD dataset structure and content quality"""
    
    print(f"\nANALYZING: {dataset_name}")
    print("-" * 40)
    
    # Basic statistics
    print(f"Rows: {len(df):,}")
    print(f"Columns: {list(df.columns)}")
    
    # Look for question/answer columns
    question_cols = [col for col in df.columns if 'question' in col.lower()]
    answer_cols = [col for col in df.columns if any(word in col.lower() for word in ['answer', 'completion', 'response'])]
    
    print(f"Question columns: {question_cols}")
    print(f"Answer columns: {answer_cols}")
    
    if question_cols and answer_cols:
        q_col = question_cols[0]
        a_col = answer_cols[0]
        
        # Show sample Q&A pairs
        print(f"\nSAMPLE Q&A PAIRS:")
        print("-" * 30)
        
        for i in range(min(3, len(df))):
            question = df.iloc[i][q_col]
            answer = df.iloc[i][a_col]
            
            print(f"Q{i+1}: {question}")
            print(f"A{i+1}: {str(answer)[:200]}...")
            print(f"Answer length: {len(str(answer))} characters")
            print("-" * 25)
        
        # Assess patient-friendliness
        sample_answers = [str(df.iloc[i][a_col]) for i in range(min(10, len(df)))]
        assess_patient_friendliness(sample_answers, dataset_name)
    
    else:
        print("No clear Q&A structure found")

def assess_patient_friendliness(sample_answers, dataset_name):
    """Assess how patient-friendly the content is"""
    
    print(f"\nPATIENT-FRIENDLINESS ASSESSMENT: {dataset_name}")
    print("-" * 45)
    
    # Check for technical vs patient-friendly language
    technical_indicators = [
        'cytokines', 'pathogenesis', 'etiology', 'immunoglobulin', 'biomarkers',
        'meta-analysis', 'randomized controlled trial', 'systematic review'
    ]
    
    patient_friendly_indicators = [
        'symptoms include', 'treatment options', 'when to see a doctor',
        'home remedies', 'lifestyle changes', 'common causes'
    ]
    
    technical_count = 0
    patient_friendly_count = 0
    
    for answer in sample_answers:
        answer_lower = answer.lower()
        
        if any(indicator in answer_lower for indicator in technical_indicators):
            technical_count += 1
        
        if any(indicator in answer_lower for indicator in patient_friendly_indicators):
            patient_friendly_count += 1
    
    total_samples = len(sample_answers)
    
    print(f"Technical language: {technical_count}/{total_samples} ({technical_count/total_samples*100:.1f}%)")
    print(f"Patient-friendly language: {patient_friendly_count}/{total_samples} ({patient_friendly_count/total_samples*100:.1f}%)")
    
    if patient_friendly_count > technical_count:
        print("ASSESSMENT: Patient-friendly content - GOOD for chatbot")
    elif technical_count > patient_friendly_count:
        print("ASSESSMENT: Technical content - may be too complex")
    else:
        print("ASSESSMENT: Mixed content - review samples needed")

def compare_datasets(successful_downloads):
    """Compare all successfully downloaded datasets"""
    
    if not successful_downloads:
        print("No datasets downloaded successfully")
        return
    
    print(f"\nDATASET COMPARISON")
    print("="*50)
    
    print(f"Available options:")
    for i, dataset in enumerate(successful_downloads, 1):
        print(f"{i}. {dataset['name']}: {dataset['size']:,} entries")
        print(f"   Path: {dataset['path']}")
    
    print(f"\nRECOMMENDATION:")
    
    # Find the largest dataset with good structure
    best_dataset = max(successful_downloads, key=lambda x: x['size'])
    
    print(f"Best option: {best_dataset['name']}")
    print(f"Size: {best_dataset['size']:,} entries")
    print(f"Reason: Largest dataset with proper Q&A structure")
    
    return best_dataset

def main():
    """Main function to download and analyze MedQuAD options"""
    
    try:
        # Install required package
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'datasets'], check=True)
        
        # Download and analyze datasets
        successful_downloads = download_medquad_options()
        
        if successful_downloads:
            best_dataset = compare_datasets(successful_downloads)
            
            print(f"\nNEXT STEPS:")
            print("1. Review the sample Q&A pairs above")
            print("2. Choose the most patient-friendly dataset")
            print("3. Create knowledge base from chosen dataset")
            print("4. Replace current knowledge base")
            print("5. Test improved responses")
            
            print(f"\nRECOMMENDED:")
            print(f"Use {best_dataset['name']} with {best_dataset['size']:,} entries")
            print(f"File ready at: {best_dataset['path']}")
        else:
            print("Failed to download any MedQuAD datasets")
            print("Consider using alternative medical datasets or manual curation")
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
