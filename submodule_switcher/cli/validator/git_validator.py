from submodule_switcher.cli.constants import GitExitCodes


class GitValidator:

    @staticmethod
    def is_cloned(exit_code):
        return exit_code in [GitExitCodes.SUCCESS_EXIT_CODE, GitExitCodes.ALREADY_EXISTS_EXIT_CODE]

    @staticmethod
    def is_added(exit_code):
        return exit_code in [GitExitCodes.SUCCESS_EXIT_CODE, GitExitCodes.ALREADY_CREATED_EXIT_CODE]
