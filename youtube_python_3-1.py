##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.3 - Script 1 
##############################################################
# Description: Simple script for qr generation
# Dependencies:
# ----------------------------------------
# pip install "qrcode[pil]"
# ----------------------------------------
# Author: Goz
# https://codewithgoz.com
##############################################################

import qrcode

img = qrcode.make('https://codewithgoz.com')
img.save("my_qr.png")


