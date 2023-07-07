import time
import os

while True:
    os.system('clear')  # 对于windows操作系统, 请使用'cls'
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f'当前时间: {current_time}')
    time.sleep(1)
