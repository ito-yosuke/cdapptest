from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']

    # Pythonスクリプトを実行し、ユーザーのメッセージを渡して出力を取得
    result = subprocess.run(
        ['python3', 'chat.py', user_message],
        capture_output=True, text=True
    )

    # Pythonスクリプトの出力を返す
    response = result.stdout.strip()

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
