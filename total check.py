import os
import subprocess

# 대상 경로 지정
directory_path = r"C:\Users\USER\Desktop\중간과제물 관련 메뉴얼"

def execute_and_save(py_file):
    # 실행결과를 저장할 텍스트 파일 이름 지정 (예: script.py -> script_output.txt)
    output_filename = os.path.splitext(py_file)[0] + "_output.txt"
    output_path = os.path.join(directory_path, output_filename)

    # 파일 실행 및 결과 저장
    with open(output_path, 'w', encoding='utf-8') as output_file:
        try:
            result = subprocess.check_output(["python", os.path.join(directory_path, py_file)], universal_newlines=True, stderr=subprocess.STDOUT)
            output_file.write(result)
        except subprocess.CalledProcessError as e:
            output_file.write(e.output)

if __name__ == "__main__":
    # 지정된 경로에서 .py 확장자를 가진 모든 파일 목록을 가져옴
    python_files = [f for f in os.listdir(directory_path) if f.endswith('.py') and os.path.isfile(os.path.join(directory_path, f))]

    # 각 .py 파일을 실행하고 결과를 저장
    for py_file in python_files:
        execute_and_save(py_file)