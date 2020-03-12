import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time


##Error screen2
def del_sc2():
    sc2.destroy()
def err_screen1():
    global sc2
    sc2 = tk.Tk()
    sc2.geometry('300x100')
    sc2.iconbitmap('FRAMS.ico')
    sc2.title('Warning!!')
    sc2.configure(background='snow')
    Label(sc2,text='Please enter your subject name!!!',fg='red',bg='white',font=('times', 16, ' bold ')).pack()
    Button(sc2,text='OK',command=del_sc2,fg="black"  ,bg="lawn green"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)

def Fillattendances():
    sub = tx.get()
    now = time.time()  ###For calculate seconds of video
    future = now + 20
    if time.time() < future:
        if sub == '':
            err_screen1()
        else:
            recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
            try:
                recognizer.read("TrainingImageLabel\Trainner.yml")
            except:
                e = 'Model not found,Please train model'
                Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=20, y=250)

            harcascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath)
            df = pd.read_csv("StudentDetails\StudentDetails.csv")
            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names = ['Enrollment', 'Name', 'Date', 'Time']
            attendance = pd.DataFrame(columns=col_names)
            while True:
                ret, im = cam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                for (x, y, w, h) in faces:
                    global Id

                    Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                    if (conf < 70):
                        print(conf)
                        global Subject
                        global aa
                        global date
                        global timeStamp
                        Subject = tx.get()
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        aa = df.loc[df['Enrollment'] == Id]['Name'].values
                        global tt
                        tt = str(Id) + "-" + aa
                        En = '15624031' + str(Id)
                        attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                        cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4)

                    else:
                        Id = 'Unknown'
                        tt = str(Id)
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                        cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                if time.time() > future:
                    break

                attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                cv2.imshow('Filling attedance..', im)
                key = cv2.waitKey(30) & 0xff
                if key == 27:
                    break

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour, Minute, Second = timeStamp.split(":")
            fileName = "Attendance/" + Subject + "_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
            attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
            print(attendance)
            attendance.to_csv(fileName, index=False)

            M = 'Attendance filled Successfully'
            Notifica.configure(text=M, bg="Green", fg="white", width=33, font=('times', 15, 'bold'))
            Notifica.place(x=20, y=250)
            cam.release()
            cv2.destroyAllWindows()

            import csv
            import tkinter
            root = tkinter.Tk()
            root.title("Attendance of " + Subject)
            root.configure(background='snow')
            cs = './' + fileName
            with open(cs, newline="") as file:
                reader = csv.reader(file)
                r = 0
                for col in reader:
                    c = 0
                    for row in col:
                        # i've added some styling
                        label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                                  bg="lawn green", text=row, relief=tkinter.RIDGE)
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1
            root.mainloop()
            print(attendance)


if __name__ == '__main__':

    ###windo is frame for subject choosing
    windo = tk.Tk()
    windo.iconbitmap('FRAMS.ico')
    windo.title("Enter subject name...")
    windo.geometry('580x320')
    windo.configure(background='snow')
    Notifica = tk.Label(windo, text="Attendance filled Successfully", bg="Green", fg="white", width=33,
                        height=2, font=('times', 15, 'bold'))


    def Attf():
        import subprocess
        subprocess.Popen(
            r'explorer /select,".\Attendance\Manually Attendance\"')  # open attendance sheet window


    attf = tk.Button(windo, text="Check Sheets", command=Attf, fg="black", bg="lawn green", width=12, height=1,
                     activebackground="Red", font=('times', 14, ' bold '))
    attf.place(x=430, y=255)

    sub = tk.Label(windo, text="Enter Subject", width=15, height=2, fg="white", bg="blue2",
                   font=('times', 15, ' bold '))
    sub.place(x=30, y=100)

    tx = tk.Entry(windo, width=20, bg="yellow", fg="red", font=('times', 23, ' bold '))
    tx.place(x=250, y=105)

    fill_a = tk.Button(windo, text="Fill Attendance", fg="white", command=Fillattendances, bg="deep pink", width=20,
                       height=2,
                       activebackground="Red", font=('times', 15, ' bold '))
    fill_a.place(x=250, y=160)
    windo.mainloop()