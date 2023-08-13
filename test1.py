import os
import ast

def validate_python_files(directory):
    """
    주어진 디렉터리에서 파이썬 파일의 구문을 검증합니다.
    :param directory: 탐색을 시작할 디렉토리
    """
    
    if not os.path.exists(directory):
        print("지정된 경로가 존재하지 않습니다.")
        return

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    try:
                        ast.parse(content)
                        print(f"{file_path} is syntactically correct.")
                    except SyntaxError:
                        print(f"Syntax error in {file_path}")

if __name__ == '__main__':
    path = r'C:\Users'
    validate_python_files(path)
