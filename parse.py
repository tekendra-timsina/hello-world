import json
import os

with open("settings.json", "w") as f:
    json.dump(json.loads(os.getenv('TEST_SECRET_2')), f)