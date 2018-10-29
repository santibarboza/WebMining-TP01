import unicodedata
import json
import codecs
import os
import signal
import time
import alex



import queue
import re
import math
from stopws import stopwords
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def limpiar_Contenido(cadena):
	#elimino los links
	patron=re.compile("\shttp\S+")
	cadena= patron.sub("",cadena)
	#elimino todo lo qe no es una letra o forma parte de un hashtag
	patron=re.compile("[^(\w|\s)]")
	cadena= patron.sub("",cadena)

	#todas las palabras qedan separadas unicamente por espacios
	#elimino las stopwords
	for sw in stopwords:
		cadena=cadena.replace(' '+sw+' ',' ')
		cadena=cadena.replace(' '+sw+'\n','\n')
		cadena=cadena.replace('\n'+sw+' ','\n')
		cadena=cadena.replace(' '+sw.title()+' ',' ')
		cadena=cadena.replace(' '+sw.title()+'\n','\n')
		cadena=cadena.replace('\n'+sw.title()+' ','\n')

	cadena=cadena.replace("\n\n","\n")
	patronLetraAislada=re.compile(" \w ")
	cadena=patronLetraAislada.sub("",cadena)
		
	return cadena

def AnalizadorLexico():
	print("Analizador lexico")
	archivo = open("data.txt", "r")
	contenido = archivo.read()#.lower()
	contenido= 	elimina_tildes(contenido)

	#Limpio el texto
	contenido=limpiar_Contenido(contenido)
	
	#separo todos espacios y armo un cjto de terminos
	terminosconrepeticiones=contenido.split()
	terminos=list(set(terminosconrepeticiones))

	nterm=len(terminos)
	print("cantidad de terminos= ",nterm)
	priority_queue = queue.PriorityQueue(nterm)
		
	freq=[0 for j in range(nterm)]

	for t in range(0,nterm):
		freq[t]=contenido.count(terminos[t])
		if(terminos[t].istitle()):
			freq[t]=freq[t]*2
		priority_queue.put((freq[t], terminos[t]))
		

	for t in range(0,nterm):
		print(priority_queue.get())

	
	print('Finalizo Correctamente')

if __name__ == '__main__':
	AnalizadorLexico()

	

			





