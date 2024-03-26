import random
import numpy as np


import requests
import names

from schemas import Cat

s = requests.Session()
s.trust_env = False

api_base = "http://127.0.0.1:8000"

random.seed()

c = Cat(name=str(names.get_first_name()), age=random.randrange(0, 20), colors=["grey"], dimensions=(random.random()*5, random.random()*15 ))
s.put(f"{api_base}/add", c.model_dump_json())

r = s.get(api_base)
for c_jspn in r.json():
    c = Cat.model_validate(r.json()[0])
    print(c)