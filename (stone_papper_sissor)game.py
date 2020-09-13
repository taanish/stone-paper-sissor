import random
print("<==stone papper sissor==>")
print("you only have 10 steps if you won maximum times then you won othervise computer won")
wy = "winner>>>>you"
wc = "winner>>>>computer"
list_1 = [ ]
for i in range(10,0,-1):
	print("\n\nyou have",i,"steps")
	computer = random.choice(['stone','papper','sissor'])
	you = input("enter stone,papper or sissor-")
	if computer == "stone" and you == "papper":
		print("you:",you,"computer:", computer)
		print(wy)
		list_1.append("yw")
	elif computer == "stone" and you == "sissor":
		print("you:",you,"\ncomputer:", computer)
		print(wc)
		list_1.append("cw")
	elif computer == "stone" and you == "stone":
		print("you:",you,"\ncomputer:", computer)
		print(">>>>drow")	
	elif computer == "papper" and you =="papper":
		print("you:",you,"\ncomputer:", computer)
		print(">>>>draw")
	elif computer == "papper" and you == "sissor":
		print("you:",you,"\ncomputer:", computer)
		print(wy)
		list_1.append("yw")
	elif computer == "papper" and you == "stone":
		print("you:",you,"\ncomputer:", computer)		
		print(wc)
		list_1.append("cw")
	elif computer == "sissor" and you == "sissor":
		print("you:",you,"\ncomputer:", computer)
		print(">>>>draw")
	elif computer == "sissor" and you == "stone":
		print("you:",you,"\ncomputer:", computer)	
		print(wy)
		list_1.append("yw")
	elif computer == "sissor" and you == "papper":
		print("you:",you,"\ncomputer:", computer)
		print(wc)
		list_1.append("cw")	
	else:
		print("invalid input check spelling")
		continue	
print("")
print("\t\t\t*******results*******")	
cnt_yw = list_1.count("yw")
cnt_cw = list_1.count("cw")
if cnt_yw > cnt_cw :
	print("\t\t\tcongratulations! you won more time than computer")
	print("\t\t\t<=you won this game=>")
else:
	print("\t\t\tyou lost! computer won more time than you")
	print("\t\t\t<=computer won this game=>")	
		 
		 									
		 																		
		 																											
											
																