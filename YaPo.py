import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServiceToken': '76565712'}

with open('config.ini', 'w') as configfile:
        config.write(configfile)

operator = input( "Operator: " )
version = "0.12"
setup = "Installation, please wait..."
setup_done = "Installation completed successfully!"
error = "Error! (Contact the official VK group)"
cancel = "Canceling the installation!"

if operator == "help":
        print("List of commands: ")
        print("1. Print")
        print("2. Math")
        print("3. -v")
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
	print("v"+version)


