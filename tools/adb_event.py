import os
import time

adb = 'adb -s 127.0.0.1:5555'
adb_emulator = 'adb -s emulator-5554'

def connect(deviceName):
    adb_connect = "adb connect {}".format(deviceName)
    os.system(adb_connect)

def open_game(game_name,activity_name):
    adb_shell_open = "{} shell am start -n {}/{}".format(adb,game_name,activity_name)
    os.system(adb_shell_open)
    time.sleep(2)

def stop_game(game_name):
    adb_stop = "{} shell am force-stop {}".format(adb,game_name)
    os.system(adb_stop)

def clean_game_data(game_name):
    adb_clear = "{} shell pm clear {}".format(adb,game_name)
    os.system(adb_clear)

def tap(x,y):
    adb_tap = "{} shell input tap {} {}".format(adb,x,y)
    print("click event => tap ({},{})".format(x,y))
    os.system(adb_tap)

def press(x,y,duration):
    adb_press = "{} shell input swipe {} {} {} {} {}".format(adb,x,y,x,y,duration)
    print("press event => ({},{},{})".format(x, y,duration))
    os.system(adb_press)

def swipe(x_start,y_start,x_end,y_end):
    adb_swipe = "{} shell input swipe {} {} {} {}".format(adb,x_start,y_start,x_end,y_end)
    print("scroll event => swipe ({},{},{},{})".format(x_start, y_start, x_end,y_end))
    os.system(adb_swipe)
    time.sleep(2)

def getscreen(save_path):
    adb_screencap = "{} exec-out screencap -p > {}".format(adb,save_path)
    os.system(adb_screencap)

def input_text(name):
    adb_input = "{} shell am broadcast -a ADB_INPUT_TEXT --es msg '{}'".format(adb,name)
    print("input text event => {}".format(name))
    os.system(adb_input)
