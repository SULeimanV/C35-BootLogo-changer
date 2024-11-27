import gzip

filePath= "logo.bin"  #our logo.bin

file = open(filePath, "rb")


def get_bytes(i):
	g = int.from_bytes(logos[0][::-1])
	go = g

	with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.bmp.gz", "wb") as logo_gz:
		logo_gz.write(byte[48:48+g])

		with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.bmp", "wb") as i_out_file:
			i_out_file.write(gzip.decompress(byte[48:48+g]))

	for ii in range(1,i+1):
		g+=int.from_bytes(logos[ii][::-1])
		with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.bmp.gz", "wb") as logo_gz:
			logo_gz.write(byte[48+go:48+g])

			with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.bmp", "wb") as i_out_file:
				i_out_file.write(gzip.decompress(byte[48+go:48+g]))
		go = g


print("Start scanning!")

byte = bytearray(file.read())
logos = []

try:
	if byte[0:2] == b'GZ':
		print("logo bin header found")
	else:
		raise NameError("Header not found")

	logos_count = int.from_bytes(byte[2])

	for i in range(logos_count):
		logos.append(byte[24+i*4:27+i*4]) #Sizes

	get_bytes(logos_count-1)

	print("Succesfully extracted!")


except NameError:
	print('An exception flew by!')
	file.close()
	raise


file.close()
