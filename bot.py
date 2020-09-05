from wit import Wit
import json
import requests

client = Wit("LUAK3FMQHOZWWEYYNOPP73PMIHO44TZF")
country_codes = json.load(open('country-2-code.json','r'))

def get_country(msg):
	resp = client.message(msg)
	country = resp['entities']['wit$location:location'][0]['resolved']['values'][0]['name']
	return country

def get_2_digit_code(country_name):
	return country_codes[country_name]

def get_stats(country_code, country):
	resp = requests.get('https://corona-api.com/countries/' + country_code).json()
	response = "\033[92mToday there were new " + str(resp['data']['today']['confirmed']) + " cases and " + str(resp['data']['today']['deaths']) + " new deaths in " + country + "."
	response += " This bring the tally to " +  str(resp['data']['latest_data']['confirmed']) + " confirmed, " +  str(resp['data']['latest_data']['deaths']) + " deaths, " +  str(resp['data']['latest_data']['recovered']) + " recovered and " +  str(resp['data']['latest_data']['critical']) + " critical patients. \033[0m"
	return response

print("Welcome to COVID Tracker. Enter q to exit. You can ask me question like: How many corona cases are there in India.")

while(True):
	inp = input("Enter a query: ")
	if inp == 'q' or inp =='Q':
		exit()

	try:
		country = get_country(inp)
		country_code = get_2_digit_code(country.lower())
		stats = get_stats(country_code, country)
		print(stats)
	except:
		print("\033[93mCOVID is an earthly problem. Doesn't apply to alien countries!\033[0m")
