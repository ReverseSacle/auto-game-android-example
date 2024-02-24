from tools.image_tackle import is_in_image_center_point, is_in_image_original
from tools.adb_event import getscreen,tap
from utils import save_image_battle_path,screenshot_path

def check_if_battling(threadshold=0.75):
    print("check if battling....")
    select_pointer_path = save_image_battle_path + 'battle_start.png'

    getscreen(screenshot_path)
    x = is_in_image_original(select_pointer_path, screenshot_path)
    if x >= threadshold: return True
    return False

