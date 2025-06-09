import random
import time

board = ["-","-","-",
		 "-","-","-",
		 "-","-","-"]
user_symbol = 'O'
computer_symbol = 'X'
winner = None
def printBoard(board):
		print(board[0] + "|" + board[1] + "|" + board[2])
		print(board[3] + "|" + board[4] + "|" + board[5])
		print(board[6] + "|" + board[7] + "|" + board[8])


def player_move(board):
	trackplayerinput = []
	player_input = int(input('Enter a number 1-9: '))
	index = player_input - 1
	if 0 <= index < 9 and board[index] == "-":
		board[index] = user_symbol
	else:
		print('This spot is already taken! Try again')

def computer_move(board):
		while True:
			computer_input = random.randint(0, 8)
			if board[computer_input] == "-":
				board[computer_input] = computer_symbol
				break


def checkhorizontal(board):
	global winner
	if board[0] == board[1] == board[2] and board[0] != "-":
		winner = board[0]
		return True
	elif board[3] == board[4] == board[5] and board[3] != "-":
		winner = board[3]
		return True
	elif board[6] == board[7] == board[8] and board[6] != "-":
		winner = board[6]
		return True

def checkrows(board):
	global winner
	if board[0] == board[3] == board[6] and board[0] != "-":
		winner = board[0]
		return True
	elif board[1] == board[4] == board[7] and board[1] != "-":
		winner = board[1]
		return True
	elif board[2] == board[5] == board[8] and board[2] != "-":
		winner = board[2]
		return True

def checkdiagonal(board):
	global winner
	if board[0] == board[4] == board[8] and board[0] != "-":
		winner = board[0]
		return True
	elif board[2] == board[4] == board[6] and board[2] != "-":
		winner = board[2]
		return True

def checktie(board):
	global gamerunning
	if "-" not in board:
		print("It's a tie!")
		gamerunning = False

def check_win(board):
	global gamerunning
	if checkrows(board) or checkdiagonal(board) or checkhorizontal(board):
		print(f"The winner is:{winner}")
		gamerunning = False

gamerunning = True
while gamerunning:
	player_move(board)
	printBoard(board)
	check_win(board)
	checktie(board)

	print("Now is computer's turn!")
	time.sleep(2)
	computer_move(board)
	printBoard(board)
	check_win(board)
	checktie(board)
