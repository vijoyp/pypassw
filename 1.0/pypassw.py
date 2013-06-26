import random, time
f = open("passwords.txt", "r")
g = list(f)
f.close()
found = False
chars = """abcdefghijklmnopqrstuvwxyz"""
password = raw_input("Enter a password : ")
passlen = len(password)
password = password.replace(' ', '')
print "\nWorking...\nPress 'control+C' to stop\n"
start = time.time() #####START######
for a in g:
	if password == a[:-1]:
		found = True
		break
while found == False:
	i = 0
	curtry = ""
	while i<passlen:
		curtry += random.choice(chars)
		i += 1
	if curtry == password:
		found = True
		break
total = round(time.time() - start , 4) #####STOP######
print "Taken time :",total,"\nPassword was", password
