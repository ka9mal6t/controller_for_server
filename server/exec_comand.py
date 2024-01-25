import subprocess


def read_history() -> list[str]:
    history = ""
    with open('history.txt', 'r', encoding='utf-8') as file:
        history = file.read().strip()
    history = history.split("\n")
    return history


def write_history(command):
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(command + '\n')


def clear_history():
    with open('history.txt', 'w', encoding='utf-8') as file:
        file.write('')


def run_command(command: str) -> str:
    try:
        encoding = ""
        save = False
        if "--encoding=" in command:
            encoding = (command.split()[0]).split("--encoding=")[-1]
            command = ' '.join((command.split(" ")[1:]))
        if "--save " in command:
            command = command.split("--save ")[-1]
            save = True

        elif command == "--clear":
            clear_history()
            return "History was cleared"
        history_command = " && ".join(read_history())
        if history_command.strip() != "":
            history_command += f" && {command}"
        else:
            history_command = command
        if encoding:
            result = subprocess.check_output(history_command, shell=True, text=True, encoding=encoding)
        else:
            result = subprocess.check_output(history_command, shell=True, text=True)
        if save:
            write_history(command)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # print(run_command("--encoding=cp866 dir"))
    while True:
        a = input()
        print(run_command(a))
        print(read_history())
