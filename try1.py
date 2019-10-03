# https://www.youtube.com/watch?v=-spZx-XoES8

import random

greeting_words = ['hello', 'hi', 'hey', 'ssup', 'greetings']

greeting_response = ["Hi, how are you?", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

# def response_check(sentence):
# 	for word in sentence.split():
# 		if word.lower() in 

def check_for_greetings(sentence):
	for word in sentence.split():
		if word.lower() in greeting_words:
			return random.choice(greeting_response)
		else:
			return "What are you saying?"

while True:
	sentence = input("You : ")
	response = check_for_greetings(sentence)
	print('Bot : '+ response)

	if 'bye' in sentence:
		print("Alright, bye bye!!")
		break