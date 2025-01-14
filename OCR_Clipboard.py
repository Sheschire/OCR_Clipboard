from pytesseract import pytesseract
from PIL import ImageGrab
import pyperclip

# Configure Tesseract path
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = ImageGrab.grabclipboard()
image = image.convert('L')

# Extract text
text = pytesseract.image_to_string(image)
pyperclip.copy(text)
