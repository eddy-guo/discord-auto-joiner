import pytesseract, cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = cv2.imread("images/code1.jpg")
results = pytesseract.image_to_string(im, lang = 'eng')

print("-" * 40)
print(
    'Results from tesseract: \n'
    f'{results}'
)
print("-" * 40)

results_list = results.replace(" ", "").split("\n") # remove spaces and split string into list of strings by newlines
ocr_list = list(filter(None, results_list)) # filter out empty strings in list

print(
    'Final list of strings: \n'
    f'{ocr_list}')
print("-" * 40)