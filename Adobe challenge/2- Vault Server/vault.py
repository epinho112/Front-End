import requests

#GLOBAL VARIABLES:

"""
Both VAULT_TOKEN and UNSEAL_VAULT_KEY for now they have to be generated on the CLI by using the following commnad
>>> curl --request POST --data '{"secret_shares": 1, "secret_threshold": 1}' http://127.0.0.1:8200/v1/sys/init | jq
Vault_Token is the root_token and UNSEAL_VAULT_KEY is the "keys_base64"
Each system will have a different VAULT_TOKEN and UNSEAL_VAULT_KEY, so generate the key and populate on the Variables below
"""
INCOMPLETE_URL = 'http://127.0.0.1:8200/v1/'
VAULT_TOKEN = '<add root_token>'
UNSEAL_VAULT_KEY = '"<add keys_base64>"'

#Function to Unseal and run commands on the Vault Server
def unseal_vault():
	url = INCOMPLETE_URL + 'sys/unseal'
	payload = '{"key": %s}'% (UNSEAL_VAULT_KEY)
	api_results = requests.post(url, data = payload)

'''
Check if Vault server system is healthy or having any issues Possible vallues
>> 200 if initialized, unsealed, and active
>> 429 if unsealed and standby
>> 472 if disaster recovery mode replication secondary and active
>> 473 if performance standby
>> 501 if not initialized
>> 503 if sealed
'''
def get_vault_system_health():
	url = INCOMPLETE_URL + 'sys/health'
	api_results = requests.get(url)
	return api_results.status_code

#Function responsible in adding foo:bar key value pair to secret/text
def add_foo_bar_secret():
	print("Values are wrong:\nUpdating to foo:bar")
	url = INCOMPLETE_URL + 'secret/text'
	payload = '{"foo" : "bar"}'
	headers = {"X-Vault-Token": VAULT_TOKEN}
	api_results = requests.post(url, data = payload, headers = headers)
	
#this function will check and update Secrets Engine - Version 1 (API) 
def get_secret_v1():
	url = INCOMPLETE_URL + 'secret/text'
	headers = {"X-Vault-Token": VAULT_TOKEN}
	api_results = requests.get(url, headers=headers)
	json_results = api_results.json()
	data_results = json_results['data']
	
	if "foo" in data_results:
		if(data_results["foo"] == "bar"):
			print("Key: Value listed below ")
			print(data_results)
			#add and else statement and check for is bar is the value
		else:
			add_foo_bar_secret()
	else:
		add_foo_bar_secret()


#### MAIN BEGINS ###

#Check the System Health status and store in status_code Variable
#If the status code = 200 it will get secret using API V1
#If status code different than 200 will display the status code number.
unseal_vault()

status_code = get_vault_system_health()

if status_code == 200:
	get_secret_v1()
else:
	print(status_code)
	
### MAIN ENDS ###	
	




### EXTRA FUNCTIONS USED TO LEARN/RESEARCH DOCUMENTATION ###
#this function will check and update Secrets Engine - Version 2 (API)
#This function is not used on the may code
def get_secret_v2():
	url = 'http://127.0.0.1:8200/v1/secret/data/test'
	headers = {"X-Vault-Token": "s.knspkfLS5lbI87uCYn815RQu"}
	api_results = requests.get(url, headers=headers)
	json_results = api_results.json()
	data_results = json_results['data']['data'];
	print(api_results.status_code)
	print(data_results)
	#if(results['data']['data']['foo']):
	
	if "foo" in data_results:
    		print("Key: Value listed below ")
    		print(data_results)
	else:
    		print("this will not")
    		url = 'http://127.0.0.1:8200/v1/secret/data/test'
    		payload = '{"data": {"foo" : "bar" }}'
    		api_results = requests.post(url, data = payload, headers = headers)
    		print(api_results.status_code)
	
