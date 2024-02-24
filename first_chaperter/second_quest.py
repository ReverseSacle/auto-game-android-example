import time

from game_event.battle_event import check_if_battling
from game_event.normal_event import check_dialog, check_if_in_city, move_forward, check_return_city, \
    check_if_loading
from game_event.quest_window import check_if_quest_entering, check_quest_end_button
from game_process import city_info_clean
from tools.adb_event import getscreen, tap
from tools.image_tackle import is_in_image_center_bottom, is_in_image_center_point
from utils import save_image_monster_path, screenshot_path, save_image_battle_path


def monster_select_3():
    print("monster select.....")
    monster_area_path = save_image_monster_path + '3.png'
    monster_area1_path = save_image_monster_path + '3_r1.png'
    monster_area2_path = save_image_monster_path + '3_r2.png'
    monster_area3_path = save_image_monster_path + '3_r3.png'

    getscreen(screenshot_path)
    x1, y1 = is_in_image_center_bottom(monster_area_path, screenshot_path, 0.62)
    x2, y2 = is_in_image_center_bottom(monster_area1_path, screenshot_path, 0.62)
    x3, y3 = is_in_image_center_bottom(monster_area2_path, screenshot_path, 0.62)
    x4, y4 = is_in_image_center_bottom(monster_area3_path, screenshot_path, 0.62)
    x,y = -1,-1
    if x1 > 0 and y1 > 0: x,y = x1,y1
    elif x2 > 0 and y2 > 0: x,y = x2,y2
    elif x3 > 0 and y3 > 0: x,y = x3,y3
    elif x4 > 0 and y4 > 0: x,y = x4,y4

    if x > 0 and y > 0: tap(x=x + 30, y=y)

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
    print("first chaperter - second quest start.....")
    check_if_quest_entering()
    check_dialog()

    time.sleep(time_wait)
    move_time = 7
    while move_time:
        move_forward(200,-160)
        time.sleep(1)
        move_time -= 1
    # move_forward(120, -120)

    while False == check_if_battling(): continue

    times = 60
    monster_select_time = 15
    weapon_select_time = 40
    while times > 0:
        if check_if_battling(): times += 0.4
        else: times -= 0.2
        times -= 1
        if monster_select_time:
            monster_select_3()
            monster_select_time -= 1
        if weapon_select_time:
            weapon_selected_2()
            weapon_select_time -= 1

    time.sleep(time_wait)
    check_dialog()
    check_return_city(timeout=3)

    time.sleep(5)
    check_quest_end_button(timeout=3)
    time.sleep(5)
    print("first chaperter - second quest end")
    check_if_in_city()
    check_if_loading()
    city_info_clean()

