#############################################################################
#
# testtwilio.py                                    
#
# Description:
#  
#	This program sends a text message to a phone number
#
# History:
#
#       2018.09.06	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python testtwilio.py INIFile sendto message
#       sendto is the phone number to send the message to
#
#############################################################################

from twilio.rest import Client		# Needed to talk to twilio
import sys				# Needed to process parameters
import ConfigParser			# Needed to process the ini file

myINIFile = ""				# Initialize these to blank to prevent errors.
my_account_sid = ""
my_auth_token = ""
my_Phone_Number =  ""

# Get the parameters

if len(sys.argv) < 4:
	print 'To run this program, enter ' + str(sys.argv[0]) + ' INIFile sendto message'
	print 'Argument List:', str(sys.argv)
	sys.exit(0)
else:
	myINIFile = sys.argv[1]
	sendto = sys.argv[2]
	messageList = sys.argv[3:]
	my_message = ' '.join(messageList)


# Read the INI file
# The format of ini file is like this (minus the #). Note, no quote around the string
#[DEFAULT]
# Your Account Sid and Auth Token and phone number from twilio.com/console
# my_account_sid = Your Account Sid from twilio.com/console
# my_auth_token = Your Auth Token from twilio.com/console
# my_Phone_Number = Your bought phone number from twilio.com/console
# my_Phone_Number should be of the format: +1aaallleeee (e.g. +12125551212)

config = ConfigParser.ConfigParser()


try:
	config.read(myINIFile)
	my_account_sid = config.get('DEFAULT', 'my_account_sid')
	my_auth_token =  config.get('DEFAULT', 'my_auth_token')
	my_Phone_Number =  config.get('DEFAULT', 'my_Phone_Number')

except:
	print "An error occurred getting parameters from " + myINIFile
	
# If there is a problem with the token or userid, then exit
if (my_account_sid == "") or (my_auth_token == "") or (my_Phone_Number == ""): 
	print 'Check your INI file: ' + myINIFile
	print 'my_account_sid or my_auth_token or my_Phone_Number  is not properly assigned a value'
	print 'To run this program, enter ' + str(sys.argv[0]) + ' INIFile sendto message'
	sys.exit(0)

# We have the information we need. Now send the message.

client = Client(my_account_sid, my_auth_token)

message = client.messages \
                .create(
                     body= my_message,
                     from_= my_Phone_Number,
                     to= sendto
                 )

print "Response back from twilio is:", message.sid


