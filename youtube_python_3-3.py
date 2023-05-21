##############################################################
# CODE WITH GOZ Youtube Channel - Python Video No.3 - Script 3 
##############################################################
# Description: Simple script for custom qr generation
# Dependencies:
# ----------------------------------------
# pip install "qrcode[pil]"
# ----------------------------------------
# Author: Goz
# https://codewithgoz.com
##############################################################

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SolidFillColorMask, HorizontalGradiantColorMask, VerticalGradiantColorMask, ImageColorMask, SquareGradiantColorMask
from PIL import Image

qr = qrcode.QRCode(version = None, error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('https://google.com')

# Styled image

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_1.save("rounded_qr.png")

img_2 = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
img_2.save("gapped_qr.png")

img_3 = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
img_3.save("circle_qr.png")

img_4 = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
img_4.save("vertical_qr.png")

img_5 = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
img_5.save("horizontal_qr.png")

img_6 = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
img_6.save("square_qr.png")


# Other color masks

img_7 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_7.save("radial_qr.png")

img_8 = qr.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask())
img_8.save("solid_qr.png")

img_9 = qr.make_image(image_factory=StyledPilImage, color_mask=SquareGradiantColorMask())
img_9.save("square_mask_qr.png")

img_10 = qr.make_image(image_factory=StyledPilImage, color_mask=HorizontalGradiantColorMask())
img_10.save("horizontal_mask_qr.png")

img_11 = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask())
img_11.save("vertical_mask_qr.png")

logo = Image.open('/home/goz/youtube/python/video_3/codewithgoz.png')
img_12 = qr.make_image(image_factory=StyledPilImage, color_mask=ImageColorMask(back_color=(255,255,255), color_mask_image=logo))
img_12.save("image_gradiant_qr.png")


img_13 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/home/goz/youtube/python/video_3/codewithgoz.png")
img_13.save("my_logo_qr.png")

img_14 = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer(), color_mask=RadialGradiantColorMask(), embeded_image_path="/home/goz/youtube/python/video_3/codewithgoz.png")
img_14.save("qr_extra.png")











