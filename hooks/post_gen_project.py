import os
import shutil
import glob

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

PROJECT_PATH = glob.glob(os.getcwd())[0]


def remove_docker_files():

    file_names = [
        os.path.join(f"{PROJECT_PATH}", "docker-compose.yml"),
        os.path.join(f"{PROJECT_PATH}", "Dockerfile"),
        os.path.join(f"{PROJECT_PATH}", "Dockerfile.local"),
    ]
    for file_name in file_names:
        os.remove(file_name)


def remove_celery_files():
    file_names = [
        os.path.join(f"{PROJECT_PATH}", "src", "core", "celery.py"),
        os.path.join(
            f"{PROJECT_PATH}",
            "src",
            "core",
            "settings",
            "components",
            "celery.py",
        ),
    ]
    for file_name in file_names:
        os.remove(file_name)


def remove_docker_hooks():
    shutil.rmtree(os.path.join(f"{PROJECT_PATH}", "hooks"))
    shutil.rmtree(os.path.join(f"{PROJECT_PATH}", "bin"))


def main():
    if "{{ cookiecutter.use_docker }}".lower() == "n":
        remove_docker_files()
        remove_docker_hooks()

    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery_files()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
