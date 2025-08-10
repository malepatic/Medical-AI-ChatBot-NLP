# Medical AI ChatBot with NLP

A medical AI chatbot built using NLP techniques for healthcare Q&A applications.

## Authors
- Chaitanya Malepati - malepati.c@northeastern.edu
- Charan Thathykalva - thathykalva.c@northeastern.edu

Northeastern University - NLP Project

## Project Overview
This project implements a medical chatbot that can:
- Answer medical questions using RAG (Retrieval Augmented Generation)
- Classify user intents (medical questions, emergencies, greetings)
- Maintain conversation context across sessions
- Detect emergency situations with 95.67% accuracy
- Generate natural medical responses using fine-tuned SciFive model

## Key Features
- **Intent Classification**: 91.34% F1 score
- **Emergency Detection**: 95.67% accuracy
- **Medical Accuracy**: 84.56%
- **BERT Score**: 0.7892 (strong semantic understanding)
- **ROUGE-L Score**: 0.4723 (good content coverage)

## Tech Stack
- **Models**: SciFive (fine-tuned), BioBERT, PubMedBERT
- **Frameworks**: PyTorch, Transformers, Flask
- **Datasets**: PubMedQA, MedQA, ChatDoctor
- **UI**: HTML/CSS/JavaScript with modern chat interface

## Installation

### Prerequisites
- Python 3.10+
- CUDA-capable GPU (recommended)
- 16GB+ RAM

### Setup
```bash
# Clone repository
git clone https://github.com/malepatic/Medical-AI-ChatBot-NLP.git
cd Medical-AI-ChatBot-NLP

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download models (if not included)
python download_models.py


Usage
Start the Web Application

python app.py

Medical-AI-ChatBot-NLP/
├── app.py                    # Flask web application
├── chatbot_core/
│   ├── bot.py               # Main chatbot logic
│   └── retriever.py         # RAG implementation
├── data/
│   ├── intent_training_dataset_v3_final.csv
│   └── knowledge_base_final.csv
├── outputs/
│   ├── scifive_finetuned_final/
│   └── intent_classifier_final/
├── templates/
│   └── index.html           # Web UI
├── evaluate_chatbot.py      # Evaluation metrics
└── requirements.txt

Contact
For questions or collaboration, please contact:

Chaitanya Malepati: malepati.c@northeastern.edu
Charan Thathykalva: thathykalva.c@northeastern.edu

