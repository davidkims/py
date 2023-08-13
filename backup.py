import os
import shutil
import datetime

# 폴더 경로 지정
source_directory = r"C:\Users\USER\Desktop\중간과제물 관련 메뉴얼"
backup_directory = os.path.join(source_directory, "backup")

# 백업 로그 파일 경로 지정
log_file_path = os.path.join(source_directory, "backup_log.txt")

def backup_files():
    # 백업 폴더 생성 (이미 존재하면 생략)
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # .py 파일 찾아서 백업 폴더로 복사
    for filename in os.listdir(source_directory):
        if filename.endswith('.py'):
            source_file = os.path.join(source_directory, filename)
            backup_file = os.path.join(backup_directory, filename)
            
            # 파일 복사
            shutil.copy2(source_file, backup_file)

            # 로그 작성
            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{datetime.datetime.now()}: {filename} was backed up to {backup_file}\n")

if __name__ == "__main__":
    backup_files()