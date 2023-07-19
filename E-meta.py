import json

captions = json.load(open('./2-captions.json'))
episodes = json.load(open('./4-episodes.json'))

i = 1
eps = []

for inp in episodes:
    for caption in episodes[inp]:
        ep = {'id': i, 'title': captions[str(i)], 'duration': (caption['end'] - caption['start']) // 30, 'tg': 't.me/GPTriki'}
        eps.append(ep)
        i += 1
        
print(json.dumps(eps))
