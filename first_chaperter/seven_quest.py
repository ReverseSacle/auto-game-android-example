import time

from game_event.normal_event import check_dialog, check_return_city, check_if_in_city, check_if_loading, move_forward, \
    check_event_info
from game_event.quest_window import check_if_quest_entering, check_quest_end_button
from game_process import city_info_clean, check_gift_box_process


def process(time_wait=2):
    print("first chaperter - seven quest start.....")
    check_if_quest_entering()
    check_dialog()

    time.sleep(time_wait)
    move_forward(130, -110)

    time.sleep(time_wait)
    check_dialog()

    time.sleep(time_wait)
    check_event_info(timeout=3)

    time.sleep(time_wait)
    check_return_city(timeout=3)

    time.sleep(5)
    check_quest_end_button(timeout=5)
    time.sleep(5)
    print("first chaperter - seven quest start end")
    check_if_in_city()
    check_if_loading()
    city_info_clean()

    time.sleep(time_wait)
    check_gift_box_process()