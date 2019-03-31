from PIL import Image
import pytesseract

def ocr_str(image_name):   
    im=Image.open(image_name)
    text=pytesseract.image_to_string(im,lang="eng")
    return text

def write():                         
    text=open("string.txt","w+")
    text.write(ocr_str(a))
    text.close()

ocr_str("image.png")
