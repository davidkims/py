import psutil
import time

def long_running_processes(threshold=3600):  # 기본적으로 1시간(3600초) 이상 실행된 프로세스를 찾습니다.
    current_time = time.time()
    
    long_running = []

    for proc in psutil.process_iter(attrs=['pid', 'name', 'create_time']):
        try:
            # 프로세스의 생성 시간을 가져옵니다.
            create_time = proc.info['create_time']

            # 현재 시간과의 차이를 확인하여 장기 실행 프로세스인지 판단합니다.
            if current_time - create_time > threshold:
                long_running.append((proc.info['name'], proc.info['pid']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return long_running

if __name__ == "__main__":
    processes = long_running_processes()

    if processes:
        print("Long running processes:")
        for name, pid in processes:
            print(f"Name: {name}, PID: {pid}")
    else:
        print("No long running processes found.")