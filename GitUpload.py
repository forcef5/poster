import os
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')


def GitUpload():
    # os.system('git clone https://github.com/forcef5/poster.git')
    os.system('git add .')
    time.sleep(5)
    os.system('git commit -m "Upload file"')
    time.sleep(2)
    os.system('git branch -M main')
    time.sleep(2)
    os.system('git push -u origin main')
    time.sleep(2)
auto = input('Nhấn phím 1 để tự động, hoặc Enter để chạy 1 lần.\nXin mời lựa chọn : ')
if auto == '1':
    print('Bạn đã chọn tự động cập nhật Git')
    GitUpload()
    for a in range(1,9999999999):
        t = 300
        for x in range(1, int(t)):
            os.system('cls')
            print(f'Chờ upload file lần thứ {a+1}. Tự động upload sau {int(t) - x}s')
            time.sleep(1)
else:
    GitUpload()
    print('Bạn đã chọn 1 lần cập nhật Git')

