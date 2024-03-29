from unicodedata import name
import PySimpleGUI as sg 
import cv2

layout = [
    [sg.Image(key = '-IMAGE-')],
    [sg.Text('Number of people in picture: 0', key='-TEXT-', expand_x=True, justification='c')]
]

window = sg.Window('Face Detector', layout)

video = cv2.VideoCapture(0)#Gets the video
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    event, values = window.read(timeout = 0)
    if event == sg.WIN_CLOSED:
        break

    _, frame = video.read()#Updates the image
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.3, minNeighbors = 7, minSize = (50,50))
    print(faces)
    

    for (x ,y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window['-IMAGE-'].update(data = imgbytes)
    window['-TEXT-'].update(f'Number of people in picture: {len(faces)}')#Updates the number of peoplein img


window.close()
