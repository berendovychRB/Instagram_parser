import os
import shutil
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config/')


def delete_config():
    if os.path.isdir(CONFIG_PATH):
        shutil.rmtree(CONFIG_PATH)


if __name__ == "__main__":
    delete_config()