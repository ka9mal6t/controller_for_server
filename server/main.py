import os
from flask import Flask, request, jsonify

from exec_comand import run_command

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)


@app.route('/exe_command', methods=['POST'])
def exe_command():
    data = request.get_json()
    command = data.get('command')
    try:
        result = run_command(command)

        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify(f'Error: {e}'), 404


if __name__ == "__main__":
    app.run()
