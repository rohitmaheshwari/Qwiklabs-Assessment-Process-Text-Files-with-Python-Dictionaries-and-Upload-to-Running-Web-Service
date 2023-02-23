#! /usr/bin/env python3
import os
import requests

path = '/data/feedback'
url = 'http://34.72.34.104/feedback/'
for filename in os.listdir(path):
        f = open(os.path.join(os.getcwd(), path, filename), 'r')
        lines = f.read().split('\n')
        body = {
                "title": lines[0],
                "name": lines[1],
                "date": lines[2],
                "feedback": lines[3]
        }
        r = requests.post(url, data = body)
        r.raise_for_status()
