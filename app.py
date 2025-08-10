from flask import Flask, request, jsonify, render_template
from chatbot_core.bot import MedicalChatbot
import os

app = Flask(__name__)

# --- Initialize the Chatbot Once ---
# This loads the models into memory when the server starts
print("Starting server and initializing chatbot...")
project_root = os.path.dirname(os.path.abspath(__file__))
gen_model_path = os.path.join(project_root, "outputs/scifive_finetuned_final")
class_model_path = os.path.join(project_root, "outputs/intent_classifier_final")
db_path = os.path.join(project_root, "data/knowledge_base_final.csv")

chatbot = MedicalChatbot(
    generative_model_path=gen_model_path,
    classifier_model_path=class_model_path,
    db_path=db_path
)
print("Chatbot is ready.")

@app.route('/')
def index():
    """Serves the main HTML page for the user interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """API endpoint to handle chat messages."""
    data = request.json
    user_prompt = data.get("prompt")
    session_id = data.get("session_id")
    
    if not user_prompt or not session_id:
        return jsonify({"error": "A prompt and session_id are required."}), 400

    # Call our chatbot's main function, passing the session_id to manage memory
    response_dict = chatbot.get_response(user_prompt, session_id)
    
    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
