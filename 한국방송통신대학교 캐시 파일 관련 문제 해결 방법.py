import os

# Edge의 캐시 디렉토리 경로 (일반적으로 이 경로에 위치하지만, 버전 또는 환경에 따라 달라질 수 있습니다.)
EDGE_CACHE_PATH = os.path.expanduser('~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache')

def list_edge_cache_files():
    if not os.path.exists(EDGE_CACHE_PATH):
        print("Cannot find the Edge cache directory.")
        return []

    # 캐시 디렉토리의 파일 목록을 가져옵니다.
    cache_files = [f for f in os.listdir(EDGE_CACHE_PATH) if os.path.isfile(os.path.join(EDGE_CACHE_PATH, f))]
    
    return cache_files

if __name__ == "__main__":
    files = list_edge_cache_files()
    if files:
        print("Files in the Edge cache directory:")
        for f in files:
            print(f)
    else:
        print("No files found in the Edge cache directory or an error occurred.")