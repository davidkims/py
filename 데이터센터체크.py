import subprocess
import time

def call_process():
    # 예제로 'echo' 명령을 사용하여 '1번'이라는 문자열을 출력합니다.
    # 다른 프로세스나 명령으로 수정할 수 있습니다.
    subprocess.run(['echo', '1번'])

end_time = time.time() + 10  # 현재 시간 + 10초

while time.time() < end_time:
    call_process()
    # 필요하다면 time.sleep()을 사용하여 반복 간격을 조절할 수 있습니다.