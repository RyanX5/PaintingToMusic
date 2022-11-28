import cv2
import numpy

class Utils:

	def __init__(self):

		pass


	def open_image(self, img_dst = "assets/scream.webp", factor = 0.05):

		img = cv2.imread(img_dst, -1)

		img = self.process_image(img, factor)

		return img


	def process_image(self, img, factor):

		img = cv2.resize(img, (0, 0), fx=factor, fy=factor)

		return img


	def return_pixel_count(self, img):

		rows,cols,_ = img.shape

		return rows*cols

	def return_rows_cols(self, img):

		rows,cols,_ = img.shape

		return rows,cols

	def make_array(self, r, g, b):

		arr = numpy.array([r, g, b])

		return arr

	def BGR_to_RGB(self, bgr):

		rgb = [bgr[2], bgr[1], bgr[0]]

		return rgb




