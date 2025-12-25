import time
from datetime import datetime

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"실행 시간: {end_time - start_time}")
        return result
    return wrapper

@timer_decorator
def what_do_you_study(subject):
    time.sleep(0.5)
    print(f"I am studying {subject} at {datetime.now()}")

def main():
    print("decorator function이 이해가 안되서 예시를 만들었습니다. 함수가 실행되는 데 걸리는 시간을 알려주는 function이고," \
    "study 중인 subject를 적어주는 function을 decorate 해줍니다.")
    what_do_you_study("decorator in python")

if __name__=="__main__":
    main()
