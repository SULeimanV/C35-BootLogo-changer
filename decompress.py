import gzip

filePath= "logo.bin"  #our logo.bin

file = open(filePath, "rb")
logos_count = 0
pad = 0


def get_bytes(i):
	g = int.from_bytes(logos[0][::-1])
	go = g

	with open(f"{str(byte[pad+10:pad+11],encoding='ASCII')}.bmp.gz", "wb") as logo_gz:
		logo_gz.write(byte[pad:pad+g])

		with open(f"{str(byte[pad+10:pad+11],encoding='ASCII')}.bmp", "wb") as i_out_file:
			i_out_file.write(gzip.decompress(byte[pad:pad+g]))

	for ii in range(1,i):
		g+=int.from_bytes(logos[ii][::-1])
		with open(f"{str(byte[pad+10+go:pad+11+go],encoding='ASCII')}.bmp.gz", "wb") as logo_gz:
			logo_gz.write(byte[pad+go:pad+g])

			with open(f"{str(byte[pad+10+go:pad+11+go],encoding='ASCII')}.bmp", "wb") as i_out_file:
				i_out_file.write(gzip.decompress(byte[pad+go:pad+g]))
		go = g


print("Start scanning!")

byte = bytearray(file.read())
logos = []

try:
	if byte[0:2] == b'GZ':
		print("logo bin header found")
	else:
		raise NameError("Header not found")

	logos_count = int(byte[2])
	pad = 24 + 4 * logos_count

	for i in range(logos_count):
		logos.append(byte[24+i*4:28+i*4]) #Sizes

	get_bytes(logos_count)

	print("Succesfully extracted!")


except NameError:
	print('An exception flew by!')
	file.close()
	raise


file.close()