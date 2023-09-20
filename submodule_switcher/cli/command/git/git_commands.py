from submodule_switcher.cli.command.utils import CommandsUtils


class GitCommands:

    @staticmethod
    def init():
        return "git init"

    @staticmethod
    def fetch_origin():
        return "git fetch origin"

    @staticmethod
    def remote_add_origin(submodule_url: str):
        return f"git remote add origin {submodule_url}"

    @staticmethod
    def clone(
        submodule_url: str, submodule_path: str, recurse_submodules=True
    ):
        options = ""
        if recurse_submodules:
            options += "--recurse-submodules"
        return f"git clone {options} {submodule_url} {submodule_path}"

    @staticmethod
    def checkout(
            tag: str,
            branch_name: str = "local_branch",
            with_new_branch: bool = False,
    ):
        checkout_branch_command = "git checkout"
        if with_new_branch:
            checkout_branch_command = f"{checkout_branch_command} -B {branch_name}"
        checkout_branch_command = f"{checkout_branch_command} {tag}"
        return checkout_branch_command
