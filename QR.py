import pyqrcode
import png
QRstring = "www.google.com"
url = pyqrcode.create(QRstring)
url.png('qrcode.png', scale=8)
