#First u need to import the pyqrcode

import pyqrcode
from pyqrcode import QRCode
#link using of youtube
nilesh="https://thecleverprogrammer.com/2021/01/09/qr-codes-with-python/"
#create a QRcode of nilesh
url =pyqrcode.create(nilesh)
#create or save this folder "my" name or u can rename my.png
url.svg("my.svg",scale=8)
