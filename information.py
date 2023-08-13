import os
import psutil

def check_cpu():
    """CPU 정보를 출력합니다."""
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU usage: {cpu_percent}%")

def check_disk_usage(path):
    """주어진 경로의 디스크 사용량을 출력합니다."""
    usage = psutil.disk_usage(path)
    
    print(f"Total space in {path}: {usage.total / (2**30):.2f} GB")
    print(f"Used space in {path}: {usage.used / (2**30):.2f} GB")
    print(f"Free space in {path}: {usage.free / (2**30):.2f} GB")
    print(f"Percentage used in {path}: {usage.percent}%")

if __name__ == '__main__':
    check_cpu()
    check_disk_usage('C:')
