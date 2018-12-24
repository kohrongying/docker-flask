from flask import Flask
from redis import Redis 

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
  redis.incr('hits')
  return 'Flask Dockerized. Viewed {} time(s)'.format(redis.get('hits'))