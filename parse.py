import json

file_path = '/run/secrets/myfile.json'

with open(file_path, 'r') as f:
    data = json.load(f)
    print(data)