import face_recognition
import cv2
import numpy as np
import os
import glob
from getpass import getuser

def recognize(username):
    video_capture = cv2.VideoCapture(0)

    known_face_encodings = []
    known_face_names = []
    dirname = os.path.dirname(__file__)
    path = os.getcwd() + '/system/Library/Security/Face/known_people/'

    list_of_files = [f for f in glob.glob(path+'*.jpg')]
    number_files = len(list_of_files)

    names = list_of_files.copy()

    for i in range(number_files):
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
        known_face_encodings.append(globals()['image_encoding_{}'.format(i)])

        names[i] = names[i].replace("known_people/", "")  
        known_face_names.append(names[i])

    face_locations = []
    face_encodings = []
    face_names = []
    recognized = []
    process_this_frame = True

    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                filename = os.path.basename(name)
                name = filename
                base = os.path.basename(name)
                filename = os.path.splitext(base)[0]
                if filename == username:
                    return True
                else:
                    return False
                    pass

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 128, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 128, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    video_capture.release()
    cv2.destroyAllWindows()

def setup():
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()
    img_name = os.getcwd() + '/system/Library/Security/Face/known_people/default.jpg'
    cv2.imwrite(img_name, frame)

    cam.release()