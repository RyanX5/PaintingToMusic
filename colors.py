import numpy

from utils import Utils
import data



class Colors:


	def __init__(self):

		pass

	def color_distance(self, color1, color2):

		rm = 0.5*(color1[0] + color2[0])

		distance = sum((2+rm,4,3-rm)*(color1-color2)**2)**0.5

		return distance


	def preferred_note(self, color, comparedNotes):

		distanceF4 = self.color_distance(color, data.F4)
		distanceGb4 = self.color_distance(color, data.Gb4)
		distanceG4 = self.color_distance(color, data.G4)
		distanceAb4 = self.color_distance(color, data.Ab4)
		distanceA4 = self.color_distance(color, data.A4)
		distanceBb4 = self.color_distance(color, data.Bb4)
		distanceB4 = self.color_distance(color, data.B4)
		distanceC5 = self.color_distance(color, data.C5)
		distanceDb5 = self.color_distance(color, data.Db5)
		distanceD5 = self.color_distance(color, data.D5)
		distanceE5 = self.color_distance(color, data.E5)
		distanceEb5 = self.color_distance(color, data.Eb5)
		distanceF5 = self.color_distance(color, data.F5)

		li = [distanceF4, distanceGb4, distanceG4, distanceAb4, distanceA4, distanceBb4, distanceB4, distanceC5, distanceDb5, distanceD5, distanceE5, distanceEb5, distanceF5]
		minimumDistance = min(li)

		notes = comparedNotes

		return notes[li.index(minimumDistance)]
		






