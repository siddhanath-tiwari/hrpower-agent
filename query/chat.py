import os
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Environment variables load karo
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Groq API ka model
            messages=[
                {"role": "system", "content": "You are an expert HR assistant. You help in resume screening, interview scheduling, and answering HR-related queries."},
                {"role": "user", "content": user_input}
            ],
            api_key=GROQ_API_KEY
        )
        return jsonify({"response": response['choices'][0]['message']['content']})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
