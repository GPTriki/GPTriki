from pyrogram import Client
import json
import time

API_ID = ''
API_HASH = ''
SESSION_NAME = 'main'

meta = json.load(open('./meta.json'))

with Client(SESSION_NAME,  api_id=API_ID, api_hash=API_HASH) as app:
    for item in meta:
        minutes = item['duration'] // 60
        seconds = item['duration'] % 60

        app.send_video(
            chat_id='@GPTriki',
            video=f"./b-episodes/{item['id']}.mp4",
            caption=f"Серия: {item['id']} из 585\nТема: {item['title']}\nДлительность: [{minutes:02d}:{seconds:02d}]\nВсе серии: {item['tg']}",
            supports_streaming=True,
            width=1280,
            height=720,
            thumb=f"./d-thumbnails/{item['id']}.jpg"
        )
        time.sleep(10)
