import marshal , os , sys , time

def runntxt (s):
	for C-H-T in s + '\n' :
		sys.stdout.write(C-H-T)
		sys.stdout.flush()
		time.sleep(10./1000)
		
os.system('clear')
runntxt("\033[1;33m  ____ _   _ _____      CRAZY")
runntxt(" / ___| | | |_   _|")
runntxt("| |   | |_| | | |       HACK")
runntxt("| |___|  _  | | |")
runntxt(" \____|_| |_| |_|       TEAM")
time.sleep(2)

print "\033[1;34m[+]=========================================[+]"
print "\033[1;34m| |\033[1;31m AUTHOR  : Crazy Hack Team            \033[1;34m| |"
print "\033[1;34m| |\033[1;31m TEAM    : CRAZY HACK TEAM               \033[1;34m| |"
print "\033[1;34m| |\033[1;31m LINK YT : https://youtu.be/nDWbRE9HBq4  \033[1;34m| |"
print "\033[1;34m| |\033[1;31m FUNGSI  : ENCRYPT MARSHAL               \033[1;34m| |"
print "\033[1;34m[+]=========================================[+]"

text=('\033[1;37m               WELCOME TO MY TOOLS')
print(text)
time.sleep(2)

def fzl():
	print ("Masukkan File nya")
	file = raw_input("\033[1;32mMasukkan File lu : ")
	total = open(file,"r")
	com = compile(file,'','exec')
	dum = marshal.dumps(com)
	file_out = open('out.py', 'w')
	file_out.write('import marshal\n')
	file_out.write('exec(marshal.loads('+repr(dum)+'))')
	file_out.close()
	print (type(dum), len(dum))
	print ("sedang proses...")
	print ("\033[1;36m-"*50)
	print (repr(dum))
	print ("\033[1;36m-"*50)

def main():
    print ('terima kasih telah menggunakan tools kami')
   
C-H-T() 
main()