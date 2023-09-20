import os
import sys

from submodule_switcher.cli.pipeline import QADTestFrameWorkPipelines


def main(app_name: str, version: str):
    QADTestFrameWorkPipelines.build_app_project(app_name, version)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(*args)
