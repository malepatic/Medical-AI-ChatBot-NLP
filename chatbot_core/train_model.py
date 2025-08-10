import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer
from datasets import Dataset

def main():
    # 1. Load datasets
    print("Loading datasets...")
    unified_df = pd.read_csv('../data/unified_training_data.csv').dropna()
    custom_df = pd.read_csv('../data/common_diseases_dataset.csv').dropna()
    
    # 2. Ensure custom data is always included
    target_total = 12000
    custom_size = len(custom_df)
    remaining_slots = target_total - custom_size
    
    if remaining_slots > 0 and remaining_slots <= len(unified_df):
        sampled_unified = unified_df.sample(n=remaining_slots, random_state=42)
    else:
        sampled_unified = unified_df.sample(n=min(1000, len(unified_df)), random_state=42)
    
    # 3. Combine and shuffle datasets
    final_df = pd.concat([custom_df, sampled_unified], ignore_index=True)
    final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    print(f"Training dataset: {len(final_df)} examples ({custom_size} custom + {len(sampled_unified)} unified)")
    
    dataset = Dataset.from_pandas(final_df)
    
    # 4. Load model and tokenizer
    model_name = "razent/SciFive-large-Pubmed_PMC"
    print(f"Loading {model_name}...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    # 5. Tokenization function
    def preprocess_function(examples):
        inputs = [f"answer the question: {prompt}" for prompt in examples["prompt"]]
        model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")
        
        labels = tokenizer(text_target=examples["completion"], max_length=150, truncation=True, padding="max_length")
        model_inputs["labels"] = labels["input_ids"]
        
        return model_inputs
    
    print("Tokenizing dataset...")
    tokenized_dataset = dataset.map(preprocess_function, batched=True)
    
    # 6. Training arguments - FIXED for stability
    training_args = TrainingArguments(
        output_dir="../outputs/scifive_finetuned",
        num_train_epochs=3,
        per_device_train_batch_size=1,  # Reduced for stability
        learning_rate=5e-5,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='../outputs/logs',
        logging_steps=100,
        save_steps=500,
        fp16=False,  # Disabled to prevent NaN gradients
        save_total_limit=2,
        dataloader_pin_memory=False,
        max_grad_norm=1.0,  # Gradient clipping for stability
        gradient_accumulation_steps=2,  # Simulate larger batch size
    )
    
    # 7. Create trainer and start training
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )
    
    print("Starting training...")
    trainer.train()
    
    # 8. Save model
    print("Saving model...")
    trainer.save_model("../outputs/scifive_finetuned_final")
    tokenizer.save_pretrained("../outputs/scifive_finetuned_final")
    
    print("✅ Training complete! Model saved to ../outputs/scifive_finetuned_final")

if __name__ == "__main__":
    main()
