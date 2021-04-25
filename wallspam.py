import amino
import os
#SirLez
#wallspam
#i see u
os.system("clear")
print ("\033[0;42m _   _       ___   _           ___  ")
print ("\033[0;42m| | | |     /   | | |         /   | ")
print ("\033[0;42m| |_| |    / /| | | |        / /| | ")
print ("\033[0;42m|  _  |   / / | | | |       / / | | ")
print ("\033[0;42m| | | |  / /  | | | |___   / /  | | ")
print ("\033[0;42m|_| |_| /_/   |_| |_____| /_/   |_| ")
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
	try:
		email=input("\033[1;34m┌──\033[0;32m(\033[0;34mENTER YOUR💀\033[1;35mEmail\033[0;32m)-[~]\n\033[1;34m└─>> ")
		password=input("\033[1;34m┌──\033[0;32m(\033[0;34mENTER YOUR💀\033[1;35mPASSWORD\033[0;32m)-[~]\n\033[1;34m└─>> ")
		client.login(email=email,password=password)
		tst=True
	except:
			tst=False
			print("\n# Verify ur account! \n")
			exx=input("# continue?\033[1;32m y/n : \033[1;0m")
			if exx=='N' or exx=='n' or exx=='no':
					os._exit(1)


os.system("clear")
print ("\033[0;42m _   _       ___   _           ___  ")
print ("\033[0;42m| | | |     /   | | |         /   | ")
print ("\033[0;42m| |_| |    / /| | | |        / /| | ")
print ("\033[0;42m|  _  |   / / | | | |       / / | | ")
print ("\033[0;42m| | | |  / /  | | | |___   / /  | | ")
print ("\033[0;42m|_| |_| /_/   |_| |_____| /_/   |_| ")
infoos=input("\033[1;34m┌──\033[0;32m(\033[0;34mENTER THE💀\033[1;35mUser url\033[0;32m)-[~]\n\033[1;34m└─>> ")
infoo=client.get_from_code(infoos)
comId=infoo.path[1:infoo.path.index("/")]
subclient = amino.SubClient(comId=comId,profile=client.profile)
uid=subclient.get_from_code(infoos).objectId
os.system("clear")
print ("\033[0;42m _   _       ___   _           ___  ")
print ("\033[0;42m| | | |     /   | | |         /   | ")
print ("\033[0;42m| |_| |    / /| | | |        / /| | ")
print ("\033[0;42m|  _  |   / / | | | |       / / | | ")
print ("\033[0;42m| | | |  / /  | | | |___   / /  | | ")
print ("\033[0;42m|_| |_| /_/   |_| |_____| /_/   |_| ")
cmn=input("\033[1;33m# Type a comment : \033[1;0m")
os.system("clear")
n=0
k = True
while k is True:
	try:
		subclient.comment(message=cmn,userId=uid)
		n=n+1
		print("\033[1;33m",n,"- ""\033[1;32mdone")
	except:
		pass
