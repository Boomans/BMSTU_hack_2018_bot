from flask import Flask
from flask import request, jsonify
import re
from json import loads
import levenshtein

from data import actions


MAX_LEVINSHTEIN_DISTANCE = 4


def pylevenshtein(s, t):
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

    print(levenshtein.distance(s, t))
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
            continue

        match_key = re.match(r'\[(.+)\]', request[i])
        if match_key:
            min_dist = 1024

            for word in match_key.group(1).split('|'):
                levenshtein_dist = pylevenshtein(message[i], word)
                if levenshtein_dist < min_dist:
                    min_dist = levenshtein_dist

            dist += min_dist
            continue

        dist += pylevenshtein(message[i], request[i])

    if dist < MAX_LEVINSHTEIN_DISTANCE:
        return data, dist

    return None


app = Flask(__name__)


@app.route('/', methods=['GET'])
def help():
    response = ""
    for action in actions:
        pass


@app.route('/', methods=['POST'])
def bot():
    message = request.form['message'].lower()

    meta_data = None
    if request.form.get('meta_data'):
        meta_data = loads(request.form['meta_data'])

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

                if meta_data:
                    data.update(meta_data)
                response = jsonify({
                    key: value.format(**data) for key, value in action['response'].items()
                })
    print(response_dist)

    if response:
        return response
    return 'error\n'


if __name__ == '__main__':
    app.run()
