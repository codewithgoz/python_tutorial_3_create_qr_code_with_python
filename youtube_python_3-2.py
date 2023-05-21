##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.3 - Script 2 
##############################################################
# Description: Simple script for custom qr generation from a list
# Dependencies:
# ----------------------------------------
# pip install "qrcode[pil]"
# ----------------------------------------
# Author: Goz
# https://codewithgoz.com
##############################################################

import qrcode

my_codes = [
            { 'name':'qr1', 'url':'https://www.sitio1.com'},
            { 'name':'qr2', 'url':'https://www.sitio2.com'},
            { 'name':'qr3', 'url':'https://www.sitio3.com'}
           ]

qr = qrcode.QRCode(
    # Version is an integer (1 to 40) that controls the size of the qr code
    version = None,
    # Error correction
    # ERROR_CORRECT_L: 7% errors can be corrected
    # ERROR_CORRECT_M: 15% errors can be corrected
    # ERROR_CORRECT_Q: 25% errors can be corrected
    # ERROR_CORRECT_H: 30% errors can be corrected
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    # Box size defines the number of pixels on each box of the qr
    box_size = 10,
    # Border controls how many boxes thick the border will be (4 is the minimum)
    border = 4 
)

for code in my_codes:
    try:
        qr.add_data(code['url'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        # We can use RGB colors tuples for fill and back color
        #img = qr.make_image(fill_color=(98,17,25), back_color=(0,0,0))
        img.save(code['name'] + '.png')
        print(f"{code['name']}.png fue generado!")
    except:
        print(f"{code['name']}.png no pudo generarse")
 
 
