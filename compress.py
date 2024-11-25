import gzip
import shutil

with open('4.bmp', 'rb') as f_in:
    with gzip.open('4.bmp.gz', 'wb', compresslevel=9) as f_out:
        shutil.copyfileobj(f_in, f_out)

filePath= "logo.bin"
file = open(filePath, "rb")

byte = bytearray(file.read())
logos = []

def write_bytes(i):
	byte[48:]=[]
	pass
	g=0
	compr_out = b""

	with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.bmp", "rb") as f_in:
		compr_out = gzip.compress(f_in.read())t
		logos[0]= len(compr_out).to_bytes(2)[::-1]

	g = int.from_bytes(logos[0][::-1])

	byte[48:48+g] = bytearray(compr_out) 

	#g = int.from_bytes(logos[0][::-1])
	go = g

	

#	with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.gz", "wb") as logo_gz:
#		logo_gz.write(byte[48:48+g])

#		with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.bmp", "wb") as i_out_file:
#			i_out_file.write(gzip.decompress(byte[48:48+g]))

	for ii in range(1,i+1):
		with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.bmp", "rb") as f_in:
			compr_out = gzip.compress(f_in.read())t
			logos[ii]= len(compr_out).to_bytes(2)[::-1]

		logos[ii] = len()
		g+=int.from_bytes(logos[ii][::-1])
		with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.gz", "wb") as logo_gz:
			logo_gz.write(byte[48+go:48+g])

			with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.bmp", "wb") as i_out_file:
				i_out_file.write(gzip.decompress(byte[48+go:48+g]))
		go = g




try:
	if byte[0:3] == b'GZ\x06':
		print("logo bin header found")
	else:
		raise NameError("Header not found")
	
	#for i in range(6):
	#	logos.append(byte[24+i*4:26+i*4]) #Sizes
		
	write_bytes(5)
	
	print("Succesfully extracted!")

	#print("Extracting logos from gzips")

	#with

except NameError:
	print('An exception flew by!')
	file.close()
	raise


file.close()
