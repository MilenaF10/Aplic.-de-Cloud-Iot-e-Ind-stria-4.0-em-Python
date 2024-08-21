from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update-temperature', methods=['POST'])
def update_temperature():
    data = request.get_json()
    temperature = data.get('temperature')
    print(f"Temperatura recebida: {temperature}°C")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)

