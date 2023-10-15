from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

test = Image.open("C:\Jason Alexander\MisleadingVIs\COVID vs flu cases, 2020 1.png")
#test.show()
print(pytesseract.image_to_string(test))

