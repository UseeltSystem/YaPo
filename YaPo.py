import configparser
import os
import time
import math

config = configparser.ConfigParser()
config['config'] = {'ServiceToken': '76565712'}

with open('config.ini', 'w') as configfile:
        config.write(configfile)

operator = input( "Operator: " )
version = "0.2"
setup = "Installation, please wait..."
setup_done = "Installation completed successfully!"
error = "Error! (Contact the official VK group)"
delete_start = "I'm remove this module!"
delete_done = "I have removed this module!"
not_found = "I didn't find this module!"
have_module = "You already have a module!"
cancel = "Canceling the installation!"

def Math_IO_setup():
	os.mkdir("modules")
	os.mkdir("modules/Math-IO")
	core = open('modules/Math-IO/core.py', 'w')
	core.write("import math\nimport os\nimport time\nimport configparser\n\nconfig = configparser.ConfigParser()\nconfig['config'] = {'SerialToken': '65462344'}\n\nwith open('config.ini', 'w') as configfile:\n        config.write(configfile)")

def YaPo_all():
	Math_IO_setup()

def YaPo_types():
	if o_type == "download":
		download = input("What to download?: ")
		if download == "math-io":
			agree = input("Do you want to download Math-IO? (y/n): ")
			if agree == "y":
				if os.path.isdir("modules/Math-IO") == False:
					print(setup)
					Math_IO_setup()
					time.sleep(1)
					print(setup_done)
				else:
					print(have_module)
			if agree == "n":
				print(cancel)
		if download == "-all":
			agree_all = input("Do you want to download all modules? (y/n): ")
			if agree_all == "y":
				print(setup)
				YaPo_all()
				print(setup_done)
			if agree_all == "n":
				print(cancel)
	if o_type == "remove":
		delete = input("What to remove?: ")
		if delete == "math-io":
			del_agree = input("Do you want to remove Math-IO? (y/n): ")
			if del_agree == "y":
				if os.path.isdir("modules/Math-IO") == True:
					print(delete_start)
					os.remove("modules/Math-IO/core.py")
					os.removedirs("modules/Math-IO")
					time.sleep(1)
					print(delete_done)
				else:
					print(not_found)
			if del_agree == "n":
				print(cancel)
if operator == "math-io":
	if os.path.isdir("modules/Math-IO") == True:
		moper = input("Math-IO Operator: ")
		if moper == "sqrt":
			sqrt_num = int(input("The number from which to extract the root: "))
			sqrt = math.sqrt(sqrt_num)
			print(f"Math-IO Result: {sqrt}")
		if moper == "abs":
			abs_num = int(input("The number whose module to search for: "))
			abs_result = abs(abs_num)
			print(f"Math-IO Result: {abs_result}")
		if moper == "phd":
			phd_1 = int(input("Number: "))
			phd_2 = int(input("To what extent?: "))
			print(f"{phd_1**phd_2}")
if operator == "YaPo":
	o_type = input("Type: ")
	YaPo_types()
if operator == "help":
        print("List of commands: ")
        print("1. Print")
        print("2. Math")
        print("3. YaPo")
        print("4. -v")
        if os.path.isdir("modules/Math-IO") == True:
        	print("5. Math-IO")
        print("The list of commands will be supplemented")
if operator == "print":
	inside = input( "Inside: " )
	print(inside)
if operator == "math":
	a = float(input( "The First Value: " ) )
	b = float(input( "Second Value: " ) )
	math = input( "Operator math: " )

	if math == "-":
		result = a - b
		print("Math Result: " + str(result) )
	if math == "+":
		result = a + b
		print("Math Result: " + str(result) )
	if math == "*":
		result = a * b
		print("Math Result: " + str(result) )
	if math == "/":
		result = a / b
		print("Math Result: " + str(result) )
if operator == "-v":
	print(f"v{version}")


