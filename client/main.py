import requests


def run_command(url, command):
    data = {'command': command}
    response = requests.post(f'{url}/exe_command',
                             json=data)
    response_data = response.json()

    if response.status_code == 200:
        result = response_data['result']
        return result
    else:
        return response_data


if __name__ == "__main__":
    while True:
        url = input("Server: ")
        while True:
            command = input("Command: ")
            if command == "--stop":
                break
            print(run_command(url, command))