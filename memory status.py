import psutil

def diagnose_system_performance():
    # CPU 사용률
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # 메모리 사용량
    memory_info = psutil.virtual_memory()
    print(f"Total Memory: {memory_info.total / (1024**3):.2f} GB")
    print(f"Used Memory: {memory_info.used / (1024**3):.2f} GB ({memory_info.percent}%)")
    print(f"Available Memory: {memory_info.available / (1024**3):.2f} GB")

    # 디스크 사용량
    disk_usage = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk_usage.total / (1024**3):.2f} GB")
    print(f"Used Disk Space: {disk_usage.used / (1024**3):.2f} GB ({disk_usage.percent}%)")
    print(f"Free Disk Space: {disk_usage.free / (1024**3):.2f} GB")

    # 상위 5개 프로세스 메모리 사용량
    processes = sorted(psutil.process_iter(['pid', 'name', 'memory_info']), key=lambda x: x.info['memory_info'].rss, reverse=True)[:5]
    print("\nTop 5 Memory Consuming Processes:")
    for proc in processes:
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, Memory Usage: {proc.info['memory_info'].rss / (1024**2):.2f} MB")

if __name__ == "__main__":
    diagnose_system_performance()