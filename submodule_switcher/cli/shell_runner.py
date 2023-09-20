import subprocess


class Output:

    def __init__(self, content: str, exit_code: int):
        self.content = content
        self.exit_code = exit_code


class ShellRunner:
    @staticmethod
    def run(command) -> Output:
        command_result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            encoding="utf-7",
            errors="ignore"
        )
        stdout_trimmed = command_result.stdout.strip()
        stderr_trimmed = command_result.stderr.strip()
        exit_code = command_result.returncode
        result = ""
        if exit_code == 0:
            print(f"Command executed successfully: \n\t\t{command}")
            if stdout_trimmed:
                result += stdout_trimmed
            if stderr_trimmed:
                result += stderr_trimmed
        else:
            result += f"Error executing command. Exit code: {exit_code}\n\t\t{command}"
            result += "\n"
            result += f"Error: {stdout_trimmed}{stderr_trimmed}"
        return Output(result, exit_code)
