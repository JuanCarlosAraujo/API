import pytesseract as tess
from PIL import Image
import cv2
tess.pytesseract.tesseract_cmd = r'D:\PROGRAMS INSTALL\tesseract\tesseract.exe'

# my_image = Image.open('D:\\PROGRAMMING\\3-Python\\My_Virtual_Envs\\ocr_youtube\\routing.PNG')

def textRecognition():
    my_image = cv2.imread('imagenAPI.jpeg')
    txt = tess.image_to_string(my_image)
    json = {"text": str(txt)}
    return json

