import time

from game_event.normal_event import check_if_loading, move_forward, check_confirm_button
from tools.image_tackle import is_in_image_center_point, is_in_image_center_bottom, is_in_image_original, \
    is_in_image_center_right, is_in_image_center_left
from tools.adb_event import getscreen,tap
from utils import save_image_quest_path,screenshot_path

# 任务版确认
def check_quest_window():
    check_if_loading()
    print("check quest window...")
    move_forward(250,-250)
    print("check quest window done")

# 任务版中任务第一章选择
def check_quest_first_area(threadshold=0.65,timeout=-1):
    check_if_loading()
    print("check quest first area....")
    first_quest_area_path = save_image_quest_path + 'first_area.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(first_quest_area_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check quest first area done")

# 任务出发按钮
def check_quest_chufa_button(threadshold=0.8,timeout=-1):
    print("check quest chufa button....")
    quest_confirm_button_path = save_image_quest_path + 'quest_confirm_button.png'
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(quest_confirm_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check quest chufa button done")


# 任务版中选择第一个任务
def get_first_quest(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("get first quest....")
    first_area_head_path = save_image_quest_path + 'first_area_head.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_bottom(first_area_head_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y + 10)

            time.sleep(5)
            check_confirm_button(timeout=10)

            time.sleep(1)
            check_quest_chufa_button(timeout=10)
            break
        getscreen(screenshot_path)
    print("get first quest done")

# 确认是否是任务进入前的加载
def check_if_quest_entering(threadshold=0.7):
    time.sleep(5)
    print("check if quest entering....")
    quest_entering_path = save_image_quest_path + 'quest_entering.png'

    getscreen(screenshot_path)
    times = 5
    while times > 0:
        x= is_in_image_original(quest_entering_path, screenshot_path)
        if x >= threadshold: times += 0.35
        else: times -= 1
        getscreen(screenshot_path)

    print("check if quest entering done")

def check_quest_end_button(threadshold=0.9,timeout=-1):
    print("check quest end button....")
    quest_end_button_path = save_image_quest_path + 'quest_end_button.png'
    quest_end_r1_button_path = save_image_quest_path + 'quest_end_r1_button.png'
    quest_end_r2_button_path = save_image_quest_path + 'quest_end_r2_button.png'
    quest_end_r3_button_path = save_image_quest_path + 'quest_end_r3_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_center_point(quest_end_button_path, screenshot_path, threadshold)
        x2, y2 = is_in_image_center_point(quest_end_r1_button_path, screenshot_path, threadshold)
        x3, y3 = is_in_image_center_point(quest_end_r2_button_path, screenshot_path, threadshold)
        x4, y4 = is_in_image_center_point(quest_end_r3_button_path, screenshot_path, threadshold)
        x,y = -1,-1
        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2
        elif x3 > 0 and y3 > 0: x,y = x3,y3
        elif x4 > 0 and y4 > 0: x, y = x4, y4

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check quest end button done")

def check_quest_mode_button(quest_mode="right",threadshold=0.9,timeout=-1):
    print("check quest mode button....")
    quest_mode_button_path = save_image_quest_path + 'quest_mode_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x,y = -1,-1
        if "right" == quest_mode:
            x, y = is_in_image_center_right(quest_mode_button_path, screenshot_path, threadshold,x_bias=-20)
        elif "left" == quest_mode:
            x, y = is_in_image_center_left(quest_mode_button_path, screenshot_path, threadshold,x_bias=20)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check quest mode button done")


def check_quest_exit_button(threadshold=0.9, timeout=-1):
    print("check quest exit button....")
    quest_exit_button_path = save_image_quest_path + 'quest_exit_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(quest_exit_button_path, screenshot_path, threadshold)

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check quest exit button done")

def check_quest_event_select_button(quest_mode="right",threadshold=0.9,timeout=-1):
    print("check quest event select button....")
    quest_event_select_button_path = save_image_quest_path + 'quest_event_select_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x,y = -1,-1
        if "right" == quest_mode:
            x, y = is_in_image_center_point(quest_event_select_button_path, screenshot_path, threadshold,x_bias=20)
        elif "left" == quest_mode:
            x, y = is_in_image_center_point(quest_event_select_button_path, screenshot_path, threadshold,x_bias=-20)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check quest event select button done")


