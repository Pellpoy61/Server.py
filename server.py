from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/receive_duckyscript', methods=['POST'])
def receive_duckyscript():
    try:
        duckyscript = request.form.get('duckyscript')
        
        # Process the received Duckyscript (e.g., save to a file and execute)
        with open('/home/elliot/received_duckyscript.txt', 'w') as file:
            file.write(duckyscript)
            # Execute Duckyscript or perform desired actions

        return 'Duckyscript received successfully!'
    except Exception as e:
        print(f'Error processing Duckyscript: {e}')
        return 'Error processing Duckyscript', 500  # Return a 500 Internal Server Error response

if __name__ == '__main__':
    app.run(host='192.168.10.111', port=8080, ssl_context=('cert.pem', 'key.pem'))
