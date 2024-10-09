from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get the prompt from the POST request data
        data = request.json
        prompt = data.get("prompt", "")

        # Check if prompt is provided
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Use the Gemini API to generate content
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        # Return the generated text as a response
        return jsonify({"response": response.text}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5005)