 import openai
import config
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = config.api_key

@app.route('/chatbot', methods=['POST'])
def chatbot():
    request_data = request.get_json()
    user_input = request_data['user_input']
    
    messages = [{'role':"system" ,
                "content": "eres un asistente muy bueno"}]
    
    messages.append({"role": "user", "content": user_input})

    response = openai.Completion.create(
            model="davinci", prompt=f"Sobre que quieres hablar? Usuario: {user_input} AI: ", max_tokens=60)

    response_text = response['choices'][0]['text']
    
    messages.append({"role": "assistant", "content": response_text})
    
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
