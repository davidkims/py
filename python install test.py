import subprocess

def install_or_uninstall_choco_package(package_name):
    decision = input(f"'{package_name}' 패키지를 설치하시겠습니까? (설치: Y, 삭제: D, 취소: N) ").lower()

    if decision == 'y':
        cmd = f"choco install {package_name} -y"
        subprocess.run(cmd, shell=True)
        print(f"'{package_name}' 패키지 설치 완료!")

    elif decision == 'd':
        cmd = f"choco uninstall {package_name} -y"
        subprocess.run(cmd, shell=True)
        print(f"'{package_name}' 패키지 삭제 완료!")

    else:
        print(f"'{package_name}' 패키지에 대한 작업 취소.")

if __name__ == "__main__":
    package_name = input("설치하거나 삭제하고자 하는 Chocolatey 패키지 이름을 입력하세요: ")
    install_or_uninstall_choco_package(package_name)