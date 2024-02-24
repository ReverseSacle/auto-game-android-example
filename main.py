from game_process import game_clen_data_process
from multiply_game_process import new_game_character_event_process, collecting_for_lottery, game_save_and_lottery
from tools.adb_event import connect
from utils import deviceName
if __name__ == '__main__':
    connect(deviceName)

    # game_clen_data_process()

    new_game_character_event_process()
    collecting_for_lottery()
    game_save_and_lottery()


