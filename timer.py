#!/usr/bin/env python3
import time

t = {'start':'', 'end':''}

def startTime():
	t['start'] = time.time()
	return t['start']

def endTime():
	print('\n--------- Time: %ss ---------' % (time.time() - t['start']))