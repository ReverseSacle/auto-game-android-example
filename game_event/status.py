import time

from game_event.normal_event import check_event_info, check_if_loading, check_shide_button
from tools.adb_event import getscreen, tap, swipe
from tools.image_tackle import is_in_image_center_point, is_in_image_center_bottom, is_in_image_center_left, \
    is_in_image_center_right, is_in_image_bottom_right_top
from utils import save_image_status_path, screenshot_path, getscreen_in_character_folder

#################################状态栏控件区域#################################
# 游戏中状态栏选择
def check_status_area(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check status area....")
    status_button_path = save_image_status_path + 'status_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(status_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check status area done")

# 游戏中状态栏退出
def status_area_exit(threadshold=0.8,timeout=-1):
    time.sleep(0.5)
    print("status area exit....")
    exit_button_path = save_image_status_path + 'exit_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(exit_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("status area exit done")

# 游戏中状态栏内部退出
def status_inner_exit(threadshold=0.8,timeout=-1):
    print("status area inner exit....")
    inner_exit_button_path = save_image_status_path + 'inner_exit_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(inner_exit_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("status area inner exit done")

#################################状态栏控件区域#################################


#################################礼物box#################################
# 礼物获取按钮确认
def check_get_gift_button(threadshold=0.8,timeout=-1):
    print("check get gift button....")
    get_gift_button_path = save_image_status_path + 'get_gift_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(get_gift_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check get gift button done")

# 礼物盒确认
def check_gift_box(threadshold=0.8,timeout=-1):
    print("check gift box....")
    gift_box_path = save_image_status_path + 'gift_box.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(gift_box_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check gift box done")

#################################礼物box#################################


#################################装备区域#################################
# 游戏中装备区域选择
def check_weapon_area(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check weapon area....")
    weapon_button_path = save_image_status_path + 'weapon_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(weapon_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check weapon area done")

# 游戏中装备栏中装备选择
def weapon_select(selected_num=2,timeout=-1):
    check_if_loading()
    print("selected weapon area....")
    weapon_button_path = save_image_status_path + 'weapon{}.png'.format(selected_num)

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(weapon_button_path, screenshot_path, 0.85)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("selected weapon area done")

# 游戏中装备选择区域内选择
def weapon_select_area_select(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("selected weapon area select....")
    weapon_select_area_path = save_image_status_path + 'weapon_select_area.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_bottom(weapon_select_area_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y + 10)

            time.sleep(1)
            weapon_select_confirm_button_path = save_image_status_path + 'weapon_select_confirm_button.png'

            getscreen(screenshot_path)
            while True:
                x, y = is_in_image_center_point(weapon_select_confirm_button_path, screenshot_path, threadshold)
                if x > 0 and y > 0:
                    tap(x=x, y=y + 10)
                    break
                getscreen(screenshot_path)
            break
        getscreen(screenshot_path)
    print("selected weapon area select done")

#################################装备区域#################################


#################################扭蛋区域#################################
# 抽奖区域内部顶栏的第一个
def check_lottery_head(threadshold=0.8,timeout=-1):
    time.sleep(1)
    check_if_loading()
    print("check lottery area head....")
    lottery_area_head_path = save_image_status_path + 'lottery_area_head.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_bottom(lottery_area_head_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y + 50)
            break
        getscreen(screenshot_path)
    print("check lottery area head done")


# -1500 => 滑到底部
#
# 滑动到抽奖区域某一区域
def lottery_area_scroll_to(threadshold=0.8,timeout=-1,y_bias=-1500):
    time.sleep(1)
    check_if_loading()
    print("scroll to lottery area....")
    lottery_area_head_path = save_image_status_path + 'lottery_area_head.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_bottom(lottery_area_head_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            y += 150
            swipe(x, y,x,y + y_bias)
            break
        getscreen(screenshot_path)
    print("scroll to lottery area done")

# 每日抽奖的按钮点击
def everyday_lottery_button_click(threadshold=0.9,timeout=-1):
    time.sleep(1)
    print("everyday lottery button click....")
    everyday_lottery_click_button_path = save_image_status_path + 'everyday_lottery_click_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(everyday_lottery_click_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            time.sleep(15)

            getscreen_in_character_folder()
            getscreen(screenshot_path)
            break
        getscreen(screenshot_path)
    print("everyday lottery button click done")

# 抽奖每日一抽区域确认
def check_everyday_lottery_area(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check everyday lottery area....")
    everyday_lottery_button_path = save_image_status_path + 'everyday_lottery_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(everyday_lottery_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check everyday lottery done....")

# 常规区域确认
def check_regular_lottery_area(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check regular lottery area....")
    regular_lottery_area_path = save_image_status_path + 'regular_lottery_area.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(regular_lottery_area_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check regular lottery area....")

# 常规区域确认
def check_select_lottery_area(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check select lottery area....")
    select_area_path = save_image_status_path + 'select_area.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(select_area_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check select lottery area....")

# 抽奖区域确认
def check_lottery_area(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check lottery area....")
    lottery_button_path = save_image_status_path + 'lottery_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(lottery_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check lottery area done")

def check_lottery_area_select(lottery_mode="right",threadshold=0.8,timeout=-1):
    time.sleep(2)
    print("ticket lottery button click....")
    lottery_area_select_path = save_image_status_path + 'lottery_area_select.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break

        x,y = -1,-1
        if "right" == lottery_mode:
            x,y = is_in_image_center_point(lottery_area_select_path, screenshot_path, threadshold,x_bias=60,y_bias=-20)
        elif "left" == lottery_mode:
            x,y = is_in_image_center_point(lottery_area_select_path, screenshot_path, threadshold,x_bias=-60,y_bias=-20)

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("ticket lottery button click done")
# 活动票据抽奖按钮点击
def ticket_lottery_button_click(threadshold=0.9,lottery_mode=10,timeout=100):
    time.sleep(1)
    print("ticket lottery button click....")
    ticket_click_button_10_path = save_image_status_path + 'ticket_click_button_10.png'
    ticket_click_button_1_path = save_image_status_path + 'ticket_click_button_1.png'
    lottery_click_button_path = save_image_status_path + 'lottery_click_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break

        x,y = -1,-1
        if 10 == lottery_mode:
            x,y = is_in_image_center_right(ticket_click_button_10_path, screenshot_path, threadshold,x_bias=-20)
        elif 1 == lottery_mode:
            x1,y1 = is_in_image_center_point(ticket_click_button_1_path, screenshot_path, threadshold,x_bias=20)
            x2,y2 = is_in_image_center_point(lottery_click_button_path, screenshot_path, threadshold, x_bias=20)

            if x1 > 0 and y1 > 0: x,y = x1,y1
            if x2 > 0 and y2 > 0: x,y = x2,y2

        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("ticket lottery button click done")

# 活动票据抽奖按钮点击times次
def ticket_lottery_button_click_with_times(lottery_mode=10, times=1, timeout=100):
    while times > 0:
        ticket_lottery_button_click(lottery_mode=lottery_mode,timeout=timeout)
        check_shide_button(timeout=2)
        time.sleep(20)

        getscreen_in_character_folder()
        check_event_info(timeout=2)
        times -= 1

# 活动票据抽奖
def check_ticket_lottery(threadshold=0.8,timeout=-1):
    time.sleep(0.5)
    print("check lottery ticket....")
    lottery_ticket_button_path = save_image_status_path + 'lottery_ticket_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(lottery_ticket_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check lottery ticket done")

#################################扭蛋区域#################################

#################################设置区域#################################

# 设置区域确认
def check_setting_area(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check setting area....")
    setting_button_path = save_image_status_path + 'setting_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(setting_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check setting area done")

# 设置区域的继承密钥区域确认
def check_setting_secret(threadshold=0.8,timeout=-1):
    check_if_loading()
    print("check setting secret....")
    setting_secret_button_path = save_image_status_path + 'setting_secret_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(setting_secret_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check setting secret done")

# 继承密钥发送按钮
def check_setting_secret_sending(threadshold=0.9,timeout=-1):
    print("check setting secret sending....")
    setting_secret_sending_button_path = save_image_status_path + 'setting_secret_sending_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_point(setting_secret_sending_button_path, screenshot_path, threadshold)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("check setting secret sending done")

#################################设置区域#################################

#################################设置区域的额外事件#################################

def switch_app_to_save(timeout=-1):
    print("switch app to save....")
    switch_to_save_button_path = save_image_status_path + 'switch_to_save_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_bottom_right_top(switch_to_save_button_path, screenshot_path, 0.85,x_bias=-10)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("switch app to save done")
    time.sleep(1)

def switch_app_all_in_click(timeout=-1):
    print("switch app all in click....")
    all_in_button_path = save_image_status_path + 'all_in_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_right(all_in_button_path, screenshot_path, 0.85,x_bias=-10)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("switch app all in click done")

def switch_app_copy_click(timeout=-1):
    print("switch app copy click....")
    copy_button_path = save_image_status_path + 'copy_button.png'

    getscreen(screenshot_path)
    start_time = time.time()
    while True:
        if -1 != timeout and time.time() - start_time >= timeout: break
        x, y = is_in_image_center_left(copy_button_path, screenshot_path, 0.85,x_bias=10)
        if x > 0 and y > 0:
            tap(x=x, y=y)
            break
        getscreen(screenshot_path)
    print("switch app copy click done")

#################################设置区域的额外事件#################################
