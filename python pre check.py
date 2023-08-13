import subprocess
import sys

def uninstall_module(module_name):
    """
    주어진 모듈 이름을 pip를 사용하여 삭제합니다.
    :param module_name: 삭제할 모듈의 이름
    """
    try:
        # 파이썬의 경로를 사용하여 pip를 호출
        pip_path = f"{sys.executable} -m pip"
        subprocess.check_call(f"{pip_path} uninstall {module_name} -y", shell=True)
        print(f"'{module_name}' module successfully uninstalled!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while uninstalling '{module_name}' module. Error: {e}")

if __name__ == '__main__':
    uninstall_module("requests")