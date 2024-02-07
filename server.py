from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_duckyscript', methods=['POST'])
def receive_duckyscript():
    duckyscript = request.form.get('duckyscript')
    # Process the received Duckyscript (e.g., save to a file and execute)
    with open('/home/elliot/received_duckyscript.txt', 'w') as file:
        file.write(duckyscript)
        # Execute Duckyscript or perform desired actions
    return 'Duckyscript received successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
