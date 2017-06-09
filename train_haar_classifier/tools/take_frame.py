import cv2
vidcap = cv2.VideoCapture('video_name.mov')
success,image = vidcap.read()
name = 1
success = True
while success:
	success,image = vidcap.read()
	if success:
		print (name)
		s = 'pos-' + '{:04d}'.format(name) + '.jpg'
		#flip horizontally
		#image = cv2.flip(image, 0)  
		cv2.imwrite(s, image)     # save frame as JPEG file
		name += 1
