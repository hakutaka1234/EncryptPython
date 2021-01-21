import random,sys,logging

logging.basicConfig(level=logging.INFO)
__banner__="""
\t[ obfucaste by hakutaka ]\n"""
def main(files,string):
        s=open(files).read()
        z=[]
        for i in s:
                z.append(ord(i))
        pea=[]
        for i in z:
                pea.append(string.replace("'","").replace('"','')*i)
        file="""
# coding=utf-8
# obfuscated with plusobf: https://github.com/hakutaka1234/EncryptPython



d={};exec("".join([chr(len(i)) for i in d]))
        """.format(pea)
        open(files.replace(".py","encypt.py"),"w").write(file)
        logging.info(" saved as "+files.replace(".py","encrypt.py"))

try:
        print(__banner__)
        logging.info(" obfuscating "+sys.argv[1]+" ...")
        main(sys.argv[1],sys.argv[2])
except:
        print("""

[!] \033[31;1mCara Menggunakan : obfucaste.py <filename> 'string'
Contoh:
        python obfucaste.py scriptku.py '+'
""")