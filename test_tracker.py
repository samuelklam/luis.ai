#!/usr/bin/env python

"""
This Script tests the LUIS.ai applications
"""

from __future__ import print_function
import argparse
import csv
import random

try:
	import json
except ImportError:
	import simplejson as json
import sys
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

API_LINK = "https://api.projectoxford.ai/luis/v1/application?id=7ef18924-6aee-44d7-be98-1aa2a7428282&subscription-key=f5ff50ec30804649a7f1c52dc782c089"

def url_converter(s):
	return API_LINK + "&q=" + s.replace(" ", "%20")

def csv_splitter(s):
	return s.split(",")

def get_response(query):
	resp = urlopen(url_converter(query))
	returnobj = resp.read()

	try:
		return json.loads(returnobj)
	except:
		return json.loads(returnobj.decode(resp.info().get_content_charset()))


def test_file(filename):
	intent_right = 0
	entity_right = 0
	num_total = 0

	neg_intent_examples = []
	neg_entity_examples = []
	pos_examples = []

	with open(filename, 'rU') as f:
		csvreader = csv.reader(f, dialect=csv.excel_tab)
		for index, row in enumerate(csvreader):
			if index%5 ==0:
				print("{}% done".format(index/25.*100))
			current_test = csv_splitter(row[0])
			json_response = get_response(current_test[0])

			# print current_test[0]
			response_intent = json_response['intents'][0]['intent']
			response_entities = [o['entity'] for o in json_response['entities']]
			if not response_entities:
				response_entities.append(" ")

			num_total+=1
			if current_test[1] == response_intent and current_test[2] in response_entities:
				# print "both right"
				pos_examples.append(current_test[0])
				intent_right+=1
				entity_right+=1
			elif current_test[1] == response_intent:
				# print "intent right"
				neg_entity_examples.append(current_test[0])
				intent_right+=1
			elif current_test[2] in json_response['entities']:
				# print "entity right"
				neg_intent_examples.append(current_test[0])
				entity_right+=1
			else:
				# print "all wrong"
				neg_intent_examples.append(current_test[0])
				neg_entity_examples.append(current_test[0])
			# print "----"

			# break
	print("------- SUMMARY ------------------")
	print("Total tested: {}".format(num_total))
	print("Intent correct: {} - {}%".format(intent_right, 100*intent_right/float(num_total)))
	print("Entity correct: {} - {}%".format(entity_right, 100*entity_right/float(num_total)))
	print()
	print("Correct Examples:")
	for s in random.sample(pos_examples, min(len(pos_examples), 10)):
		print(s)
	print()
	print("Examples with wrong intent:")
	for s in random.sample(neg_intent_examples, min(len(neg_intent_examples), 10)):
		print(s)
	print()
	print("Examples with wrong entity:")
	for s in random.sample(neg_entity_examples, min(len(neg_entity_examples), 10)):
		print(s)

def main(arguments):

	parser = argparse.ArgumentParser()
	parser.add_argument('--basic', help="Tests the first version of the Activity Tracker", action="store_true")
	parser.add_argument('--updated', help="Tests the updated version of the Activity Tracker", action="store_true")
	args = parser.parse_args(arguments)

	# teststring = "This is a test"
	# print url_converter(teststring)

	use_file = ""
	if args.basic:
		use_file = "basic.csv"
	elif args.updated:
		use_file = "updated.csv"

	if use_file:
		test_file(use_file)
	else:
		print("Please run this script in either basic or updated mode")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
