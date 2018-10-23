#############################################################################
#
# tweetalert.py                                    
#
# Description:
#  
#	This program acts as a bot. It will take the status you pass it and 
# assume it is the filename of a .jpg file. It can then post either the status
# you give it or the jpg image.
#
# History:
#
#       2015.10.02	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python tweetalert.py INIFile status
#
#############################################################################

import tweepy as tp			# needed to talk to twitter
import sys					# needed to process input parameters
import ConfigParser			# need to process the input file

# Process the input parameters.
if len(sys.argv) == 3:
	myINIFile = sys.argv[1]
	my_status = sys.argv[2]
else:
	print "you need to pass an INI file and a status (e.g. good) as input"
	exit(0)

# Read the INI file
# The format of ini file is like this (minus the #). Note, no quote around the string
#[DEFAULT]
#myconsumer_key = your twitter consumer key
#myconsumer_secret = your secret key
#myaccess_token = your access token
#myaccess_secret = your secret access value

config = ConfigParser.ConfigParser()
config.read(myINIFile)

try:
	consumer_key = config.get('DEFAULT', 'myconsumer_key')
	consumer_secret = config.get('DEFAULT', 'myconsumer_secret')
	access_token = config.get('DEFAULT', 'myaccess_token')
	access_secret = config.get('DEFAULT', 'myaccess_secret')

except:
	print "An error occurred getting keys to talk to twitter"
	
# If there is a problem with the INI file, then exit
if (consumer_key == "") or (consumer_secret == "") or (access_token == "") or (access_secret == "") :
	print 'Check your INI file: ' + myINIFile
	print 'You need to assign four keys in this file.'
	sys.exit(0)

# Login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# Use this command if the jpg images are in a different directory.
# os.chdir('images')

# Assume you have this image.
my_image = my_status + ".jpg"

try:
    # Post the image
    api.update_with_media(my_image)
    
    # Post the status you posted
    api.update_status(my_status)
	
finally:
	exit(0)
