from PIL import Image
import pytesseract

#Define path to tesseract
path_to_tesseract = r'/home/safaet/Codes/Development/FastAPI/text-to-image/env/bin/pytesseract'

#Define path to image
path_to_image = 'images/sampletext1-ocr.png'

#Point tesseract_cmd to tesseract
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)