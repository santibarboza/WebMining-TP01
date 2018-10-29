#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata
import tweepy
import json
import codecs
import os
import signal
import time
import alex

consumer_key = 'd2lXdoAa1B1ts8pzEmTzrYym7'
consumer_secret = 'D1Z0LHL2jXpKQhOiwIpYGyXMAd0JPDRww6NJs8RWlQ7dn2gTCJ'
access_token = '192439126-3UyW8XPUL5mZbtjGnHGq20PLj1tiXcLoUssmdROx'
access_token_secret = 'JyDpIQEOMYOpHROdjo7FELFYpf39XcDBMDddtGZFi8NxX'

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))        

def get_auth():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return auth

class MyStreamListener(tweepy.StreamListener):
	
	def on_data(self, data):
		try:
			decoded = json.loads(data)
			texto=elimina_tildes(decoded['text'].lower()).replace('\n',' ')
			#print(texto)
			#print("-"*10)
			with codecs.open("tweets.txt", "a", "utf-8") as myfile:
        			myfile.write(texto+'\n')
		except Exception as e:
			print("ERROR: {}".format(e))
		finally:
			myfile.close()
			return True  # Keep listening
	
if __name__ == '__main__':
	print("Mineria de la Web 2017")

	# Get an API item using tweepy
	auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
	api = tweepy.API(auth)  # Build an API object.

	newpid = os.fork()
	if newpid==0:
		# Connect to the stream
		myStreamListener1 = MyStreamListener()
		myStream1 = tweepy.Stream(auth=api.auth, listener=myStreamListener1)

		print(">> Listening to tweets")
		myStream1.filter(track=['futbol','justicia','macri'],languages=["es"],async=True)
	else:
		time.sleep(45)
		os.kill(newpid, signal.SIGTERM)
		alex.AnalizadorLexico()
		
	#End
	#print("El programa finalizo Correctamente")
