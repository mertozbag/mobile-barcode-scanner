# mobile-barcode-scanner
Barcode scanner to use on Android Phone via python.

It can be used on Android Devices.

Both devices must be connected on the same internet point.

Telegram bot configuration should be done via console before start.

IP Webcam - Google Play application used in order to pass the image from phone camera to python.

✨ How to configure IP Webcam and mobile-barcode-scanner ✨
  
  - Open the app
  - Start a server
  - Write generated server ip to url section of main.py

✨ How it works ✨
- It gets the display from phone camera
- Process it to image
- Scans the image for barcode
- Resolves the barcode
- Searches resolved barcode number in defined excel file
- If it finds any matched number, it sends other related information via telegram.
