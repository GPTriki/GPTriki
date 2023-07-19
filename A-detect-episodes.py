import cv2
from PIL import Image, ImageChops
import numpy as np

video_path = "./a-yt-rips/1.mp4" # 1-5
cap = cv2.VideoCapture(video_path)

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

def get_frame(frame_number = -1):
    if frame_number != -1:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
    ret, frame = cap.read()
    
    if not ret:
        return None
    
    return Image.fromarray(frame)

region = (70, 45, 140, 70)
reference = get_frame(32000).crop(region)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

start = 0
last_is_payload = False
periods = []

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    crop = Image.fromarray(frame).crop(region)
    diff = np.array(ImageChops.difference(reference, crop))
    is_payload = np.sum(diff > 10) / diff.size < 0.52
    
    if(last_is_payload):
        if(not is_payload):
            last_is_payload = False
            period = {"start": start, "end": int(cap.get(cv2.CAP_PROP_POS_FRAMES))}
            periods.append(period)
            print(period)
            
    else:
        if(is_payload):
            last_is_payload = True
            start = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
