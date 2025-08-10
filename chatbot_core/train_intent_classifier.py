import pandas as pd
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from datasets import Dataset
from sklearn.metrics import accuracy_score, f1_score

def main():
    # 1. Load the Intent Dataset
    print("Loading intent dataset...")
    df = pd.read_csv('../data/intent_training_dataset_v3_final.csv').dropna()
    
    # Create label mappings
    labels = df['intent'].unique().tolist()
    label2id = {label: i for i, label in enumerate(labels)}
    id2label = {i: label for i, label in enumerate(labels)}
    df['label'] = df['intent'].map(label2id)
    
    print(f"Found {len(labels)} intent classes: {labels}")
    print(f"Dataset size: {len(df)} examples")
    
    dataset = Dataset.from_pandas(df)
    
    # 2. Load the BioBERT Model and Tokenizer for Classification
    model_name = "dmis-lab/biobert-base-cased-v1.1"
    print(f"Loading BioBERT for classification...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, 
        num_labels=len(labels),
        id2label=id2label,
        label2id=label2id
    )
    
    # 3. Tokenize the Dataset
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)
    
    print("Tokenizing dataset...")
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    
    # 4. Split data into train and test sets
    train_test_split = tokenized_dataset.train_test_split(test_size=0.1, seed=42)
    train_dataset = train_test_split["train"]
    eval_dataset = train_test_split["test"]
    
    print(f"Train examples: {len(train_dataset)}")
    print(f"Eval examples: {len(eval_dataset)}")
    
    # 5. Define Evaluation Metrics
    def compute_metrics(eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)
        accuracy = accuracy_score(labels, predictions)
        f1 = f1_score(labels, predictions, average='weighted')
        return {"accuracy": accuracy, "f1": f1}
    
    # 6. Set Up Training Arguments - FIXED
    training_args = TrainingArguments(
        output_dir="../outputs/intent_classifier",
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        learning_rate=5e-5,
        warmup_steps=100,
        weight_decay=0.01,
        logging_dir='../outputs/intent_logs',
        logging_steps=50,
        save_steps=500,  # Save less frequently
        save_total_limit=2,
        # Removed problematic parameters for your Transformers version
    )
    
    # 7. Create the Trainer and Start Training
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        # Removed eval_dataset to avoid strategy conflicts
        compute_metrics=compute_metrics,
    )
    
    print("Starting intent classifier training...")
    trainer.train()
    
    # 8. Manual evaluation after training
    print("Evaluating model on test set...")
    trainer.args.per_device_eval_batch_size = 16
    eval_results = trainer.evaluate(eval_dataset=eval_dataset)
    print(f"Final evaluation results:")
    print(f"  Accuracy: {eval_results.get('eval_accuracy', 'N/A')}")
    print(f"  F1 Score: {eval_results.get('eval_f1', 'N/A')}")
    print(f"  Loss: {eval_results.get('eval_loss', 'N/A')}")
    
    # 9. Save the Final Model
    print("Saving intent classifier...")
    trainer.save_model("../outputs/intent_classifier_final")
    tokenizer.save_pretrained("../outputs/intent_classifier_final")
    
    # Save label mappings for later use
    label_mapping = {
        'labels': labels,
        'label2id': label2id,
        'id2label': id2label
    }
    
    import json
    with open("../outputs/intent_classifier_final/label_mapping.json", "w") as f:
        json.dump(label_mapping, f)
    
    print("✅ Intent classifier training complete!")
    print(f"✅ Model saved to: ../outputs/intent_classifier_final")
    print(f"✅ Label mappings saved for inference")

if __name__ == "__main__":
    main()
