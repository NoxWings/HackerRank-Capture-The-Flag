#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.hackerrank.com/contests/capture-the-flag/challenges/secret-key
import requests
import json

keys_web = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json'
detail_web = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/{}.json'
keys = json.loads(requests.get(keys_web).text)
news = [json.loads(requests.get(detail_web.format(key)).text)['news_title'] for key in keys]
for n in news:
    print(n)
