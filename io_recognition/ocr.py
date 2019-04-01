import numpy as np
from PIL import Image
import pytesseract
import cv2

def ocr_text(arr):
	img = cv2.cvtColor(np.uint8(arr), cv2.COLOR_RGBA2BGR)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return pytesseract.image_to_string(gray)

def ocr_number(arr):
	return int(ocr_text(arr))