import time

from game_event.normal_event import move_forward, chek_dialog_skip_button, check_unique_button, \
    check_zhidao_button, check_if_in_city, check_return_city
from game_event.quest_window import check_if_quest_entering, check_quest_end_button


def process(time_wait=2):
    print("making quest start.....")
    check_if_quest_entering()

    time.sleep(time_wait)
    move_forward(60, -240)

    time.sleep(time_wait)
    move_forward(-100, -240)

    time.sleep(time_wait)
    move_forward(-120, -30)

    time.sleep(time_wait)
    chek_dialog_skip_button()

    time.sleep(time_wait)
    move_forward(0,50)

    time.sleep(time_wait)
    check_unique_button(timeout=2)

    time.sleep(time_wait)
    check_zhidao_button()

    time.sleep(time_wait)
    check_return_city(timeout=5)

    time.sleep(10)
    check_quest_end_button(timeout=3)
    time.sleep(5)
    print("making quest end")
    check_if_in_city()