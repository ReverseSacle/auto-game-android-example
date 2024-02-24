import time

from utils import screenshot_path, save_image_start_page_path
from tools.image_tackle import is_in_image_center_point, is_in_image_center_right, \
    is_in_image_bottom_left, is_in_image_bottom_right, is_in_image_bottom_right_left, is_in_image_center_bottom, \
    is_in_image_original
from tools.adb_event import getscreen,tap,swipe


###################################未进入游戏中###################################
# 游戏启动画面
# 游戏启动google警告确认
def check_start_warning(threadshold=0.9,timeout=-1):
    print("check start warning.....")
    start_warning_path = save_image_start_page_path + 'start_warning.png'
    getscreen(screenshot_path)

    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_bottom_right_left(start_warning_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check start warning done")

# 游戏启动画面确认
def check_start_page(threadshold=0.8,timeout=-1):
    print("check start page.....")
    start_page_path = save_image_start_page_path + 'start_page.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(start_page_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check start page done")

# 游戏区域选择
def check_area_select(threadshold=0.8,timeout=-1):
    print("check area select.....")
    area_select_path = save_image_start_page_path + 'area_select.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(area_select_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            #### 14区一定要这样写
            y += 150
            swipe(x,y,x,y - 218)
            #####################

            time.sleep(1.5)
            area_select_button_path = save_image_start_page_path + 'area_select_button.png'
            getscreen(screenshot_path)
            while True:
                x, y = is_in_image_center_point(area_select_button_path, screenshot_path, threadshold)
                if x > 0 and y > 0:
                    tap(x=x, y=y)
                    break
                getscreen(screenshot_path)
            break
        getscreen(screenshot_path)
    print("check area select done")

# 等待预下载页面
def waiting_for_pre_downloading_area(threadshold=0.8,timeout=-1):
    print("waiting for pre downloading area.....")
    download_pre_loading_path = save_image_start_page_path + 'download_pre_loading.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x = is_in_image_original(download_pre_loading_path, screenshot_path)
        if x >= threadshold: break
        getscreen(screenshot_path)
    print("waiting for pre downloading area done")

# 游戏预下载确认
def check_if_pre_download(threadshold=0.8,timeout=-1):
    print("check if pre-download.....")
    start_download_button_path = save_image_start_page_path + 'start_download_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_bottom_left(start_download_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check if pre-download done")

# 游戏下载完成确认
def check_if_download_end(threadshold=0.8,timeout=-1):
    print("check if download end.....")
    download_end_button_path = save_image_start_page_path + 'download_end_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_bottom(download_end_button_path, screenshot_path, threadshold, y_bias=-10)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check if download end done")

# 游戏额外下载确认
def check_if_extra_download(threadshold=0.8,timeout=-1):
    print("check if extra-download.....")
    start_download_button_path = save_image_start_page_path + 'extra_download_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_bottom_right(start_download_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check if extra-download done")

# 游戏条约
def check_constraint(threadshold=0.8,timeout=-1):
    print("check constraint.....")
    constraint_button_path = save_image_start_page_path + 'constraint_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_bottom_right(constraint_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)

            time.sleep(1)
            constraint_confirm_button_path = save_image_start_page_path + 'constraint_confirm_button.png'

            getscreen(screenshot_path)
            while True:
                x, y = is_in_image_bottom_right(constraint_confirm_button_path, screenshot_path, threadshold)
                if x > 0 and y > 0:
                    tap(x=x, y=y)
                    break
                getscreen(screenshot_path)
            break
        getscreen(screenshot_path)
    print("check constraint done")

# 游戏性别
def check_gender(threadshold=0.8,timeout=-1):
    print("check gender.....")
    gender_button_path = save_image_start_page_path + 'gender_select_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_right(gender_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)

            time.sleep(1)
            confirm_button_path = save_image_start_page_path + 'confirm_button.png'

            getscreen(screenshot_path)
            while True:
                x, y = is_in_image_center_bottom(confirm_button_path, screenshot_path, threadshold,y_bias=-10)
                if x > 0 and y > 0:
                    tap(x=x, y=y)
                    break
                getscreen(screenshot_path)
            break
        getscreen(screenshot_path)
    print("check gender done")

###################################未进入游戏中###################################