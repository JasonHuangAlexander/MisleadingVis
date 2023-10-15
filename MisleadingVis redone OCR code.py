from PIL import Image
import pytesseract
import pprint
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
originalImage = Image.open("C:\Jason Alexander\MisleadingVIs\COVID vs flu cases, 2020 1.png")
extractedFeatures = {
    "x_axis":[], 
    "y_axis":[], 
    "title":[], 
    "legend":[], 
    "x_title":[], 
    "y_title":[],
    "data":[],
    "bottom_y_tick":[]
}
def extract_bottom_y_tick():
    bottom_y_tick = []
    image = originalImage.crop((41,291,75,310))
    OCRextraction = pytesseract.image_to_string(image,config ="--psm 6")
    bottom_y_tick.append(OCRextraction)
    extractedFeatures["bottom_y_tick"] = bottom_y_tick
def extract_x_axis():
    x_axis = []
    image = originalImage.crop((74,302,600,325))
    OCRextraction = pytesseract.image_to_string(image)
    x_axis.append(OCRextraction)
    extractedFeatures["x_axis"] = x_axis
def extract_y_axis():
    y_axis = []
    image = originalImage.crop((41,75,78,308))
    OCRextraction = pytesseract.image_to_string(image)
    y_axis.append(OCRextraction)
    extractedFeatures["y_axis"] = y_axis
def extract_title():
    title = []
    image = originalImage.crop((0,0,600,46))
    OCRextraction = pytesseract.image_to_string(image)
    title.append(OCRextraction)
    extractedFeatures["title"] = title
def extract_legend():
    legend = []
    image = originalImage.crop((0,49,600,75))
    OCRextraction = pytesseract.image_to_string(image)
    legend.append(OCRextraction)
    extractedFeatures["legend"] = legend
def extract_x_title():
    x_title = []
    image = originalImage.crop((39,330,600,363))
    OCRextraction = pytesseract.image_to_string(image)
    x_title.append(OCRextraction)
    extractedFeatures["x_title"] = x_title
def extract_y_title():
    y_title = []
    image = originalImage.crop((0,0,300,370)).rotate(270).crop((0,0,250,70))
    OCRextraction = pytesseract.image_to_string(image)
    y_title.append(OCRextraction)
    extractedFeatures["y_title"] = y_title
def extract_data():
    data = []
    x_axis = []
    image = originalImage.crop((74,302,600,325))
    print(pytesseract.image_to_boxes(image,config="--psmg"))
    #OCRextraction = pytesseract.image_to_string(image)
    
    
    extractedFeatures["data"] = data

extract_x_axis()
extract_y_axis()
extract_title()
extract_legend()
extract_x_title()
extract_y_title()
extract_data()
extract_bottom_y_tick()
#pprint.pprint(extractedFeatures)
