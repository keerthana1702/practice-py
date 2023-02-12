import qrcode
from PIL import Image
qr= qrcode.QRCode(version=1,#indicates no of moduels if the data is huge version changes
                  error_correction=qrcode.constants.ERROR_CORRECT_H,#avoids overlapping
                  box_size=10,border=4)#give functionality and remove errors
qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit=True)#if the data fits then continue
img= qr.make_image(fill_color='purple',bg_color='white')#make can also add data
img.save("scan.png")
