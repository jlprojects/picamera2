#!/usr/bin/python3

# Capture a full resolution image to memory rather than to a file.

from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
preview_config = picam2.preview_configuration()
capture_config = picam2.still_configuration()

picam2.configure(preview_config)
picam2.start()
time.sleep(2)

image = picam2.switch_mode_and_capture_image(capture_config)
image.show()


time.sleep(5)

picam2.close()
