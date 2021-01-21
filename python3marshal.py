import marshal


a=input('file py3 > ')
x=open(a).read()
m=compile(x,'','exec')
k=marshal.dumps(m)
I=open('hasil-'+a,'w')
I.write('import marshal\n')
I.write('exec(marshal.loads( '+repr(k)+'))')
print( 'sucsess')
