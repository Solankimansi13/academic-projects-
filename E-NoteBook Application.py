
import datetime # imports the datetime module for show present date and time

import os # imports the os module




def display_menu(): 
	print("\t\tWelcome To Python E-Note\n")
	print("\t\tPress 1 for Generate Note")
	print("\t\tPress 2 for View Note")
	print("\t\tPress 4 for Exit\n\n")
	print("Enter your choice: ") 

'''
when user select option 1 then accept following details from user 
'''

def generate_note():
	print("Enter Python E-Note Generator Name:") 
	generator_name = input()
	while not generator_name:
		print("Invalid input. Please enter a valid name.")
		generator_name = input() 
	
	print("Enter Python E-Note Book Title:")
	title = input()
	while not title:
		print("Invalid input. Please enter a valid title.")
		title = input()
	
	print("Enter E-Note Content:")
	content = input() 
	while not content:
		print("Invalid input. Please enter some content.")
		content = input()
	
	with open("notes.txt", "a") as file:
		file.write(f"-----------\n{datetime.datetime.now()}\nE-Note title: {title}\nE-note Description: {content}\nNote Generator: {generator_name}\n---------------------------\n")
	

	print("Note saved successfully!")#  

def view_note():

	with open("notes.txt", "r") as file:
		print(file.read())

def log_transaction(message):
	with open("log.txt", "a") as file:
		file.write(f"{datetime.datetime.now()}: {message}\n")

def main():
	display_menu()

	while True:
		choice = input()
		if choice == "1":
			generate_note()
			log_transaction("Note generated")
    						
			display_menu()
		elif choice == "2":
			view_note()
    			
			log_transaction("Note viewed")
			display_menu()
		elif choice == "4":
			break
		else:
			print("Invalid choice. Please try again.")
			log_transaction("Invalid choice")
			display_menu()

if __name__ == "__main__":
	main()
  