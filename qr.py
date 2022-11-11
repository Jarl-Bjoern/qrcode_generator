# Rainer Christian Bjoern Herold
# Vers 0.1 11.11.2022

# Libraries
from os.path import expanduser, join
from qrcode import QRCode
from qrcode.constants import *
from sys import argv

# Settings
qr = QRCode (
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=25,
    border=4,
)

# Main
if __name__ == '__main__':
    if (len(argv) > 1): qr.add_data(argv[1])
    else: qr.add_data(input('URL: '))
    qr.make(fit=True)
    
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(join(expanduser(r'~\Desktop'), 'qr_file.png'))