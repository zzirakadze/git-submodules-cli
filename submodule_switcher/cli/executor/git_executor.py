from submodule_switcher.cli.command.git.git_commands import GitCommands
from submodule_switcher.cli.command.utils import CommandsUtils
from submodule_switcher.cli.constants import GitExitCodes
from submodule_switcher.cli.validator.git_validator import GitValidator
from submodule_switcher.cli.shell_runner import ShellRunner


class GitExecutor:

    @staticmethod
    def init_repository(
            submodule_path: str,
            submodule_name: str = None,
    ):
        print(f"Initiating {submodule_name}")
        init_command = GitCommands.init()
        init_command = CommandsUtils.prepend_change_dir_command(
            submodule_path,
            init_command
        )
        CommandsUtils.make_dir(submodule_path)
        init_output = ShellRunner.run(init_command)
        return init_output.exit_code == 0

    @staticmethod
    def remote_add_origin_repository(
            submodule_path: str,
            submodule_url: str = None,
    ):
        print(f"Adding remote {submodule_url}")
        add_command = GitCommands.remote_add_origin(submodule_url)
        add_command = CommandsUtils.prepend_change_dir_command(
            submodule_path,
            add_command
        )
        add_output = ShellRunner.run(add_command)
        is_added = GitValidator.is_added(add_output.exit_code)
        return is_added

    @staticmethod
    def fetch(
            submodule_path: str,
            submodule_name: str = None,
    ):
        print(f"Fetching {submodule_name}")
        fetch_command = GitCommands.fetch_origin()
        fetch_command = CommandsUtils.prepend_change_dir_command(
            submodule_path,
            fetch_command
        )
        fetch_output = ShellRunner.run(fetch_command)
        return fetch_output.exit_code == GitExitCodes.SUCCESS_EXIT_CODE

    @staticmethod
    def clone_submodule_with_directory(
        submodule_url: str, submodule_path: str, submodule_name: str = None
    ) -> bool:
        if not submodule_name:
            submodule_name = submodule_path
        print(f"Cloning {submodule_name}")
        clone_command = GitCommands.clone(submodule_url, submodule_path)
        clone_output = ShellRunner.run(clone_command)
        return GitValidator.is_cloned(clone_output.exit_code)

    @staticmethod
    def checkout_with_new_branch(
        project_path: str,
        new_branch_name: str,
        tag: str,
    ) -> int:
        print(f"Checking out {tag}")
        checkout_command = GitCommands.checkout(
            tag=tag,
            branch_name=new_branch_name,
            with_new_branch=True,
        )
        if project_path:
            checkout_command = CommandsUtils.prepend_change_dir_command(
                project_path,
                checkout_command
            )
        checked_out_result = ShellRunner.run(checkout_command)
        return checked_out_result.exit_code

    @staticmethod
    def checkout(
        project_path: str,
        branch_name: str,
    ) -> bool:
        print(f"Checking out {branch_name}")
        checkout_command = GitCommands.checkout(
            tag=branch_name,
        )
        if project_path:
            checkout_command = CommandsUtils.prepend_change_dir_command(
                project_path,
                checkout_command
            )
        checked_out_result = ShellRunner.run(checkout_command)
        return checked_out_result.exit_code == 0
