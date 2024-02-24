import time
import random

from game_event.normal_event import check_dialog, move_forward, check_if_in_city, check_info, check_confirm_button, \
    check_done_button, check_shide_button, check_bushi_button, check_event_info, check_return_city, \
    check_if_loading
from game_event.quest_window import check_if_quest_entering, check_quest_end_button
from game_process import city_info_clean
from tools.adb_event import tap, getscreen, input_text
from tools.image_tackle import is_in_image_center_top, is_in_image_center_point
from utils import screenshot_path, save_image_figure_path

def generate_gbk2312_chinese():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    return bytes.fromhex(val).decode('gb2312')

def check_dialog_obj():
    main_figure_path = save_image_figure_path + '1.png'

    getscreen(screenshot_path)
    while True:
        x, y = is_in_image_center_point(main_figure_path, screenshot_path, 0.8)
        if x > 0 and y > 0:
            tap(x=x, y=y + 10)
            break
        getscreen(screenshot_path)

def check_main_character():
    main_figure_path = save_image_figure_path + 'main.png'
    getscreen(screenshot_path)
    while True:
        x, y = is_in_image_center_top(main_figure_path, screenshot_path, 0.8)
        if x > 0 and y > 0:
            tap(x=x, y=y + 10)
            break
        getscreen(screenshot_path)

def process(time_wait=2):
    forbid_name = ['妾']
    print("first chaperter - third quest start.....")
    check_if_quest_entering()
    check_dialog()

    time.sleep(time_wait)
    move_forward(x_bias=-130,y_bias=-130)

    time.sleep(time_wait)
    check_dialog_obj()

    time.sleep(time_wait)
    check_main_character()

    # 名字选择
    time.sleep(time_wait)
    name = '小小{}'.format(generate_gbk2312_chinese()).replace(' ','')

    while name in forbid_name:
        name = '小小{}'.format(generate_gbk2312_chinese()).replace(' ', '')

    time.sleep(time_wait)
    input_text(name)

    time.sleep(time_wait)
    check_done_button()

    time.sleep(time_wait)
    check_confirm_button()

    time.sleep(time_wait)
    check_shide_button()

    time.sleep(time_wait)
    check_dialog_obj()

    time.sleep(time_wait)
    check_dialog(timeout=5)

    time.sleep(time_wait)
    check_return_city(timeout=3)

    time.sleep(5)
    check_quest_end_button(timeout=3)
    time.sleep(5)
    print("first chaperter - third quest end")
    check_if_in_city()
    check_if_loading()
    city_info_clean()
    check_bushi_button(timeout=3)
    city_info_clean()
    check_bushi_button(timeout=3)
    city_info_clean()

