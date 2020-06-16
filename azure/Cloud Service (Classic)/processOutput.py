import json
import os

if os.path.isfile('output/output.json'):
    with open('output/output.json') as inp:
        d = json.loads(inp.read())
else:
    d = {}

for k,v in d.items():
    print k, v
