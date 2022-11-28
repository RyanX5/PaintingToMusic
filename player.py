import musicalbeeps
import random
from colors import Colors
from utils import Utils
import data

class Player:

	

	def __init__(self):

		pass

	def play_note(self, note, duration):

		player = musicalbeeps.Player(volume = 0.5, mute_output = False)

		player.play_note(note, duration)

	def play(self, img, rows, cols, randMin = 0.05, randMax = 0.15, octave_shift = -1):

		color = Colors()
		utils = Utils()

		for i in range(rows):
			for j in range(cols):
				pixel = img[i, j]
				pixel = utils.BGR_to_RGB(pixel)
				pixel = utils.make_array(pixel[0], pixel[1], pixel[2])/255.0

				noteList = self.shift_octave(data.notes, octave_shift)


				note = color.preferred_note(pixel, noteList)

				duration = round(random.uniform(randMin, randMax), 2)

				self.play_note(note, duration)

	def shift_octave(self, notesList, value = 0):

		numbers = "0123456789"

		shifted_notesList = []

		for note in notesList:

			if note[-1] not in numbers:

				new_note = note[0] + str(int(note[1]) + value) + note[2]

				shifted_notesList.append(new_note)

			elif note[-1] in numbers:

				new_note = note[0] + str(int(note[1]) + value)

				shifted_notesList.append(new_note)

		return shifted_notesList


