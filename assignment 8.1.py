#ask user for input (directory and file name)
#validate they exist
#ask user for input (name, address and phone number)
#write this data to file and directory specified by user in comma separated line
#read the file and display contents to user
#while loop that quits with q
while True:
	choice = input("Hello! Press y to begin or q to quit! ")
	if choice == "q":
		print("Goodbye!")
		break
	elif choice == "y":
		file_input = input("Please enter your file name: ")
		directory_input = input("Please enter your directory (No file name and ending with a backslash) : ")

		file_path = directory_input + file_input

		try:
			with open(file_path) as file_object:
				lines = file_object.readlines()
		except FileNotFoundError:
			print(f"Sorry, the file path {file_path} could not be found")
		else:
			name = input("What is your name? ")
			address = input("What is your address? ")
			phone_number = str(input("What is your phone number? "))
			user_input = name + ", " + address + ", " + phone_number + " "
			with open(file_path, 'a') as file_object:
				file_object.write(user_input)
			with open(file_path, 'r') as file_object:
				lines = file_object.readlines()
				for line in lines:
					print(line.rstrip())
	else:
		print("The input was incorrect!")