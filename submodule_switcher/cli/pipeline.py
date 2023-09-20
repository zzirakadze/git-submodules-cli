from submodule_switcher.test_framework_versions import APP_REPOSITORIES_VERSIONS
from submodule_switcher.cli.executor.git_executor import GitExecutor
from submodule_switcher.cli.constants import GitExitCodes


class GitCLIPipelines:
    @staticmethod
    def clone_submodules(
            submodule_url: str,
            submodule_path: str,
            submodule_name: str = None,
            with_fetch: bool = True
    ):
        is_cloned = False
        if not with_fetch:
            # TODO Maybe redundant - remove in future whole function clone_submodule_with_directory
            is_cloned = GitExecutor.clone_submodule_with_directory(
                submodule_url,
                submodule_path,
                submodule_name,
            )
        else:
            is_initiated = GitExecutor.init_repository(submodule_path, submodule_name)
            is_added = False
            if is_initiated:
                is_added = GitExecutor.remote_add_origin_repository(submodule_path, submodule_url)
            if is_added:
                is_cloned = GitExecutor.fetch(submodule_path, submodule_name)
        if not is_cloned:
            return False

    @staticmethod
    def checkout_pipeline(project_path: str, new_branch_name: str, tag: str):
        check_out_exit_code = GitExecutor.checkout_with_new_branch(
            project_path=project_path,
            new_branch_name=new_branch_name,
            tag=tag,
        )
        if check_out_exit_code == GitExitCodes.ALREADY_EXISTS_EXIT_CODE:
            return GitExecutor.checkout(project_path, tag)
        return check_out_exit_code == GitExitCodes.SUCCESS_EXIT_CODE


class QADTestFrameWorkPipelines:
    @staticmethod
    def build_app_project(app_name: str, version: str):
        app_versions = APP_REPOSITORIES_VERSIONS[app_name]
        main_project = app_versions[version]["main_project"]
        main_project_tag = main_project["tag"]
        main_project_new_branch_name = main_project_tag
        is_main_project_switched = GitCLIPipelines.checkout_pipeline(
            project_path="",
            new_branch_name=main_project_new_branch_name,
            tag=main_project_tag,
        )
        if not is_main_project_switched:
            raise Exception("Main project has not checked out")
        for module in app_versions[version]["submodules"]:
            submodule_url = module["git_url"]
            submodule_path = module["path"]
            tag = module["tag"]
            submodule_branch_name = module["tag"]
            submodule_name = module["submodule_name"]
            GitCLIPipelines.clone_submodules(
                submodule_url,
                submodule_path,
                submodule_name,
            )
            GitCLIPipelines.checkout_pipeline(
                project_path=submodule_path,
                new_branch_name=submodule_branch_name,
                tag=tag,
            )
