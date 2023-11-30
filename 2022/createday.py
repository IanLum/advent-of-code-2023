import os
import sys

try:
    day = sys.argv[1]
except IndexError:
    raise SystemExit('No day number inputed, try: python3 ' + sys.argv[0] + ' [DAY NUMBER]')

os.mkdir('day' + day)
open('day' + day + '/day' + day + '_input.txt', 'x')
open('day' + day + '/day' + day + '_test.txt', 'x')
with open('sampleday.py') as sample:
    text = sample.read().replace('[DAY]', day)
    with open('day' + day + '/day' + day + '_pt1.py', 'w') as pt1:
        pt1.write(text)
    with open('day' + day + '/day' + day + '_pt2.py', 'w') as pt1:
        pt1.write(text)