import time

from game_event.normal_event import check_dialog, move_forward, chek_dialog_skip_button, check_unique_button, \
    check_zhidao_button, check_if_loading, check_return_city, check_if_in_city, check_info
from game_event.quest_window import check_if_quest_entering, check_quest_end_button


def process(time_wait=2):
    print("gudai quest start.....")
    time.sleep(time_wait)
    check_if_quest_entering()
    check_dialog()

    time.sleep(time_wait)
    move_forward(-200,-200)
    time.sleep(1)
    move_forward(-200,-200)
    time.sleep(1)
    move_forward(-100,-100)
    time.sleep(1)
    move_forward(-150,-100)
    time.sleep(1)
    move_forward(-80,-20)

    time.sleep(time_wait)
    chek_dialog_skip_button()

    time.sleep(time_wait)
    move_forward(0,50)

    time.sleep(time_wait)
    check_if_loading()
    times = 12
    while times:
        move_forward(150, -100)
        time.sleep(1)
        times -= 1

    time.sleep(time_wait)
    move_forward(0,-60)

    time.sleep(time_wait)
    chek_dialog_skip_button()

    time.sleep(1)
    check_unique_button(timeout=2)
    time.sleep(1)
    check_unique_button(timeout=2)
    time.sleep(1)
    check_unique_button(timeout=2)
    time.sleep(1)
    check_unique_button(timeout=2)
    time.sleep(1)
    check_unique_button(timeout=2)

    time.sleep(time_wait)
    check_zhidao_button()

    time.sleep(time_wait)
    check_return_city(timeout=2)

    time.sleep(10)
    check_quest_end_button(timeout=3)
    time.sleep(5)
    print("gudai quest end")
    check_if_in_city()
    check_if_loading()
    check_info(timeout=2)




