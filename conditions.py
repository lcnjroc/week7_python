print("Rules that govern the state of water")

current_temp= false

while current_temp is false
	current_temp= input("Enter a temperature \n")
	print(current_temp)

	if(int(current_temp) < 0) or (int(current_temp== 0)):
		print("water is a solid. icy!")
		current_temp= false

	elif(int(current_temp) < 100):
		print("water is a liquid. profit!")
		current_temp= false

	elif(int(current_temp) > 100) or (int(current_temp== 100)):
		print("water is a vapor. drop it like it's hot!")
		current_temp= false
		