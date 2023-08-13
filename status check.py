import subprocess
import sys

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"'{package_name}' has been successfully installed!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing '{package_name}': {str(e)}")

if __name__ == "__main__":
    install_package('requests')