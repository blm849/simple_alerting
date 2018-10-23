# simple_alerting repo
## Introduction

I started these programs because I was creating a number of VMs in the cloud and I needed a way for these VMs to report on their status. I developed a number of programs to communicate with various services to send out alerts. These programs were written in Python and can be found below.

I wanted to be able to report alerts in a number of ways:
- via email (using Mailgun)
- via an iPhone app (Pushover)
- via SMS (Twilio)
- via Twitter

The programs below do that.


## File Listing

These Python programs do simple alerting on your system. I run them in VMs but you can run them on any platform that supports the Python language and has access to the Internet:
- mailgun.py: This program reads a file and sends it out via mailgun
- pushover.py: This program reads a file and sends it out via Pushover
- twilioalert.py: This program sends a text message to a phone number
- tweetalert.py: This program acts like a twitter bot. It will take the status you pass it and assume it is the filename of a .jpg file. It can then post either the status you give it or the jpg image.

For each server (e.g. twitter) you would need to get your own credentials, create an ini file based on the ini.sample file, and put your credentials in your ini file.
- mailgun.ini.sample
- pushover.ini.sample
- twilioalert.ini.sample
- tweetalert.ini.sample

The following files are sample JPEG files you can use with the tweetalert.py programs
  - bad.jpg
  - good.jpg

Other files in this repo:
- LICENSE
- README.md

For more information, see the comments section of the Python programs.
