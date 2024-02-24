import time
import utils
from game_event.game_start_event import check_start_page, waiting_for_pre_downloading_area, check_if_pre_download, \
    check_if_download_end, check_if_extra_download, check_area_select, check_constraint, check_gender

from game_event.normal_event import move_forward, check_event_info, check_info, check_if_loading, check_bushi_button, \
    check_confirm_button
from game_event.quest_window import check_quest_window, check_quest_first_area, get_first_quest, \
    check_quest_chufa_button, check_quest_mode_button, check_quest_exit_button, check_quest_event_select_button
from game_event.status import check_status_area, check_gift_box, status_inner_exit, \
    status_area_exit, check_get_gift_button, check_lottery_head, everyday_lottery_button_click, \
    check_ticket_lottery, ticket_lottery_button_click_with_times, lottery_area_scroll_to, check_setting_area, \
    check_setting_secret, check_setting_secret_sending, switch_app_to_save, switch_app_all_in_click, \
    switch_app_copy_click, check_weapon_area, weapon_select, weapon_select_area_select, check_lottery_area, \
    check_everyday_lottery_area, check_regular_lottery_area, check_select_lottery_area, check_lottery_area_select
from lottery_quest import making_quest, gudai_quest, unique_quest
from tools.adb_event import open_game, press, stop_game, clean_game_data, swipe
from utils import getscreen_in_character_folder


################################游戏启动相关################################
# 非全新角色的启动过程
def game_normal_start_process(time_wait=2):
    print("game normal start process....")
    open_game(utils.appPackage, utils.appActivity)
    # check_start_warning()

    time.sleep(time_wait)
    check_start_page()

    time.sleep(time_wait)
    waiting_for_pre_downloading_area()

    time.sleep(time_wait)
    check_if_pre_download(timeout=3)

    time.sleep(time_wait)
    check_if_download_end()

    time.sleep(time_wait)
    check_if_extra_download(timeout=3)
    print("game normal start process done")

# 清空数据后启动的全新角色启动过程
def game_new_start_process(time_wait=2.5):
    print("game new start process....")
    open_game(utils.appPackage, utils.appActivity)
    # check_start_warning()

    time.sleep(time_wait)
    check_start_page()

    time.sleep(time_wait)
    check_area_select()

    time.sleep(time_wait)
    waiting_for_pre_downloading_area()

    time.sleep(time_wait)
    check_if_pre_download()

    time.sleep(300)
    check_if_download_end()

    time.sleep(time_wait)
    check_if_extra_download()

    time.sleep(time_wait)
    check_constraint()

    time.sleep(time_wait)
    check_gender()

    time.sleep(5)
    stop_game(utils.appPackage)

    time.sleep(time_wait)
    game_normal_start_process()
    print("game new start process done")

# 清空游戏数据
def game_clen_data_process():
    stop_game(utils.appPackage)
    clean_game_data(utils.appPackage)

################################游戏启动相关################################


################################游戏中事件的组合################################
# 清理城市消息通知
def city_info_clean():
    check_info(timeout=3)
    check_event_info(timeout=3)

    check_info(timeout=3)
    check_event_info(timeout=3)

    check_info(timeout=3)
    check_event_info(timeout=3)

# 第一章第一次任务的获取
def quest_select_new(time_wait=2):
    print("quest select new....")
    check_if_loading()
    check_quest_window()

    time.sleep(time_wait)
    check_if_loading()
    check_event_info(1.5)

    time.sleep(time_wait)
    check_quest_first_area(timeout=3)

    time.sleep(time_wait)
    get_first_quest()
    print("quest select new done")

# 第一章顶部任务的第四个任务及之前的获取
def quest_select(time_wait=2):
    print("quest select....")
    check_if_loading()
    check_quest_window()

    time.sleep(time_wait)
    check_if_loading()
    check_info(1.5)
    check_event_info(1.5)

    time.sleep(time_wait)
    get_first_quest()
    print("quest select done")


def quest_select_normal(time_wait=2):
    print("quest select normal....")
    check_if_loading()
    check_quest_window()

    time.sleep(time_wait)
    check_if_loading()
    check_info(1.5)
    check_event_info(1.5)

    time.sleep(time_wait)
    print("quest select normal done")

# 查看礼物盒并获取礼物
def check_gift_box_process():
    print("check gift box process...")
    check_status_area()
    check_gift_box(timeout=3)
    check_get_gift_button(timeout=3)
    check_event_info(timeout=3)
    status_inner_exit(timeout=3)
    status_area_exit()
    print("check gift box process done")

# 每日一抽任务
def check_everyday_lottery_process():
    check_status_area()
    check_everyday_lottery_area(timeout=3)
    check_lottery_head(timeout=3)
    everyday_lottery_button_click(timeout=3)
    check_event_info(timeout=3)
    status_inner_exit(timeout=3)
    status_inner_exit(timeout=3)
    status_area_exit()

# 活动票据的抽取
def check_event_ticket_lottery_process(lottery_mode=10,lottery_times=1):
    print("check event ticket lottery process....")
    check_status_area()
    check_lottery_area()
    lottery_area_scroll_to(y_bias=-1500)
    check_ticket_lottery()
    ticket_lottery_button_click_with_times(lottery_mode=lottery_mode,times=lottery_times)
    status_area_exit()
    print("check event ticket lottery process done")


def check_regular_ticket_lottery_process():
    print("check regular ticket lottery process....")
    check_status_area()
    check_lottery_area()
    check_regular_lottery_area()
    ticket_lottery_button_click_with_times(lottery_mode=1,times=6)
    status_area_exit()
    print("check regular ticket lottery process done")

def check_select_lottery_process():
    print("check select lottery process....")
    check_status_area()
    check_lottery_area()
    check_select_lottery_area()
    ticket_lottery_button_click_with_times(lottery_mode=1,times=2)
    status_area_exit()
    print("check select lottery process done")

# 保存用户数据
def save_game_character_data(time_wait=2):
    character_folder = utils.character_folder

    if '' == character_folder: print("game character data not create")
    check_status_area()

    check_if_loading()
    getscreen_in_character_folder()

    time.sleep(time_wait)
    check_setting_area()
    check_setting_secret()

    check_if_loading()
    getscreen_in_character_folder()
    check_setting_secret_sending()

    time.sleep(time_wait)
    switch_app_to_save()

    time.sleep(time_wait)
    press(utils.resolution_x / 2, utils.resolution_y / 2,2000)

    time.sleep(time_wait)
    switch_app_all_in_click()

    time.sleep(time_wait)
    switch_app_copy_click()

    open_game(utils.appPackage, utils.appActivity)

    time.sleep(time_wait)
    status_area_exit()

################################游戏中事件相关################################


################################剧情主线################################
def weapon_select_event(time_wait=2):
    print("weapon select event.......")
    check_if_loading()

    time.sleep(time_wait)
    check_status_area(threadshold=0.75)

    check_if_loading()
    check_weapon_area()

    check_if_loading()
    weapon_select(timeout=4)

    time.sleep(time_wait)
    weapon_select_area_select()

    time.sleep(time_wait)
    check_info(timeout=4)

    time.sleep(time_wait)
    status_area_exit()
    print("weapon select event done")

################################剧情主线################################


################################相关任务################################
def making_quest_process(time_wait=2):
    ######### quest1
    time.sleep(time_wait)
    quest_select_normal()

    time.sleep(time_wait)
    move_forward(0, -30)

    time.sleep(time_wait)
    move_forward(0, -30)

    time.sleep(time_wait)
    check_quest_chufa_button(timeout=3)

    time.sleep(time_wait)
    making_quest.process()
    ######### quest1

    ######## quest2
    # time.sleep(time_wait)
    # quest_select_normal()
    #
    # time.sleep(time_wait)
    # move_forward(0, -30)
    #
    # time.sleep(time_wait)
    # move_forward(0, -50)
    #
    # time.sleep(time_wait)
    # check_quest_chufa_button(timeout=3)
    #
    # time.sleep(time_wait)
    # making_quest.process()
    ######## quest2
    #
    # ######## quest3
    # time.sleep(time_wait)
    # quest_select_normal()
    #
    # time.sleep(time_wait)
    # move_forward(0, -30)
    #
    # time.sleep(time_wait)
    # move_forward(0, -120)
    #
    # time.sleep(time_wait)
    # check_quest_chufa_button(timeout=3)
    #
    # time.sleep(time_wait)
    # making_quest.process()
    # ######### quest3

    # ######### quest4
    # time.sleep(time_wait)
    # quest_select_normal()
    #
    # time.sleep(time_wait)
    # move_forward(0, 80)
    #
    # time.sleep(time_wait)
    # move_forward(0, -260)
    #
    # time.sleep(time_wait)
    # check_quest_chufa_button(timeout=3)
    #
    # time.sleep(time_wait)
    # making_quest.process()
    # ########## quest4

def gudai_quest_process(time_wait=2):
    check_if_loading()
    quest_select_normal()

    time.sleep(time_wait)
    move_forward(0, 80)

    time.sleep(time_wait)
    move_forward(0, -260)

    time.sleep(time_wait)
    check_quest_chufa_button(timeout=3)

    time.sleep(time_wait)
    gudai_quest.process()

def unique_quest_process(time_wait=2):
    time.sleep(time_wait)
    quest_select_normal()

    time.sleep(time_wait)
    check_quest_mode_button()

    time.sleep(time_wait)
    check_quest_exit_button()

    time.sleep(time_wait)
    check_info(timeout=2)

    time.sleep(time_wait)
    check_quest_event_select_button()

    time.sleep(time_wait)
    move_forward(0,-30)

    time.sleep(time_wait)
    move_forward(0, -260)

    time.sleep(time_wait)
    check_quest_chufa_button(timeout=3)

    time.sleep(time_wait)
    unique_quest.process()

def normal_occupation_quest1(time_wait):
    time.sleep(time_wait)
    quest_select_normal()

    time.sleep(time_wait)
    check_quest_mode_button()

    time.sleep(time_wait)
    check_quest_exit_button()

    time.sleep(time_wait)
    check_info(timeout=2)

    time.sleep(time_wait)
    check_quest_event_select_button(quest_mode="left")

    time.sleep(time_wait)
    check_info(timeout=2)

    time.sleep(time_wait)
    swipe(utils.resolution_x / 2, utils.resolution_y / 2, utils.resolution_x / 2, utils.resolution_y / 2 - 130)

    time.sleep(time_wait)
    move_forward(0,0)

    time.sleep(time_wait)
    move_forward(0, -230)

    time.sleep(time_wait)
    check_confirm_button()

    time.sleep(time_wait)
    check_quest_chufa_button(timeout=3)


################################相关任务################################


