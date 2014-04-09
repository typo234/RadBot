#Ed v1.1
#
#Satellite from days of old, lead me to your access code!

#important importing imports
import sys
import socket
import time
import string
from sys import argv

#script, chan = argv

#initialize formalities, names, server, ports, etc
HOST = "dot"#"dot.cs.wmich.edu" #could also be SERVER
PORT= 6667
channel = '#thisisatest'
NICK = "RadicalEdward"
IDENT = "RadicalEdward"
REALNAME = "Edward Wong Hau Pepelu Tivrusky IV"
REALREALNAME = "Francoise Appledehli"
owner  = "typo"
readbuffer = ''

#Start connecting, sockets, I don't get this part so much yet
s = socket.socket() #creating the socket
print "Connecting to server: "+HOST
s.connect((HOST, PORT)) #connecting to the server
s.send("NICK %s\r\n" % NICK) #This sends the nick to the server
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME)) #identify to the server
s.send("JOIN %s\r\n" % channel)

def sendmessage(message):
	s.send('PRIVMSG ' +channel+' :'+message+'\r\n')

while 1:  #5evr looping
	data = s.recv(2048)
	if data.find ('PING') != -1:
		s.send('PONG' + data.split()[1]+'\r\n')
	if data.find( '~test' ) != -1:
		sendmessage('This is a test!')
		sendmessage(data.split()[0])#displays username and connection
		sendmessage(data.split()[1])#PRIVMSG
		sendmessage(data.split()[2])#channel
		sendmessage(data.split()[3])#~test.  this is the command,
		#any after this will be user inpu
	####Who is Ed?
	if data.find('!whois RadicalEdward') != -1:
		sendmessage('Ed is Edward Wong Hau Pepelu Tivrusky IV!  Nice to meet ya!')
	if data.find('who is RadicalEdward') != -1:
		sendmessage('Ed is Edward Wong Hau Pepelu Tivrusky IV!  Nice to meet ya!')
	if data.find('who is radicaledward') != -1:
		sendmessage('Ed is Edward Wong Hau Pepelu Tivrusky IV!  Nice to meet ya!')
	if data.find('hello Ed') != -1:
		sendmessage('Hi hi!~')
	####Helping helping!
	if data.find('bot roll call') != -1:
		sendmessage("You found Ed!")
	if data.find( '~officehours' ) != -1:
		sendmessage('Misclik-TR 12-3 | Sphinx-MW 1-3 | Flay-R 3-5 | Typo-M 5-6, T 5-7')
	if data.find( '~pi' ) != -1:
		sendmessage('3.14159265358979323846264338327950288419716939937510')
	if data.find( '~help' ) != -1:
		sendmessage('Ed can help ~test, ~officehours, ~help, ~pi')
	if data.find('bebop') != -1:
		sendmessage('BEBOP BEBOP!')
	####Silly
	if data.find('~Bananas') != -1:
		sendmessage('Banana!  Plantana!  Santana!  BONANZA!')
	if data.find('~bananas') != -1:
		sendmessage('Banana!  Plantana!  Santana!  BONANZA!')
	####Secrets secrets :S
	if data.find('timmaha?') != -1:
		sendmessage('Rahhhr  D:<<')
	if data.find('renix?') != -1:
		sendmessage('My twin!!')
	if data.find('flay?') != -1:
		sendmessage('Flayflay!')
	

#Ed: Neeeeee check-check-check-checkmate!
#Hex: Huh?
#Ed: Aah, so Ed thought. Well, at least my knight takes your rook.
#Hex: [laughs] Penelope? This is either an idiot or a genius! I like this fellow! [laughs]


#SHIT TO DO:
#Edward bot will recite pi to 25 decimal points, crack passwords, do advanced web searches, 
#Also she'll spout nonsense randomly.  In addition, make friends w/ a satellite
#And and and play chess.  Also will list lofty goals, and hijack.  Also lie about things she can do.
#Print out "Ding dong time for x to do office hours!!" during the office hours of
#whomever is on the schedule
#Find google calendar parser for office hours rather than hardcoding
