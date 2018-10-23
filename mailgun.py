#############################################################################
#
# mailgun.py                                    
#
# Description:
#  
#	This program reads a file and sends it out via mailgun
#
# History:
#
#       2018.09.06	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python mailgun.py fileName INIfile
# 	fileName is the file that is going to be sent out via mailgun
#
#############################################################################

# Initialization of variables, etc.
#import sys, subprocess, httplib, urllib
#import ConfigParser
import sys, ConfigParser, requests
myMessage = ""
myPushoverToken = ""
myPushoverUserID = ""

# Get the parameters

if len(sys.argv) != 3:
	print 'To run this program, enter ' + str(sys.argv[0]) + ' filename  INIfile'
	print 'Argument List:', str(sys.argv)
	sys.exit(0)
else:
	inputFile = sys.argv[1]
	myINIFile = sys.argv[2]
	
# Read the INI file
# The format of ini file is like this (minus the #). Note, no quote around the string
#[DEFAULT]
#myAPI = your Mailgun API key
#MyFrom = your Mailgun from information
#MyTo = email recipient
#MySubject = Email subject line


config = ConfigParser.ConfigParser()
config.read(myINIFile)

try:
	myAPI = config.get('DEFAULT', 'myAPI')
	myFrom =  config.get('DEFAULT', 'myFrom')
	myTo =  config.get('DEFAULT', 'myTo')
	mySubject =  config.get('DEFAULT', 'mySubject')
except:
	print "An error occurred getting parameters from" + myINIFile
	
# If there is a problem with the token or userid, then exit
if (myAPI == "") or (myFrom == "") or (myTo == "") or (mySubject == ""): 
	print 'Check your INI file: ' + myINIFile
	print 'myAPI or myFrom or myTo or mySubject is not properly assigned a value'
	sys.exit(0)

# Main body of the shell script.

#Check to see if the pingTable exists and it is a text file.
try:
	f = open(inputFile)
	lines = f.readlines()
	for line in lines:
		myMessage = myMessage + line
	f.close()
			
except:
	myMessage = "Error reading " + inputFile

try:
  returnCode = requests.post(
        "https://api.mailgun.net/v3/sandbox069aadff8bc44202bbf74f02ff947b5f.mailgun.org/messages",
        auth=("api", myAPI),
        data={"from": myFrom,
              "to": myTo,
              "subject": mySubject,
              "text": myMessage})
except:
	print "Errors trying to connect to the API for Mailgun"

print returnCode
sys.exit(0)
