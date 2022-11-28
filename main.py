from utils import Utils
from colors import Colors
import data
from player import Player

import random

def main():

	utils = Utils()
	color = Colors()
	player = Player()

	scaleFactor = 0.05

	img = utils.open_image("assets/scream.webp", scaleFactor)

	rows,cols = utils.return_rows_cols(img)

	player.play(img, rows, cols, 0.1, 0.2)

if __name__ == '__main__':

	main()

