import time

def timer():
    time_s = int(input("타이머 초를 입력: "))

    time_m = 0
    if time_s > 59:
        time_m = time_s // 60
        time_s = time_s - (time_m * 60)

    while time_m:
        for i in range(time_s, -1 ,-1):
            print(f"{time_m}분 {i}초")
            time.sleep(1)
        time_m = time_m - 1
        time_s = 59
    for i in range(time_s, -1 ,-1):
        if i == 0:
            print("타이머 종료")
        else:
            print(f"{i}초")
            time.sleep(1)
        
    
timer() 
