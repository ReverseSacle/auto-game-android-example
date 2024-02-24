import time

from game_event.battle_event import check_if_battling
from game_event.normal_event import check_dialog, move_forward, check_return_city, check_if_in_city, \
    check_info, check_if_loading
from game_event.quest_window import check_if_quest_entering, check_quest_end_button
from game_process import city_info_clean
from tools.adb_event import getscreen, tap
from tools.image_tackle import is_in_image_center_point, is_in_image_center_bottom
from utils import save_image_monster_path, screenshot_path

def monster_pointer_select(threadshold=0.5):
    print("monster pointer select.....")
    select_pointer_path = save_image_monster_path + 'select_pointer.png'
    select_pointer1_path = save_image_monster_path + 'select_pointer_r1.png'

    getscreen(screenshot_path)
    x1, y1 = is_in_image_center_point(select_pointer_path, screenshot_path, threadshold)
    x2,y2 = is_in_image_center_bottom(select_pointer1_path, screenshot_path, threadshold)
    if x1 > 0 and y1 > 0: tap(x=x1, y=y1)
    if x2 > 0 and y2 > 0: tap(x=x2,y=y2)

def monster_select_2():
    print("monster select.....")
    monster_area_path = save_image_monster_path + '2.png'
    monster_area1_path = save_image_monster_path + '2_r1.png'
    monster_area2_path = save_image_monster_path + '2_r2.png'
    monster_area3_path = save_image_monster_path + '2_r3.png'

    getscreen(screenshot_path)
    x1, y1 = is_in_image_center_point(monster_area_path, screenshot_path, 0.6)
    x2, y2 = is_in_image_center_point(monster_area1_path, screenshot_path, 0.6)
    x3, y3 = is_in_image_center_point(monster_area2_path, screenshot_path, 0.6)
    x4, y4 = is_in_image_center_point(monster_area3_path, screenshot_path, 0.6)
    x, y = -1, -1
    if x1 > 0 and y1 > 0: x, y = x1, y1
    elif x2 > 0 and y2 > 0: x, y = x2, y2
    elif x3 > 0 and y3 > 0: x, y = x3, y3
    elif x4 > 0 and y4 > 0: x, y = x4, y4

    if x > 0 and y > 0: tap(x=x + 20, y=y)

def process(time_wait=2):
    print("first chaperter - first quest start.....")
    check_if_quest_entering()
    check_dialog()

    time.sleep(time_wait)
    move_forward(30,-230)

    time.sleep(time_wait)
    move_forward(100, -50)

    while False == check_if_battling(): continue

    times = 60
    while times > 0:
        if check_if_battling(): times += 0.4
        else: times -= 0.2
        times -= 1
        monster_pointer_select()


    time.sleep(time_wait)
    check_dialog()

    time.sleep(time_wait)
    check_return_city(timeout=3)

    time.sleep(5)
    check_quest_end_button(timeout=3)
    time.sleep(5)
    print("first chaperter - first quest end")
    check_if_in_city()
    check_if_loading()
    city_info_clean()
