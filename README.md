# Sql-Injection-automation
Python script to exploit SQL injection vulnerabilities in web applications to extract the password hashes of users stored in a database. It does so by sending malicious SQL queries to the web application and analyzing the response to determine whether a given condition is true or false. The script prompts the user to input a user ID, determines the length of the password hash, and extracts each character of the hash one by one using a brute-force method. The total number of queries made during the extraction process is output to the console.

## Requirements:
Python 3.x

requests library

## Usage:

Clone the repository

Install the requests library using pip
 
 ``pip install requests
 ``
 
Modify the 'charset' variable to include the set of characters used in the password hashes

Run the script using the command 

``python sql_injection.py
``

Input the user ID that you wish to extract the password hash for when prompted

The script will output the password hash and the number of queries made
