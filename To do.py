'''
def set_device_mode(mode):
    allowed_modes = ['user', 'admin', 'guest']
    if mode not in allowed_modes:
        raise ValueError(f"Invalid mode: {mode}")
    return f"Mode set to {mode}"


def apply_palette_setting(palette, brightness, contrast):
	allowed_palettes = ['HotBlack', 'CoolWhite']

	if palette not in allowed_palettes:
		raise ValueError("Unsupported palette.")
	if not (0 <= brightness <= 100):
		raise ValueError("Brightness must be 0-100.")
	if not (0 <= contrast <= 100):
		raise ValueError("Contrast must be 0-100.")

	return {
		"palette": palette,
		"brightness": brightness,
		"contrast": contrast
	}

def reboot_and_restore(mode):
    if mode not in ["factory", "user"]:
        raise ValueError("Mode must be 'factory' or 'user'.")

    if mode == "factory":
        return {"palette": "HotBlack", "brightness": 70, "contrast": 50}
    else:
        return {"palette": "CoolWhite", "brightness": 40, "contrast": 40}

def set_amplification_level(level):
    valid_levels = ["Normal", "High", "Extreme"]
    if level not in valid_levels:
        raise ValueError("Invalid amplification level.")
    return f"Amplification set to {level}"

def configure_device(palette, brightness, contrast, amp_level):
    apply_palette_setting(palette, brightness, contrast)
    set_amplification_level(amp_level)
    return "Configuration complete"




userinput = input('Enter your word: ')
dic = {}

for n in userinput:
	if n not in dic.keys():
		dic[n] = 1
	else:
		dic[n] = dic[n] + 1

print(dic)
'''

import random
import time

board = ["-","-","-",
		 "-","-","-",
		 "-","-","-"]

winner = None
gamerunning = True

def printBoard (board):
	print (board[0] + '|' + board[1] + '|' + board[2])
	print(board[3] + '|' + board[4] + '|' + board[5])
	print(board[6] + '|' + board[7] + '|' + board[8])

def player_move(board):
	player_symbol = 'O'
	player_input = int(input('Enter a number from 1 to 9: '))
	index = player_input - 1
	if 0 <= index < 9 and board[index] == "-":
		board[index] = player_symbol
	else:
		print('This place has been taken!')

def computer_move(board):
	computer_symbol = 'X'
	computer_input = random.randint(0,8)
	print("Now it's computers turn...")
	time.sleep(3)
	if board[computer_input] == "-":
		board[computer_input] = computer_symbol

def checkrow(board):
	global winner
	if board[0] == board[1] == board[2] and board != "-"
		winner = board[0]
		return True





while gamerunning:
	player_move(board)
	printBoard(board)
	computer_move(board)
	printBoard(board)