from random import random
from time import sleep
import redis
import datetime

CHANNEL = 'hungry'
backend = redis.Redis(host="localhost", port=6379, db=0)

def message(content: str):
    return f"[{datetime.datetime.now()}] {content}"

while True:
    sleep(3)
    content = str(int(random() * 100))
    print(content)
    backend.publish(channel=CHANNEL, message=message(content))