# coding : utf-8

import os
import psutil

def main():

	print('What your name?')
	name = raw_input()
	print("Hello, " + name)

	Answer = raw_input('Prodoljem rabotat? (Y/N)')

	if Answer == 'Y':
		print('Viberite deystvie')
		print('1 - idti domoy')
		print('2 - idti rabotat')
		Deystvie = raw_input('vashe deystvie:')
		if Deystvie == '1':
			print('By, go home')
			print(os.listdir())
		elif Deystvie == '2':
			print('Work is life')
			print(psutil.pids())
		else:
			print('Uooopsss')
	elif Answer == 'N':
		print('good bi')
	else:
		print('error, vveden ne pravelniy simvol')
		

if __name__ == "__main__":
	main()