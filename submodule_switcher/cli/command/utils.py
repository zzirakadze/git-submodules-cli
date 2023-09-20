import os


class CommandsUtils:

    @staticmethod
    def prepend_change_dir_command(project_path: str, command: str, sep="&&"):
        return CommandsUtils.join(
            f"cd {project_path}",
            command,
            sep=sep
        )

    @staticmethod
    def join(*commands, sep="&&", strip=True):
        if strip:
            sep = f" {sep} "
        return sep.join(commands)

    @staticmethod
    def make_dir(path: str):
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print(f"The new directory [{path}] is created!")
