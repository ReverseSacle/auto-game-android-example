import time

from game_process import game_new_start_process, game_normal_start_process, city_info_clean, check_gift_box_process, \
    check_everyday_lottery_process, weapon_select_event, quest_select_new, quest_select, \
    check_event_ticket_lottery_process, save_game_character_data, game_clen_data_process, \
    making_quest_process, unique_quest_process, check_regular_ticket_lottery_process, \
    check_select_lottery_process, gudai_quest_process
from first_chaperter import enter_quest as fcp_enter,first_quest as fcp_first,second_quest as fcp_second,\
    third_quest as fcp_third, fourth_quest as fcp_fourth,fifth_quest as fcp_fifth, six_quest as fcp_six, \
    seven_quest as fcp_seven

from utils import create_character_folder, create_character_data


def new_game_character_event_process(time_wait=2):
    # game_new_start_process()

    # # 游戏开始的任务
    # time.sleep(time_wait)
    # fcp_enter.process()
    #
    # # 游戏主线的装备替换
    # time.sleep(time_wait)
    # weapon_select_event()
    #
    # # 游戏主线的第一章第一个任务
    # time.sleep(time_wait)
    # quest_select_new()
    #
    # time.sleep(time_wait)
    # fcp_first.process()
    #
    # # 游戏主线的第一章第二个任务
    # time.sleep(time_wait)
    # quest_select()
    #
    # time.sleep(time_wait)
    # fcp_second.process()

    # # 游戏主线的第一章第三个任务
    # time.sleep(time_wait)
    # quest_select()

    # time.sleep(time_wait)
    # fcp_third.process()

    # 游戏主线的第一章第四个任务
    time.sleep(time_wait)
    quest_select()

    time.sleep(time_wait)
    fcp_fourth.process()

    # 游戏主线的第一章第五个任务
    time.sleep(time_wait)
    quest_select()

    time.sleep(time_wait)
    fcp_fifth.process()

    # 游戏主线的第一章第六个任务
    time.sleep(time_wait)
    quest_select()

    time.sleep(time_wait)
    fcp_six.process()

    # 游戏主线的第一章第七个任务
    time.sleep(time_wait)
    quest_select()

    time.sleep(time_wait)
    fcp_seven.process()

def collecting_for_lottery(time_wait=2):
    making_quest_process()

    # time.sleep(time_wait)
    # gudai_quest_process()

    time.sleep(time_wait)
    unique_quest_process()


def game_save_and_lottery(time_wait=2):
    ###############################角色数据保存###############################
    time.sleep(time_wait)
    create_character_folder()

    time.sleep(time_wait)
    save_game_character_data()

    time.sleep(time_wait)
    create_character_data()
    ###############################角色数据保存###############################


    ###############################开始抽奖################################
    time.sleep(time_wait)
    check_gift_box_process()

    # time.sleep(time_wait)
    # check_everyday_lottery_process()

    time.sleep(time_wait)
    check_event_ticket_lottery_process(lottery_mode=10,lottery_times=2)

    time.sleep(time_wait)
    check_event_ticket_lottery_process(lottery_mode=1,lottery_times=2)

    time.sleep(time_wait)
    check_regular_ticket_lottery_process()

    time.sleep(time_wait)
    check_select_lottery_process()
    ###############################开始抽奖################################

    time.sleep(time_wait)
    game_clen_data_process()


def normal_game_character_event_process(time_wait=2):
    game_normal_start_process()

    time.sleep(time_wait)
    city_info_clean()

    time.sleep(time_wait)
    check_gift_box_process()

    time.sleep(time_wait)
    check_everyday_lottery_process()
