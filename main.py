import binascii

filePath= "logo.bin"
file = open(filePath, "rb")

#byte = file.read(48)

#hexadecimal = binascii.hexlify(byte)

'''
for i in byte:
	if i == bytes(b"47"):
		print("yes")
	print(hex(i))
print(hexadecimal)

s hex dec

G  47  71
Z  5a  90
.  06  6

1f 31
8b 139
08 8

3a-58


10 bytes to name start
'''

#print(byte[(48+int.from_bytes(logos[0][::-1])+int.from_bytes(logos[1][::-1])+10):(48+int.from_bytes(logos[0][::-1])+int.from_bytes(logos[1][::-1])+11)])

def get_bytes(i):  # b   до 5
	#go = []
	#go=0
	g = int.from_bytes(logos[0][::-1])
	go = g
	with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.gz", "wb") as logo_gz:
		logo_gz.write(byte[48:48+g])
	for ii in range(1,i+1):
		print(g,"-1")
		g+=int.from_bytes(logos[ii][::-1])
		print(g,"-2")
		print(byte[48+10+go:48+11+go], "-3")
		#go.append(g)
		print(byte[48+10+go:48+11+go], "-3")
		print(go)
		with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.gz", "wb") as logo_gz:
			logo_gz.write(byte[48+go:48+g])
		go = g
	return g


print("Start scanning!")

byte = bytearray(file.read())
#print(byte[0:3] == b"\x47\x5a\x06")
#print(byte)
logos = []

try:
	if byte[0:3] == b'GZ\x06':
		print("logo bin header found")
	else:
		raise NameError("Header not found")
	
	#for i in range(24,48):
	#	print(byte[i:i+1] == b'\x17')
	for i in range(6):
		logos.append(byte[24+i*4:26+i*4])
	#print(logos)
	#with open("1.gz", "wb") as logo_gz:
		#logo_gz.write(byte[48:48+int.from_bytes(logos[0][::-1])])
	get_bytes(5)


except NameError:
	print('An exception flew by!')
	file.close()
	raise

a = b"\x16\x1d"
print(byte[48+10:48+11])

print(byte[(48+int.from_bytes(logos[0][::-1])+int.from_bytes(logos[1][::-1])+10):(48+int.from_bytes(logos[0][::-1])+int.from_bytes(logos[1][::-1])+11)])






print(int.from_bytes(b"\x1d\x16"))
print(int(255).to_bytes())
print(int.from_bytes(a))
print(a[::-1])
print(byte[48:48+16])

file.close()