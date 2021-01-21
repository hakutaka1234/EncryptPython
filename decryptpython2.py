import time
print ('|\33[31;1mNew VIP')
time.sleep(2)
print ('|\33[0;36mLoading..\n')
print ('\33[31;1mUsername = \33[0;36ma \33[31;1mPassword = \33[0;36ma ')
time.sleep(2)
user = raw_input('\33[1;33mUsername: ')

import getpass

sandi = getpass.getpass()

if sandi == 'a' and user == 'a':

    print ('\33[1;33mAnda \33[37;1mTelah \33[0;36mLogin')
    time.sleep(3)
else:
 
  print ('\33[31;1mMasukan \33[37;1mPassword \33[31;1mDengan \33[37;1mBenar')
  time.sleep(2)   
  exit()
import os
file = open(raw_input('\33[31;1mMasukan File Yang Mau Di Decrypt\n\33[0;36mContoh /sdcard/dec.py \n\33[36;1mMasukan File : \33[32;1m')).read()
percobaan = 0
while True:
	if 'exec' in file and 'marshal' in file and 'import' in file:
		root = file.replace('exec', 'x = ')
		percobaan +=1
		print file#('percobaan ke ' + str(percobaan))
	else:
		print('\n' +file)
		try:
			os.remove('haku.py')
			print('\n File tersimpan di compile.py')
		except:
			print('\n Gagal')
		break
	sc = '''from sys import stdout
import marshal
from uncompyle6.main import decompile
'''+root+'''
decompile(2.7,x, stdout) '''
        open('haku.py','w').write(sc)
        os.system('python2 haku.py > compile.py')
        file = open('compile.py').read()
