import cv2
import logging
from pathlib import Path
import time

CASCADESFILE = 'data/haarcascades/haarcascade_frontalface_default.xml'
EYESFILE = 'data/haarcascades/haarcascade_smile.xml'
LOGFILE = 'build/faces.log'

Path('build').mkdir(exist_ok=True)
logging.basicConfig(filename=LOGFILE, level='DEBUG')

def main():
# all( (x1 <= x <= x + w <= x1 + w ) and (y1 <= y <= y + h <= y1 + h) for (x1,y1,h1,w1) in faces)
    model = cv2.CascadeClassifier(CASCADESFILE)
    modeleyes = cv2.CascadeClassifier(EYESFILE)
    webcam = cv2.VideoCapture(0)

    # infinite image processing loop
    while True:

        if not webcam.isOpened():
            logging.warning('Unable to connect to camera.')
            time.sleep(5)
            continue

        # get image from camera
        ret, frame = webcam.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # convert image to grayscale
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        # detect faces
        faces = model.detectMultiScale(grayframe, scaleFactor=3.1, minNeighbors=5, minSize=(30, 30))
        eyes = modeleyes.detectMultiScale(grayframe, scaleFactor=3.1, minNeighbors=20, minSize=(40, 40))
        logging.info(f'Detected faces: {len(faces)}')

        # add boxes
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            print(f'Face {bool(list(faces))}: {x} {y} {w} {h}')
        for (x, y, w, h) in eyes:
            if bool(list(faces)):
                if all( (x1 <= x <= x + w <= x1 + w1 ) and (y1 <= y <= y + h <= y1 + h1) for (x1,y1,h1,w1) in faces):
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
          

            print(f'Smile: {x} {y} {w} {h}')

        # show image
        cv2.imshow('Video', frame)

        # stop if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # close everything
    webcam.release()
    cv2.destroyWindows()


if __name__ == '__main__':
    main()
