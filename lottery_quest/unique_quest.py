import time

from game_event.normal_event import check_dialog, move_forward, check_return_city, check_if_in_city
from game_event.quest_window import check_if_quest_entering, check_quest_end_button


def process(time_wait=2):
    print("unique quest start.....")
    check_if_quest_entering()
    check_dialog()

    time.sleep(time_wait)
    times = 4
    while times:
        move_forward(150, -150)
        time.sleep(1)
        times -= 1

    time.sleep(time_wait)
    move_forward(130,-100)

    check_dialog()

    time.sleep(time_wait)
    check_return_city(timeout=2)

    time.sleep(10)
    check_quest_end_button(timeout=3)
    time.sleep(5)
    print("unique quest end")
    check_if_in_city()
