a=[]
b=[]
c=[]
f=open("stuff", "rb")
while 1:
	byte = f.read(1)
	if byte == b"":
		break
	else:
		a.append(int.from_bytes(byte, byteorder='big'))
f.close()

f=open("stuff2", "rb")
while 1:
	byte = f.read(1)
	if byte == b"":
		break
	else:
		b.append(int.from_bytes(byte, byteorder='big'))
f.close()

f=open("test", "rb")
while 1:
	byte = f.read(1)
	if byte == b"":
		break
	else:
		c.append(int.from_bytes(byte, byteorder='big'))
f.close()

for i in range(0,203):
	a[i]=b[202-i]^(a[i]-1)

d=[]
for i in range(63):
	d.append(c[i]^(i+0x33))

for i in a:
	if len(hex(i)[2:])==1:
		print("\\x0"+hex(i)[2:],end="")
	else:
		print("\\x"+hex(i)[2:],end="")

e=""
for i in range(63):
	if i==52:
		e+=chr((d[i]^0x27)^0x43)
	elif i==47:
		e+=chr((d[i]^0x27)^0x44)
	else:		
		e+=chr(d[i]^0x27)
print("\n")
print(e)