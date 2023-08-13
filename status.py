import os
import time

def list_py_files(path):
    # 주어진 경로에서 .py 파일들을 찾아 리스트로 반환
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.py')]

def show_file_status(path):
    while True:
        # .py 파일 리스트
        py_files = list_py_files(path)

        # 파일 상태 출력
        for file in py_files:
            file_path = os.path.join(path, file)
            file_stat = os.stat(file_path)
            
            # 파일 수정 시간, 크기 등의 정보를 출력
            mod_time = time.ctime(file_stat.st_mtime)
            size = file_stat.st_size
            
            print(f"File: {file}")
            print(f"Last modified: {mod_time}")
            print(f"Size: {size} bytes")
            print("-------------------------------")
        
        print("\nChecking again in 1 seconds...\n")
        time.sleep(1)  # 10초 동안 대기

path = "C:\\Users\\USER\\Desktop\\중간과제물 관련 메뉴얼"
show_file_status(path)