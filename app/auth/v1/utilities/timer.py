import time

class pomodoro:
    def timer():
        print("Your time starts now!")
        for i in range(4):
            t = 25*60
            while t:
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            print("Its Break Time!!")

            t = 5*60
            while t:
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                time.sleep(1)
                t -= 1
            print("Back to work!!")
