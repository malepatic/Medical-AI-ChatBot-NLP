import torch
from transformers import AutoTokenizer, EncoderDecoderModel

def generate_response(prompt_text: str, model, tokenizer) -> str:
    """
    Generates a response from the fine-tuned model.
    """
    print("Tokenizing input...")
    inputs = tokenizer(
        prompt_text,
        padding="max_length",
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

    input_ids = inputs.input_ids.to(model.device)
    attention_mask = inputs.attention_mask.to(model.device)

    print("Generating response...")
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        # --- THIS IS THE FIX ---
        decoder_start_token_id=tokenizer.cls_token_id,
        # ----------------------
        max_length=150,
        num_beams=5,
        early_stopping=True
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

if __name__ == "__main__":
    model_path = "../outputs/biobert_finetuned_final"
    print(f"Loading model from: {model_path}")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = EncoderDecoderModel.from_pretrained(model_path).to(device)

    prompt = "Question: I have had a persistent cough for two weeks, and sometimes I feel a bit of chest tightness. What could this be?"

    generated_text = generate_response(prompt, model, tokenizer)
    
    print("\n" + "="*50)
    print(f"PROMPT: {prompt}")
    print("-"*50)
    print(f"MODEL RESPONSE: {generated_text}")
    print("="*50)
