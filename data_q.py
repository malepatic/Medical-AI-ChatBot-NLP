#!/usr/bin/env python3
"""
Medical Knowledge Base Quality Analyzer
Comprehensive analysis of the entire knowledge base to identify quality issues,
inconsistencies, and areas for improvement - NO PLOTTING DEPENDENCIES
"""

import pandas as pd
import numpy as np
from collections import Counter, defaultdict
import re

class MedicalKnowledgeBaseAnalyzer:
    def __init__(self, db_path):
        self.db_path = db_path
        self.df = pd.read_csv(db_path).dropna()
        print(f"📊 Loaded knowledge base: {len(self.df)} entries")
        print(f"📋 Columns: {list(self.df.columns)}")
    
    def basic_statistics(self):
        """Generate basic statistics about the knowledge base"""
        print("\n" + "="*60)
        print("📈 BASIC STATISTICS")
        print("="*60)
        
        # Entry count and uniqueness
        total_entries = len(self.df)
        unique_prompts = self.df['prompt'].nunique()
        unique_completions = self.df['completion'].nunique()
        
        print(f"Total entries: {total_entries}")
        print(f"Unique prompts: {unique_prompts} ({unique_prompts/total_entries:.1%})")
        print(f"Unique completions: {unique_completions} ({unique_completions/total_entries:.1%})")
        
        # Text length analysis
        prompt_lengths = self.df['prompt'].str.len()
        completion_lengths = self.df['completion'].str.len()
        
        print(f"\n📝 TEXT LENGTH ANALYSIS:")
        print(f"Prompt lengths - Mean: {prompt_lengths.mean():.1f}, Median: {prompt_lengths.median():.1f}, Range: {prompt_lengths.min()}-{prompt_lengths.max()}")
        print(f"Completion lengths - Mean: {completion_lengths.mean():.1f}, Median: {completion_lengths.median():.1f}, Range: {completion_lengths.min()}-{completion_lengths.max()}")
        
        # Show very short and very long entries
        short_completions = self.df[completion_lengths < 50]
        long_completions = self.df[completion_lengths > 800]
        
        if len(short_completions) > 0:
            print(f"\n {len(short_completions)} very short completions (<50 chars):")
            for idx, row in short_completions.head(5).iterrows():
                print(f"   '{row['completion']}'")
        
        if len(long_completions) > 0:
            print(f"\n  {len(long_completions)} very long completions (>800 chars):")
            for idx, row in long_completions.head(3).iterrows():
                print(f"   Length {len(row['completion'])}: '{row['completion'][:100]}...'")
        
        return {
            'total_entries': total_entries,
            'unique_prompts': unique_prompts,
            'unique_completions': unique_completions,
            'avg_prompt_length': prompt_lengths.mean(),
            'avg_completion_length': completion_lengths.mean()
        }
    
    def find_duplicates(self):
        """Identify duplicate and near-duplicate entries"""
        print("\n" + "="*60)
        print(" DUPLICATE ANALYSIS")
        print("="*60)
        
        # Exact duplicates in completions
        completion_counts = self.df['completion'].value_counts()
        duplicates = completion_counts[completion_counts > 1]
        
        print(f"Found {len(duplicates)} completion texts with duplicates")
        print(f"Total duplicate entries: {duplicates.sum() - len(duplicates)}")
        
        if len(duplicates) > 0:
            print(f"\n TOP DUPLICATE COMPLETIONS:")
            print("-" * 70)
            for completion, count in duplicates.head(10).items():
                print(f"APPEARS {count} TIMES:")
                print(f"'{completion}'")
                print("-" * 40)
                
                # Show which prompts have this same completion
                matching_prompts = self.df[self.df['completion'] == completion]['prompt'].tolist()
                print(f"Used for prompts:")
                for prompt in matching_prompts:
                    print(f"  • {prompt}")
                print("-" * 70)
        
        return duplicates
    
    def analyze_medical_topics(self):
        """Analyze medical topics and their coverage"""
        print("\n" + "="*60)
        print(" MEDICAL TOPIC ANALYSIS")
        print("="*60)
        
        # Define medical topic keywords
        medical_topics = {
            'diabetes': ['diabetes', 'diabetic', 'insulin', 'glucose', 'blood sugar'],
            'cardiovascular': ['heart', 'blood pressure', 'hypertension', 'cardiac', 'cardiovascular'],
            'respiratory': ['lung', 'breathing', 'asthma', 'pneumonia', 'respiratory', 'cough'],
            'infection': ['infection', 'bacterial', 'viral', 'antibiotic', 'fever'],
            'mental_health': ['depression', 'anxiety', 'mental health', 'stress', 'psychological'],
            'gastrointestinal': ['stomach', 'intestinal', 'digestive', 'nausea', 'diarrhea'],
            'musculoskeletal': ['bone', 'joint', 'muscle', 'arthritis', 'fracture'],
            'neurological': ['brain', 'neurological', 'seizure', 'headache', 'migraine'],
            'dermatological': ['skin', 'rash', 'dermatitis', 'eczema', 'dermatological'],
            'reproductive': ['pregnancy', 'reproductive', 'gynecological', 'menstrual'],
            'endocrine': ['hormone', 'thyroid', 'endocrine', 'metabolism'],
            'kidney': ['kidney', 'renal', 'urinary', 'bladder']
        }
        
        topic_coverage = {}
        topic_entries = defaultdict(list)
        
        for topic, keywords in medical_topics.items():
            mask = self.df['completion'].str.contains('|'.join(keywords), case=False, na=False)
            count = mask.sum()
            topic_coverage[topic] = count
            
            # Store entries for this topic
            if count > 0:
                topic_entries[topic] = self.df[mask]['completion'].tolist()
        
        # Sort by coverage
        sorted_topics = sorted(topic_coverage.items(), key=lambda x: x[1], reverse=True)
        
        print(f"📊 TOPIC COVERAGE (entries per topic):")
        for topic, count in sorted_topics:
            percentage = (count / len(self.df)) * 100
            status = "done" if count >= 5 else "⚠️warning" if count >= 1 else "❌"
            print(f"{status} {topic:15}: {count:3d} entries ({percentage:4.1f}%)")
        
        # Show sample entries for top topics
        print(f"\n SAMPLE ENTRIES BY TOPIC:")
        for topic, count in sorted_topics[:3]:  # Top 3 topics
            if count > 0:
                print(f"\n{topic.upper()} ({count} entries):")
                print("-" * 50)
                sample_entries = topic_entries[topic][:2]  # Show 2 samples
                for i, entry in enumerate(sample_entries, 1):
                    print(f"Sample {i}: {entry[:200]}...")
                    print()
        
        return topic_coverage, topic_entries
    
    def check_content_quality(self):
        """Analyze content quality metrics"""
        print("\n" + "="*60)
        print("✨ CONTENT QUALITY ANALYSIS")
        print("="*60)
        
        quality_issues = []
        
        # Check for very short completions (likely incomplete)
        short_completions = self.df[self.df['completion'].str.len() < 50]
        if len(short_completions) > 0:
            quality_issues.append(f"Found {len(short_completions)} very short completions (<50 chars)")
            print(f"  {len(short_completions)} very short completions (<50 characters)")
        
        # Check for very long completions (might be too verbose)
        long_completions = self.df[self.df['completion'].str.len() > 800]
        if len(long_completions) > 0:
            quality_issues.append(f"Found {len(long_completions)} very long completions (>800 chars)")
            print(f" {len(long_completions)} very long completions (>800 characters)")
        
        # Check for generic/template responses
        generic_patterns = [
            'under medical supervision',
            'consult your doctor',
            'see a healthcare provider',
            'medical attention',
            'healthy eating, regular exercise'
        ]
        
        generic_count = 0
        for pattern in generic_patterns:
            mask = self.df['completion'].str.contains(pattern, case=False, na=False)
            pattern_count = mask.sum()
            if pattern_count > 10:  # If pattern appears more than 10 times
                print(f" Pattern '{pattern}' appears {pattern_count} times (may be overused)")
                generic_count += pattern_count
        
        if generic_count > 50:
            quality_issues.append("High use of generic medical advice patterns")
        
        # Check for medical advice patterns
        advice_patterns = {
            'see_doctor': ['see a doctor', 'consult', 'healthcare provider', 'medical attention'],
            'emergency': ['emergency', 'call 911', 'immediate', 'urgent'],
            'lifestyle': ['diet', 'exercise', 'lifestyle', 'healthy'],
            'medication': ['medication', 'prescription', 'drug', 'treatment']
        }
        
        pattern_counts = {}
        for pattern_name, keywords in advice_patterns.items():
            mask = self.df['completion'].str.contains('|'.join(keywords), case=False, na=False)
            pattern_counts[pattern_name] = mask.sum()
        
        print(f"\n🔍 MEDICAL ADVICE PATTERNS:")
        for pattern, count in pattern_counts.items():
            percentage = (count / len(self.df)) * 100
            print(f"   {pattern:12}: {count:3d} entries ({percentage:4.1f}%)")
        
        return quality_issues, pattern_counts
    
    def show_all_entries(self, max_entries=None):
        """Display all entries for manual review"""
        print("\n" + "="*60)
        print(" ALL DATABASE ENTRIES")
        print("="*60)
        
        entries_to_show = len(self.df) if max_entries is None else min(max_entries, len(self.df))
        
        for idx, row in self.df.head(entries_to_show).iterrows():
            print(f"\nENTRY {idx + 1}:")
            print(f"Prompt: {row['prompt']}")
            print(f"Completion: {row['completion']}")
            print(f"Length: {len(row['completion'])} characters")
            
            # Quality flags
            flags = []
            if len(row['completion']) < 50:
                flags.append(" VERY SHORT")
            if len(row['completion']) > 800:
                flags.append("  VERY LONG")
            if 'diabetes' in row['completion'].lower():
                flags.append(" DIABETES")
            if any(pattern in row['completion'].lower() for pattern in ['consult', 'see a doctor', 'medical supervision']):
                flags.append(" GENERIC ADVICE")
            
            if flags:
                print(f"Flags: {' '.join(flags)}")
            
            print("-" * 80)
        
        if len(self.df) > entries_to_show:
            print(f"\n... and {len(self.df) - entries_to_show} more entries")
            print("Run with max_entries=None to see all entries")

def main():
    """Main analysis function"""
    print("MEDICAL KNOWLEDGE BASE QUALITY ANALYZER")
    print("="*60)
    
    # Initialize analyzer
    db_path = "/medical_chatbot_project/data/common_diseases_dataset.csv"
    analyzer = MedicalKnowledgeBaseAnalyzer(db_path)
    
    # Run all analyses
    stats = analyzer.basic_statistics()
    duplicates = analyzer.find_duplicates()
    topic_coverage, topic_entries = analyzer.analyze_medical_topics()
    quality_issues, advice_patterns = analyzer.check_content_quality()
    
    # Show all entries for review (limit to first 50 for initial review)
    print(f"\n🔍 Would you like to see all entries? This will be long output.")
    print(f"For now, showing first 20 entries for quick review:")
    analyzer.show_all_entries(max_entries=20)
    
    print("\n" + "="*60)
    print(" ANALYSIS SUMMARY")
    print("="*60)
    print(f" Database loaded: {len(analyzer.df)} entries")
    print(f" Unique completions: {stats['unique_completions']} ({stats['unique_completions']/stats['total_entries']:.1%})")
    print(f" Quality issues found: {len(quality_issues)}")
    print(f" Entries with duplicates: {len(duplicates)}")
    
    print(f"\n KEY RECOMMENDATIONS:")
    
    # Specific recommendations based on findings
    if len(duplicates) > 0:
        print(f"1. Remove {duplicates.sum() - len(duplicates)} duplicate entries")
    
    if stats['unique_completions'] / stats['total_entries'] < 0.8:
        print(f"2. Add more diverse, unique content (only {stats['unique_completions']/stats['total_entries']:.1%} unique)")
    
    low_coverage_topics = [topic for topic, count in topic_coverage.items() if count < 3]
    if low_coverage_topics:
        print(f"3. Add content for topics: {', '.join(low_coverage_topics[:5])}")
    
    if quality_issues:
        print(f"4. Address quality issues:")
        for issue in quality_issues[:3]:
            print(f"   • {issue}")
    
    print(f"\n NEXT STEPS:")
    print(f"1. Review the entries shown above")
    print(f"2. Run the data enhancement script to add quality content")
    print(f"3. Remove duplicate entries")
    print(f"4. To see ALL entries, modify max_entries=None in the code")

if __name__ == "__main__":
    main()
