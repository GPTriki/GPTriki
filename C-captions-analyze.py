import cv2
from PIL import Image
import requests
import base64
import io
import json

API_KEY = ""

results = {}

for i in range(1, 586):
    try:
        video_path = "./b-episodes/"+str(i)+".mp4"
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame0 = cap.read()
        cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
        ret, frame100 = cap.read()

        Image.fromarray(frame0).save("./c-stopframes/"+str(i)+"-0.jpg")
        Image.fromarray(frame100).save("./c-stopframes/"+str(i)+"-100.jpg")

        caption = Image.fromarray(frame0).rotate(5.5).crop((430, 440, 915, 560))

        image_buffer = io.BytesIO()
        caption.save(image_buffer, format="JPEG")
        image_buffer.seek(0)
        image_base64 = base64.b64encode(image_buffer.read()).decode("utf-8")


        payload = { "folderId": "", "analyze_specs": [{ "content": image_base64,
        "features": [{"type": "TEXT_DETECTION", "text_detection_config": {"language_codes": ["ru"]}}]}]}

        url = "https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze"
        headers = { "Content-Type": "application/json", "Authorization": f"Api-Key {API_KEY}" }
        response = requests.post(url, json=payload, headers=headers)

        results[i] = response.json()
    except Exception:
        pass

with open('./4-captions.json', 'w') as file:
    json.dump(results, file)
