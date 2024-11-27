import gzip
import shutil

filePath= "logo.bin"
file = open(filePath, "rb")

byte = bytearray(file.read())
logos = []
oblen = len(byte)
onames = []

def get_names(i) :
	buff=[]
	g = int.from_bytes(logos[0][::-1])
	go = g

	buff.append(str(byte[48+10:48+11], encoding='ASCII'))

	for ii in range(1,i+1):
		g+=int.from_bytes(logos[ii][::-1])
		buff.append(str(byte[48+10+go:48+11+go],encoding='ASCII'))
		go = g
	print(buff)
	return buff


def write_bytes(i):
	byte[48:]=[]
	pass
	g=0
	compr_out = b""
	with open(f'{onames[0]}.bmp', 'rb') as f_in:
		with gzip.open(f'{onames[0]}.bmp.gz', 'wb', compresslevel=9) as f_out:
			shutil.copyfileobj(f_in, f_out)
	with open(f"{onames[0]}.bmp.gz", "rb") as f_in:
		compr_out = f_in.read()
		logos[0]= len(compr_out).to_bytes(2)[::-1]

	g = int.from_bytes(logos[0][::-1])

	byte[48:] = bytearray(compr_out)

	go = g



	for ii in range(1,i+1):
		with open(f"{onames[ii]}.bmp", "rb") as f_in:

			with gzip.open(f'{onames[ii]}.bmp.gz', 'wb', compresslevel=9) as f_out:
                        	shutil.copyfileobj(f_in, f_out)

		with open(f"{onames[ii]}.bmp.gz", "rb") as f_in:
			compr_out = f_in.read()
			logos[ii] = len(compr_out).to_bytes(2)[::-1]

		g+=int.from_bytes(logos[ii][::-1])

		byte[48+go:] = bytearray(compr_out)

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



	onames = get_names(5)

	write_bytes(5)

	write_lens(5)

	print("Succesfully extracted!")


except NameError:
	print('An exception flew by!')
	file.close()
	raise

file.close()

print(oblen,len(byte))

if oblen > len(byte):
	byte[len(byte):] = bytearray(oblen - len(byte))
else:
	with open("new_logo_greater.txt", "w") as nlg:
		nlg.write(f"Warning!\norig: {len(byteo)}\nnew: {len(byte)}")


with open("custom_logo.bin", "wb") as lb_out:
	lb_out.write(byte)

print("Succesful compressed!") 