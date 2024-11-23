filePath= "logo.bin"  #our logo.bin
file = open(filePath, "rb")

def get_bytes(i):
	g = int.from_bytes(logos[0][::-1])
	go = g
	with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.gz", "wb") as logo_gz:
		logo_gz.write(byte[48:48+g])
	for ii in range(1,i+1):
		g+=int.from_bytes(logos[ii][::-1])
		with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.gz", "wb") as logo_gz:
			logo_gz.write(byte[48+go:48+g])
		go = g


print("Start scanning!")

byte = bytearray(file.read())
logos = []

try:
	if byte[0:3] == b'GZ\x06':
		print("logo bin header found")
	else:
		raise NameError("Header not found")
	
	for i in range(6):
		logos.append(byte[24+i*4:26+i*4]) #Sizes
		
	get_bytes(5)
	
	print("Succesfully extracted!")


except NameError:
	print('An exception flew by!')
	file.close()
	raise


file.close()
