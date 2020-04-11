import redis
import time

client = redis.Redis(host='localhost', port=6379)

print('Starting off with no keys', client.keys())

print('Setting key with an expire time of 3 seconds', client.set('Jeff', 'is awesome', ex=3))

print('List of keys', client.keys())

print('Getting key "Jeff"', client.get('Jeff'))

print('Waiting for key to expire...')
time.sleep(3)

print('No more keys', client.keys())
