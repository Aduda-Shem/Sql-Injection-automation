# Sql-Injection-automation
Python script to `automate sql injection` through:
     identifying if the request,character,user,users password is valid or invalid
     and extracting the users hash by iterating over potential characters in a vulnerable sql website

## Requirements:
Python 3.x

requests library

## Usage:

Clone the repository

Install the requests library using pip
 
 `pip install requests`
 
Modify the 'charset' variable to include the set of characters used in the password hashes

Run the script using the command 

`python sql_injection_password_extractor.py`

Input the user ID that you wish to extract the password hash for when prompted

The script will output the password hash and the number of queries made
