import os

i = 1
for file in os.listdir('./'):
	if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.JPG'):	
		os.rename(file, str(i) + '.jpg')
		i = i + 1
