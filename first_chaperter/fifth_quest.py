import time

from game_event.battle_event import check_if_battling
from game_event.normal_event import check_dialog, check_unique_button, check_zhidao_button, move_forward, \
    check_return_city, check_if_in_city, check_if_loading
from game_event.quest_window import check_if_quest_entering, check_quest_end_button
from game_process import city_info_clean
from tools.adb_event import getscreen, tap
from tools.image_tackle import is_in_image_center_point
from utils import save_image_monster_path, screenshot_path, save_image_battle_path


def monster_select_4(threadshold=0.6):
    monster_area_path = save_image_monster_path + '4.png'
    monster_area1_path = save_image_monster_path + '4_r1.png'
    monster_area2_path = save_image_monster_path + '4_r2.png'

    getscreen(screenshot_path)
    x1, y1 = is_in_image_center_point(monster_area_path, screenshot_path, threadshold)
    x2, y2 = is_in_image_center_point(monster_area1_path, screenshot_path, threadshold)
    x3, y3 = is_in_image_center_point(monster_area2_path, screenshot_path, threadshold)
    x,y = -1,-1

    if x1 > 0 and y1 > 1: x,y = x1,y1
    elif x2 > 0 and y2 > 1: x,y = x2,y2
    elif x3 > 0 and y3 > 1: x,y = x3,y3
    if x > 0 and y > 0: tap(x=x, y=y)

def weapon_selected_2(threadshold=0.7):
    weapon2_path = save_image_battle_path + 'weapon2_button.png'
    weapon2_r1_path = save_image_battle_path + 'weapon2_r1_button.png'
    weapon2_r2_path = save_image_battle_path + 'weapon2_r2_button.png'

    getscreen(screenshot_path)
    x1, y1 = is_in_image_center_point(weapon2_path, screenshot_path, threadshold)
    x2, y2 = is_in_image_center_point(weapon2_r1_path, screenshot_path, threadshold)
    x3, y3 = is_in_image_center_point(weapon2_r2_path, screenshot_path, threadshold)
    x,y = -1,-1

    if x1 > 0 and y1 > 0: x,y = x1,y1
    elif x2 > 0 and y2 > 0: x,y = x2,y2
    elif x3 > 0 and y3 > 0: x,y = x3,y3

    if x > 0 and y > 0: tap(x=x,y=y)

def process(time_wait=2):
    print("first chaperter - fifth quest start.....")
    check_if_quest_entering()
    check_dialog()

    time.sleep(time_wait)
    check_unique_button()

    time.sleep(time_wait)
    check_zhidao_button()

    time.sleep(time_wait)
    move_forward(-100,100)

    time.sleep(time_wait)
    move_forward(-100,100)
    time.sleep(1)
    move_forward(-100,0)
    time.sleep(1)
    move_forward(-100,0)
    time.sleep(1)
    move_forward(-100,0)
    time.sleep(1)
    move_forward(-100,0)

    while False == check_if_battling(): monster_select_4()

    times = 60
    weapon_select_time = 40
    while times > 0:
        if check_if_battling(): times += 0.4
        else: times -= 0.2
        times -= 1
        if weapon_select_time:
            weapon_selected_2()
            weapon_select_time -= 1

    time.sleep(time_wait)
    check_dialog()

    time.sleep(time_wait)
    check_return_city(timeout=3)

    time.sleep(5)
    check_quest_end_button(timeout=20)
    time.sleep(5)
    print("first chaperter - fifth quest start end")
    check_if_in_city()
    check_if_loading()
    city_info_clean()
