import json
import os

my_dict = {"TEST_SECRET" : "", "TEST_SECRET2" :""}
with open("/run/secrets/settings.json", "r") as f:
    my_dict.update(json.load(f))
print(my_dict)
assert my_dict["TEST_SECRET"]=="Test123teest"