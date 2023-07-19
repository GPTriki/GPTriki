import cv2
from PIL import Image

for i in range(1, 586):
    video_path = "./b-episodes/"+str(i)+".mp4"
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret, thumb = cap.read()
    
    Image.fromarray(thumb[:, :, [2, 1, 0]]).save("./d-thumbnails/"+str(i)+".jpg")
