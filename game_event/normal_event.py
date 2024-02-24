import time

from utils import save_image_path, save_image_button_path,screenshot_path, resolution_y, resolution_x
from tools.image_tackle import is_in_image_center_point, is_in_image_center_right, \
    is_in_image_bottom_right, is_in_image_original, is_in_image_center_left, is_in_image_center_top
from tools.adb_event import getscreen,tap

###################################按钮事件###################################
def check_confirm_button(threadshold=0.9,timeout=-1):
    print("check confirm button...")
    confirm_button_path = save_image_button_path + 'confirm_button.png'
    confirm_button_r1_path = save_image_button_path + 'confirm_button_r1.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_center_point(confirm_button_path, screenshot_path, threadshold)
        x2, y2 = is_in_image_center_point(confirm_button_r1_path, screenshot_path, threadshold)
        x,y = -1,-1
        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check confirm button done")

def check_unique_button(threadshold=0.9,timeout=-1):
    print("check unique button....")
    unique_info_button_path = save_image_button_path + 'unique_info_button.png'
    unique_info_r1_button_path = save_image_button_path + 'unique_info_r1_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_center_right(unique_info_button_path, screenshot_path, threadshold,x_bias=-10)
        x2, y2 = is_in_image_center_point(unique_info_r1_button_path, screenshot_path, threadshold)
        x,y = -1,-1
        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check done button done")

def check_done_button(threadshold=0.9,timeout=-1):
    print("check done button....")
    done_button_path = save_image_button_path + 'done_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(done_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check done button done")

def check_shide_button(threadshold=0.9,timeout=-1):
    print("check shide button...")
    shide_button_path = save_image_button_path + 'shide_button.png'
    shide_button_r1_path = save_image_button_path + 'shide_button_r1.png'
    shide_button_r2_path = save_image_button_path + 'shide_button_r2.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_center_point(shide_button_path, screenshot_path, threadshold)
        x2, y2 = is_in_image_center_point(shide_button_r1_path, screenshot_path, threadshold)
        x3, y3 = is_in_image_center_point(shide_button_r2_path, screenshot_path, threadshold)
        x,y = -1,-1
        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2
        elif x3 > 0 and y3 > 0: x,y = x3,y3

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check shide button done")

def check_bushi_button(threadshold=0.9,timeout=-1):
    print("check bushi button...")
    bushi_button_path = save_image_button_path + 'bushi_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(bushi_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check bushi button done")

def check_zhidao_button(threadshold=0.9,timeout=-1):
    print("check confirm button...")
    zhidao_button_path = save_image_button_path + 'zhidao_button.png'
    status_info_button_path = save_image_button_path + 'status_info_button.png'
    lottery_info_button_path = save_image_button_path + 'lottery_info_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_center_point(zhidao_button_path, screenshot_path, threadshold)
        x2, y2 = is_in_image_center_point(status_info_button_path, screenshot_path, threadshold)
        x3, y3 = is_in_image_center_point(lottery_info_button_path, screenshot_path, threadshold)
        x,y = -1,-1
        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2
        elif x3 > 0 and y3 > 0: x,y = x3,y3

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check confirm button done")

###################################按钮事件###################################

###################################游戏中###################################
# 确认是否是加载中
def check_if_loading(threadshold=0.7):
    print("check if loading.....")
    loading_path = save_image_button_path + 'loading.png'
    loading_r1_path = save_image_button_path + 'loading_r1.png'
    loading_r2_path = save_image_button_path + 'loading_r2.png'
    loading_r3_path = save_image_button_path + 'loading_r3.png'

    getscreen(screenshot_path)
    times = 5
    while times > 0:
        x1 = is_in_image_original(loading_path, screenshot_path)
        x2 = is_in_image_original(loading_r1_path, screenshot_path)
        x3 = is_in_image_original(loading_r2_path, screenshot_path)
        x4 = is_in_image_original(loading_r3_path, screenshot_path)

        max_threadshold = max({x1,x2,x3,x4})
        if max_threadshold >= threadshold: times += 0.35
        elif times > 30: times -= 2
        elif times > 15: times -= 1
        else: times -= 1

        getscreen(screenshot_path)
    print("check if loading done")

# 游戏中对话确认按钮
def chek_dialog_skip_button(threadshold=0.7,timeout=-1):
    print("chek dialog skip button.....")
    dialog_skip_button_path = save_image_button_path + 'dialog_skip_button.png'
    unique_dialog_button_path = save_image_button_path + 'unique_dialog_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_bottom_right(dialog_skip_button_path, screenshot_path, threadshold)
        x2, y2 = is_in_image_center_left(unique_dialog_button_path, screenshot_path, threadshold)
        x,y = -1,-1

        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("chek dialog skip button done")

# 游戏中对话确认
def check_dialog(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check dialog.....")
    dialog_area_path = save_image_path + 'dialog_area.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_right(dialog_area_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            chek_dialog_skip_button()
            break
        getscreen(screenshot_path)
    print("check dialog done")
    time.sleep(1)

# 游戏中无按钮消息通知确认
def check_info(timeout=-1):
    print("check info.....")
    info_area_path = save_image_path + 'info_area.png'
    info_area_r1_path = save_image_path + 'info_area_r1.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_center_point(info_area_path, screenshot_path, 0.9)
        x2, y2 = is_in_image_center_top(info_area_r1_path, screenshot_path, 0.9)
        x,y = -1,-1
        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2

        if x > 0 and y > 0: tap(x=x, y=y)
        getscreen(screenshot_path)
    print("check info done")

# 游戏中有按钮活动消息通知确定
def check_event_info(timeout=-1):
    print("check normal|unique|lottery|status event info.....")
    event_info_button_path = save_image_button_path + 'event_info_button.png'
    unique_event_info_button_path = save_image_button_path + 'unique_event_info_button.png'
    lottery_info_button_path = save_image_button_path + 'lottery_info_button.png'
    status_info_button_path = save_image_button_path + 'status_info_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1, y1 = is_in_image_center_point(event_info_button_path, screenshot_path, 0.9)
        x2, y2 = is_in_image_center_point(unique_event_info_button_path, screenshot_path, 0.9)
        x3, y3 = is_in_image_center_point(lottery_info_button_path, screenshot_path, 0.9)
        x4, y4 = is_in_image_center_point(status_info_button_path, screenshot_path, 0.9)
        x,y = -1,-1
        if x1 > 0 and y1 > 0: x,y = x1,y1
        elif x2 > 0 and y2 > 0: x,y = x2,y2
        elif x3 > 0 and y3 > 0: x,y = x3,y3
        elif x4 > 0 and y4 > 0: x,y = x4,y4

        if x > 0 and y > 0:
            tap(x=x,y=y)
            break
        getscreen(screenshot_path)
    print("check normal|unique|lottery|status event info done")

###############################################todo
# 游戏中错误消息确认
def check_error_info():
    error_area_path = save_image_path + 'error_area.png'

    getscreen(screenshot_path)
    x, y = is_in_image_center_point(error_area_path, screenshot_path, 0.9)
    if x > 0 and y > 0:
        print("check error info occur")
        tap(x=x, y=y)
    getscreen(screenshot_path)
###############################################todo

# 确认是否在主城
def check_if_in_city(threadshold=0.9,timeout=-1):
    print("check if in city.....")
    main_city_area_path = save_image_path + 'main_city_area.png'
    main_city_area_follow_path = save_image_path + 'main_city_area_follow.png'
    getscreen(screenshot_path)

    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x1 = is_in_image_original(main_city_area_path, screenshot_path)
        x2 = is_in_image_original(main_city_area_follow_path, screenshot_path)
        if max(x1,x2) >= threadshold: break
        getscreen(screenshot_path)
    print("check if in city done")

# 游戏中快速回城确认
def check_return_city(threadshold=0.9,timeout=-1):
    print("check return city button.....")
    return_city_button_path = save_image_button_path + 'return_city_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_right(return_city_button_path, screenshot_path, threadshold,x_bias=-10)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check return city button done")

###################################游戏中###################################

###################################额外添加事件###################################
def move_forward(x_bias=-100,y_bias=-100):
    tap(x=(resolution_x / 2) + x_bias, y=(resolution_y / 2) + y_bias)
    time.sleep(0.5)

###################################额外添加事件###################################


