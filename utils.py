import datetime
import os
import pyperclip

from tools.adb_event import getscreen

## 设备信息
# 设备名，安卓手机可以随意填写  String
# deviceName = 'emulator-5554'
deviceName = '127.0.0.1:5555'
# app包名
appPackage = 'jp.MarvelousAQL.logres'
# 启动Activity名称  String
appActivity = 'com.aiming.lfs.LFSActivity'
resolution_x,resolution_y = 540,960

## 图片路径
save_image_path = 'D:/Rever/Downloads/jyumofa/'

save_image_button_path = save_image_path + 'button/'
save_image_start_page_path = save_image_path + 'start_page/'
save_image_monster_path = save_image_path + 'monster/'
save_image_battle_path = save_image_path + 'battle/'
save_image_status_path = save_image_path + 'status/'
save_image_figure_path = save_image_path + 'figure/'
save_image_quest_path = save_image_path + 'quest_window/'
## 角色生成路径
save_image_characters_path = save_image_path + 'characters/'
cur_len = 0
folders = None
max_id = None
character_id = cur_len + 1
character_folder = ''
character_name = ''

## 指定刷新图片path
screenshot_path = save_image_path + 'screenshot.png'
errorshot_path = save_image_path + 'errorshot.png'

def get_cur_time_folder():
    now = datetime.datetime.now()
    return "{}_{}_{}".format(now.year,now.month,now.day)

def get_cur_time_file():
    now = datetime.datetime.now()
    return "{}_{}_{}".format(now.hour,now.minute,now.second)

def create_character_folder():
    print("create character folder......")
    global folders,max_id,cur_len,character_id
    folders = [name for name in os.listdir(save_image_characters_path) if os.path.isdir(os.path.join(save_image_characters_path, name))]
    max_id = max(folders, key=lambda x: int(x))
    if folders: cur_len = int(max_id)

    character_id = cur_len + 1
    new_path = "{}{}/".format(save_image_characters_path,character_id)

    global character_folder

    character_folder = new_path
    if os.path.exists(new_path): return

    os.mkdir(new_path)


def create_character_data():
    character_data = pyperclip.paste().replace('\r','')

    file_path = '{}{}_data_{}.txt'.format(character_folder,character_id,get_cur_time_file())
    with open(file_path,"w") as file:
        file.write(character_data)

    print("create character folder done")

def getscreen_in_character_folder():
    print("getscreen in character folder...")
    getscreen('{}/{}.png'.format(character_folder, get_cur_time_file()))
