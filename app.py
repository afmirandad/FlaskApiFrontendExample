from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_ENDPOINT = "https://flaskapiexample-production.up.railway.app"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    try:
        response = requests.post(
            f"{API_ENDPOINT}/users/login",
            json={'username': username, 'password': password},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('token', 'No token received')
            return jsonify({'success': True, 'token': token})
        else:
            return jsonify({'success': False})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
