import time

import requests
import cv2
import numpy as np
import imutils
from pyzbar import pyzbar
import openpyxl
import telegram_send
"""
It`s a script for mobile barcode scanner.
Start a server from IP Webcam - Google Playstore,
replace the below URL with your own. Make sure to add "/shot.jpg" at last.
Both devices should be connected to same modem/router.
"""

url = "http://192.168.1.109:8080/shot.jpg"

# barcode analyzer
def read_barcodes(img):
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        # variables for barcode
        x, y, w, h = barcode.rect

        barcode_info = barcode.data.decode('utf-8')
        # setting coordinates
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # resolving barcode
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        # data file to match barcode
        theFile = openpyxl.load_workbook('ItemData.xlsx')

        # settings to read sheet data
        currentSheet = theFile["Sheet1"]
        for row in range(1, currentSheet.max_row + 1):
            for column in "D":  # can add or reduce the columns
                cell_name = "{}{}".format(column, row)
                if currentSheet[cell_name].value == barcode_info:
                    name = "{}{}".format("C", row)
                    quantity ="{}{}".format("E", row)
                    price = "{}{}".format("F", row)
                    disc = "{}{}".format("H", row)

                    # to send matched barcode details to phone via telegram
                    telegram_send.send(messages=["Ürün bilgileri, İsim: " + str(currentSheet[name].value) +
                                                 " Adet: " + str(currentSheet[quantity].value) +
                                                 " Fiyat: " + str(currentSheet[price].value) +
                                                 " İskonto: " + str(currentSheet[disc].value)])
                    time.sleep(3)

    return img

def main():
    while True:
        # process for getting image from phone camera and resolving barcode
        try:
            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=1000, height=1000)
            img = read_barcodes(img)
            cv2.imshow("Android_cam", img)
        except:
            cv2.destroyAllWindows()

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()