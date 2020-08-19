import cv2



face_detector = cv2.CascadeClassifier('Face.xml')
smile_detector = cv2.CascadeClassifier('Smile.xml')
webcam = cv2.VideoCapture(0)

while True:
	successful_frame_read,frame = webcam.read()
	if not successful_frame_read:
		break

	frame_grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(frame_grayscale)
	

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(100,200,50),4)
		the_face = frame[y:y+h,x:x+w]
		
		face_grayscale = cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)
		smiles = smile_detector.detectMultiScale(face_grayscale,1.7,20)

		#for (x_,y_,w_,h_) in smiles:
		#	cv2.rectangle(the_face,(x_,y_),(x_+w_,y_+h_),(50,50,200),4)

		if len(smiles)>0:
			cv2.putText(frame,'Smiling',(x,y+h+40),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))
	cv2.imshow('Why so Serious?',frame)
	cv2.waitKey(1)

webcam.release()
cv2.destroyAllWindows()

print("Code Completed" )