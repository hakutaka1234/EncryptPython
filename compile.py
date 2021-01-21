from uncompyle6.main import decompile
import marshal, time, sys, os, haku, random, requests, getpass

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


def lisensi():
    os.system('clear')
    mengetik('#####################################')
    mengetik('#### \t</> \x1b[31;1mLICENSE LOGIN \x1b[37;1m</>    ####')
    mengetik('#####################################')
user = raw_input('\33[1;33mUsername: ')

sandi = getpass.getpass()

if sandi == 'a' and user == 'a':

    print ('\33[1;33mAnda \33[37;1mTelah \33[0;36mLogin')
    time.sleep(3)
else:
 
  print ('\33[31;1mMasukan \33[37;1mPassword \33[31;1mDengan \33[37;1mBenar')
  time.sleep(2)   
  exit()
lisensi()

def Py3():
    print 'Decompile haku python3'
    c = raw_input('> File : ')
    print ''
    x = marshal.loads(haku.py3)
    xx = decompile(3.7, x, sys.stdout)
    xxx = '# Python 3.7.x\n# Decompile By Haku\n' + xx.text
    with open(c + '.py', 'w') as (f):
        f.write(xxx)
    print '\n\n[]Saved] file : \x1b[32m%s.py' % c
    print ''


def Py2():
    print 'Decompile haku python2'
    c = raw_input('> File : ')
    print ''
    x = marshal.loads(haku.py2)
    xx = decompile(2.7, x, sys.stdout)
    xxx = '# Python 2.7.x\n# Decompile By Haku\n' + xx.text
    with open(c + '.py', 'w') as (f):
        f.write(xxx)
    print '\n\n[Saved] file : \x1b[32m%s.py' % c
    print ''


try:
    os.system('clear')
    mengetik('#####################################')
    mengetik('#### </> \x1b[31;1mProgram Information \x1b[37;1m</> ####')
    mengetik('#####################################')
    mengetik('- Author       : Hakutaka')
    mengetik('- Name Program : Decompile Marshall 2.7.x And 3.7.x')
    mengetik('- Created Date : 23-09-2019')
    print ''
    if sys.version[0] in '3':
        Py3()
    elif sys.version[0] in '2':
        Py2()
except Exception as F:
    print 'Err: %s' % F