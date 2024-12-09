import time
from playsound import playsound


def pomodoro(countdown, rest):

    study_time = int(input("How many hours would you like to study? "))
    study_quarters = study_time * 4

    for i in range(study_quarters):
        countdown_loop = countdown
        rest_loop = rest

        while countdown_loop != 0:
            print(countdown_loop, 'minutes reamining.')
            time.sleep(60)
            countdown_loop -= 1

        if i < study_quarters - 1:
            print('Bzzzzz! Time for a break')
            playsound('bells.mp3')
            while rest_loop != 0:
                print(rest_loop, 'minutes reamining of break')
                time.sleep(60)
                rest_loop -= 1
            print("You've got this! Time to study")
    print('Studying is over! Go relax')


pomodoro(25, 5)
