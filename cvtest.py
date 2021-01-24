import cv2
import io
import base64

capture = cv2.VideoCapture(0)

while (True):
    # get image frame from stream and encode to jpeg image
    ret, img = capture.read()
    is_success, buffer = cv2.imencode(".jpg", img)
    # get image stream buffer
    io_buf = io.BytesIO(buffer)
    # output base64 encoded image to console
    new_image_string = base64.b64encode(io_buf.getvalue()).decode("utf-8")
    print(new_image_string)