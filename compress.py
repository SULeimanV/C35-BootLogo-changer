import gzip
import shutil

with open('4.bmp', 'rb') as f_in:
    with gzip.open('4.bmp.gz', 'wb', compresslevel=9) as f_out:
        shutil.copyfileobj(f_in, f_out)

filePath= "logo.bin"
file = open(filePath, "rb")

byte = bytearray(file.read())
logos = [] 
byteo = []
onames = [] 

def get_names(i) :
	buff=[] 
	g = int.from_bytes(logos[0][::-1])
	go = g

	buff.append(str(byteo[48+10:48+11], encoding='ASCII'))
	#with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.gz", "wb") as logo_gz:
	#	logo_gz.write(byte[48:48+g])

	#	with open(f"{str(byte[48+10:48+11],encoding='ASCII')}.bmp", "wb") as i_out_file:
	#		i_out_file.write(gzip.decompress(byte[48:48+g]))

	for ii in range(1,i+1):
		g+=int.from_bytes(logos[ii][::-1])
		buff.append(str(byte[48+10+go:48+11+go],encoding='ASCII'))
		#with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.gz", "wb") as logo_gz:
		#	logo_gz.write(byte[48+go:48+g])

		#	with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.bmp", "wb") as i_out_file:
		#		i_out_file.write(gzip.decompress(byte[48+go:48+g]))
		go = g
	return buff


def write_bytes(i):
	byte[48:]=[]
	pass
	g=0
	compr_out = b""

	with open(f"{onames[0]}.bmp", "rb") as f_in:
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
		with open(f"{onames[i]}.bmp", "rb") as f_in:
			compr_out = gzip.compress(f_in.read())
			logos[ii]= len(compr_out).to_bytes(2)[::-1]
		

		logos[ii] = len(compr_out).to_bytes(2)[::-1]
		g+=int.from_bytes(logos[ii][::-1])

		byte[48+go:48+g] = bytearray(compr_out) 
		#with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.gz", "wb") as logo_gz:
		#	logo_gz.write(byte[48+go:48+g])

		#	with open(f"{str(byte[48+10+go:48+11+go],encoding='ASCII')}.bmp", "wb") as i_out_file:
		#		i_out_file.write(gzip.decompress(byte[48+go:48+g]))
		go = g

def write_lens(i):
	pass
	for i in range(6):
		byte[24+i*4:26+i*4] = logos[i] 


try:
	if byte[0:3] == b'GZ\x06':
		print("logo bin header found")
	else:
		raise NameError("Header not found")
	
	for i in range(6):
		logos.append(byte[24+i*4:26+i*4]) #Sizes

	byteo = byte

	onames = get_names(5) 
		
	write_bytes(5)

	write_lens(5) 
	
	print("Succesfully extracted!")

	#print("Extracting logos from gzips")

	#with

except NameError:
	print('An exception flew by!')
	file.close()
	raise

file.close()

with open("custom_logo.bin", "wb") as lb_out:
	lb_out.write(byte)

print("Succesful compressed!") 
