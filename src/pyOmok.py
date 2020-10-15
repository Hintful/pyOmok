MAX_BOARD_SIZE = 15

def num_to_ascii(num):
	if(num == 1):
		pass

class Omok:
	# attributes
	board = []

	def __init__(self):
		for i in range(MAX_BOARD_SIZE):
			row = []
			for j in range(MAX_BOARD_SIZE):
				row.append(-1)
			self.board.append(row)

	def print_board(self):
		for i in range(MAX_BOARD_SIZE):
			print("")
			for j in range(MAX_BOARD_SIZE):
				if(self.board[i][j] == -1):
					print("Ｘ", end='')
				elif(self.board[i][j] == 0):
					print("●", end='')
				elif(self.board[i][j] == 1):
					print("○", end='')
				else:
					print("Ｘ", end='')
			print("")

# ----------------------------------------------------

def main():
	omok = Omok()
	omok.print_board()

if __name__ == "__main__":
	main()
