import json

with open('./4-episodes.json') as f:
    episodes = json.load(f)

i = 1

for inp in episodes:
    for segment in episodes[inp]:
        start = segment['start']
        end = segment['end']
        print(f'echo "ffmpeg -i ./a-yt-rips/{inp} -ss {(start / 30):.2f} -to {(end / 30):.2f} ./b-episodes/{i}.mp4"')
        i += 1
