from flask import Flask, render_template, request, jsonify
import openai
import time

app = Flask(__name__)

openai.api_key = "PUT YOUR API KEY HERE"

def use_openai_api(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    messages = []
    messages.append({"role": "user", "content": user_input})
    response = use_openai_api(messages)
    content = response.choices[0].message['content']

    return jsonify({'chatbot_response': content})

if __name__ == '__main__':
    app.run()
