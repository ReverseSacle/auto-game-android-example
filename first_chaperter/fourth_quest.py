import time
from game_event.normal_event import check_dialog, move_forward, check_if_in_city, check_info, check_return_city, \
    check_if_loading, check_bushi_button
from game_event.quest_window import check_if_quest_entering, check_quest_end_button
from game_process import city_info_clean


def process(time_wait=2):
    print("fourth chaperter - fourth quest start.....")
    check_if_quest_entering()
    check_if_loading()

    time.sleep(time_wait)
    move_forward(-100,-100)
    time.sleep(1)
    move_forward(-160,-100)
    time.sleep(1)
    move_forward(-210,-100)
    time.sleep(1)
    move_forward(-260,-100)

    time.sleep(time_wait)
    check_dialog()

    time.sleep(time_wait)
    check_return_city(timeout=3)

    time.sleep(5)
    check_quest_end_button(timeout=3)
    time.sleep(5)
    print("first chaperter - fourth quest end")
    check_if_in_city()
    check_if_loading()
    city_info_clean()