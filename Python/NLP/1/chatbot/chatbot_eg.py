from chatterbot.trainers import ListTrainer			#method to train chatbot
from chatterbot import ChatBot 						#import chatbot
import os
from os import listdir

bot=ChatBot('test')					#create the chatbot
bot.set_trainer(ListTrainer)		#set the trainer


chats=open(r"C:\Users\I353296\Documents\git VS\python\Python\NLP\1\chatbot\chats.txt","r").readlines()		#read the file
bot.train(chats)		#TRAIN THE BOT

"""
for file in listdir('files'):			#when there are multiple files to read from
	chats=open('files/' , 'r').readlines()
	bot.train(chats)		#TRAIN THE BOT

while True:
	request=input('You: ')
	response=bot.get_response(request)
	print('Bot: ' +response)
"""

#i=True
#while i==True:
	#print('Bot: ' +str(bot.get_response(input('You: '))))		#on line statement
	#i=False
request=input()
if request != '':
    response=bot.get_response(request)
    print('Bot: ' +str(response))