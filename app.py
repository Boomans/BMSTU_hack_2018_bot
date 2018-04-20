from flask import Flask
from flask import request, jsonify
import re

from data import actions


MAX_LEVINSHTEIN_DISTANCE = 4


def levenshtein(s, t):
    ''' From Wikipedia article; Iterative with two matrix rows. '''
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]


def get_data(message, request):

    length = len(message)
    if length != len(request):
        return None

    dist = 0
    data = {}

    for i in range(length):
        match_key = re.match(r'{(\w+)}', request[i])
        if match_key:
            data[match_key.group(1)] = message[i]
        else:
            dist += levenshtein(message[i], request[i])

    if dist < MAX_LEVINSHTEIN_DISTANCE:
        return data, dist

    return None


app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    message = request.form['message']
    message_split = message.split()

    response_dist = 1024
    response = None

    for action in actions:
        for action_request in action['requests']:
            data = get_data(message_split, action_request.split())
            if not data:
                continue

            data, dist = data
            if dist < response_dist:
                response_dist = dist
                response = jsonify({
                    key: value.format(**data) for key, value in action['response'].items()
                })
    print(response_dist)

    if response:
        return response
    return 'error\n'


if __name__ == '__main__':
    app.run()
