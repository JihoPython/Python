import redis


CHANNEL = 'hungry'

backend = redis.Redis(host="localhost", port=6379, db=0)
client = backend.pubsub()

client.subscribe(CHANNEL)

while True:
    res = client.get_message(timeout=5)
    if res:
        message = res['data']
        if type(message) is bytes:
            print(message.decode('utf-8'))