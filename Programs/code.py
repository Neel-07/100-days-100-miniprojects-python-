import pyqrcode
from pyqrcode import QRCode

# String that represents the QR code
s = "https://www.linkedin.com/in/neelmishra07/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the QR code in PNG format
url.png("qr_code.png", scale=8)


