import keyboard as k
import time


def time_between_action():
    time.sleep(0.4)


def end_cmd():
    k.press_and_release('alt+F4')


k.press_and_release('windows+r')

time_between_action()
k.write("cmd")
k.press_and_release("enter")

time_between_action()
k.write("rd %temp% /s /q")
k.press_and_release("enter")

time_between_action()
k.write("md %temp%")
k.press_and_release("enter")

time_between_action()
end_cmd()
