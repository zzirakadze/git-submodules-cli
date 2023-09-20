APP_REPOSITORIES_VERSIONS = {
    "Base": {
        "2023_M23": {
            "main_project": {
                "submodule_name": "git-submodules-cli",
                "path": "",
                "git_url": "https://gitlab.devops.qad.com/qa/git-submodules-cli.git",
                "tag": "command-runner-implementation",
            },
            "submodules": [
                {
                    "submodule_name": "testframework",
                    "path": "qad",
                    "git_url": "https://gitlab.devops.qad.com/subversion/test-automation/python-modules/aux/testframework.git",
                    "tag": "6.1.0",
                },
                {
                    "submodule_name": "base",
                    "path": "qad/base",
                    "git_url": "https://gitlab.devops.qad.com/subversion/test-automation/python-modules/aux/selenium/base.git",
                    "tag": "2.11.0.0",
                },
            ],
        },
        "main": {
            "main_project": {
                "submodule_name": "git-submodules-cli",
                "path": "",
                "git_url": "https://gitlab.devops.qad.com/qa/git-submodules-cli.git",
                "tag": "main",
            },
            "submodules": [
                {
                    "submodule_name": "testframework",
                    "path": "qad",
                    "git_url": "https://gitlab.devops.qad.com/subversion/test-automation/python-modules/aux/testframework.git",
                    "tag": "main",
                },
                {
                    "submodule_name": "base",
                    "path": "qad/base",
                    "git_url": "https://gitlab.devops.qad.com/subversion/test-automation/python-modules/aux/selenium/base.git",
                    "tag": "main",
                },
            ],
        }
    }
}
