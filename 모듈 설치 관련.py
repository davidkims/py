import subprocess

def install_module(module_name):
    """
    주어진 모듈 이름으로 모듈을 설치합니다.
    :param module_name: 설치하려는 모듈의 이름
    """
    
    try:
        print(f"Installing {module_name}...")
        result = subprocess.run(['pip', 'install', module_name], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

def list_installed_modules():
    """설치된 모듈의 목록을 출력합니다."""
    
    try:
        print("Fetching list of installed modules...")
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    module_name = input("Enter the name of the module you want to install: ")
    install_module(module_name)
    list_installed_modules()
