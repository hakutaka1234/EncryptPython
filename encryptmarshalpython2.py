import marshal
inp = raw_input("file yang mau di encrypt: ")
bk = open(inp,"r").read()
cp = compile(bk,"<enc>","exec")
md = marshal.dumps(cp)
open("hasil.py","w").write("import marshal;exec(marshal.loads("+repr(md)+"))")
print "Sukses" , "File save To hasil.py"
