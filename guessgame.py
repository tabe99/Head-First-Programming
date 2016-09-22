from random import randint 
rando_number = randint(1,10)
guess = 0
while guess != rando_number :
	g=input("Ðoán só : ")
	guess = int(g)
	if guess == rando_number :
		print ("Chien Thang")
	else :
		if guess > rando_number :
			print ("Qua cao")
		else:
			print ("Qua thap")
print ("Game Over")
