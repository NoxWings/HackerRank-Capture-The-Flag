#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.hackerrank.com/contests/capture-the-flag/challenges/infinite-links
import requests
from lxml import html

base_url = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/'

remaining = [base_url + 'qds.html']
seen = set()
passwds = set()

while remaining:
    next_url = remaining.pop()
    print('Requesting: '.format(next_url))
    dom = html.fromstring(requests.get(next_url).text)
    dom.make_links_absolute(base_url)
    seen.add(next_url)

    passwd = dom.xpath('//font/text()')
    if passwd:
        passwds.add(passwd[0])

    for link in dom.xpath('//a/@href'):
        if link not in seen:
            remaining.append(link)

print("#" * 80)
for passwd in sorted(passwds):
    print(passwd)
