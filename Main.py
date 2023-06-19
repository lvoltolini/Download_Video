# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.9

import Module # Check the installed packages and show in the command prompt

import os # Check dir_path and create a "Videos" folder.
from pytube import YouTube # Importa la classe "YouTube" dal modulo "pytube"
from moviepy.video.io.VideoFileClip import VideoFileClip # Importa la classe "VideoFileClip" dal modulo "moviepy.video.io.VideoFileClip"
import Python_image_rc

# Importa le classi necessarie da "PyQt5"
from PyQt5 import QtCore, QtGui, QtWidgets

dir_path = os.path.dirname(os.path.abspath(__file__))

# Imposta la directory di lavoro corrente sulla directory che contiene lo script principale
os.chdir(dir_path)

# Crea la cartella per salvare il film.
path = os.getcwd() + '//Videos//'
if not os.path.exists(path):
        os.makedirs(path)
        

def convert_time_to_seconds(min, sec): # FUNZIONE DEPRECATA
        # Converte il tempo da minuti e secondi a secondi
        correct_rime = min*60 + sec
        return correct_rime

def check_path_exist(path):
        if os.path.exists(path):
                print(f"{path} already exists.")
                return True

def segment_video(video, start_time, end_time, mp4_name):
        if start_time < end_time:
                # Estrae il segmento di video specificato
                segmento = video.subclip(start_time, end_time)

                # Salva il segmento di video
                segment_path = f"{os.getcwd()}//Videos//segment_{mp4_name}"
                if check_path_exist(segment_path):
                        return
                segmento.write_videofile(segment_path, codec="libx264")
      
def download(url, start_time, end_time, filename):

        print('start:', start_time, 'end:', end_time)
        
        # Crea un oggetto YouTube usando l'URL fornito
        yt = YouTube(url)

        # Scarica il video con la qualità progressiva e l'estensione mp4
        video_path = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

        # Rinomina il file video scaricato
        mp4_name = f"Video_{filename}.mp4"
        mp4_dir = f"{os.getcwd()}//Videos//"
        if check_path_exist(mp4_dir + mp4_name):
                return
        os.rename(video_path, mp4_dir + mp4_name)
        
        # Carica il video utilizzando la classe VideoFileClip
        video = VideoFileClip(mp4_dir + mp4_name)
        
        # Segmenta il video quando si è verificato che start_time < end_time
        segment_video(video, start_time, end_time, mp4_name)

        # if start_time < end_time:
        #         # Estrae il segmento di video specificato
        #         segmento = video.subclip(start_time, end_time)

        #         # Salva il segmento di video
        #         segment_path = f"{os.getcwd()}//Videos//segment_{mp4_name}"
        #         if check_path_exist(segment_path):
        #                 return
        #         segmento.write_videofile(segment_path, codec="libx264")

    
class Ui_MainWindow(object):
        
        def on_download_clicked(self):
                url = self.input_insert_url.toPlainText()
                filename = self.input_video_filename.toPlainText()
                
                # start
                start_min = self.input_insert_start_time.time().minute()
                start_sec = self.input_insert_start_time.time().second()
                start_time = 60*start_min + start_sec
                
                #end
                end_min = self.input_insert_end_time.time().minute()
                end_sec = self.input_insert_end_time.time().second()
                end_time = 60*end_min + end_sec
                
                download(url, start_time, end_time, filename)
                
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(620, 667)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                '# CHECKBOXES: ' 
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                
                # Check if download is needed:
                self.checkbox_download = QtWidgets.QCheckBox(self.centralwidget)
                self.checkbox_download.setGeometry(QtCore.QRect(20, 190, 121, 31))
                self.checkbox_download.setProperty("allow_download", False)
                self.checkbox_download.setObjectName("checkbox_download")
                
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                '# BUTTON: ' 
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                
                # Download Button:
                self.pushButton_download_edit = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_download_edit.setGeometry(QtCore.QRect(300, 280, 141, 51))
                self.pushButton_download_edit.setProperty("start_download", False)
                self.pushButton_download_edit.setObjectName("pushButton_download_edit")
                self.pushButton_download_edit.clicked.connect(self.on_download_clicked)
                
                self.Python_View = QtWidgets.QGraphicsView(self.centralwidget)
                self.Python_View.setGeometry(QtCore.QRect(10, 10, 600, 150))
                self.Python_View.setObjectName("Python_View")
                
                # Edit Button:
                self.pushButton_edit_segment = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_edit_segment.setGeometry(QtCore.QRect(460, 280, 141, 51))
                self.pushButton_edit_segment.setProperty("start_editing", False)
                self.pushButton_edit_segment.setObjectName("pushButton_edit_segment")
                
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                '# INSERTS: ' 
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                
                # URL and Filename:
                self.input_insert_url = QtWidgets.QTextEdit(self.centralwidget)
                self.input_insert_url.setGeometry(QtCore.QRect(160, 190, 441, 31))
                self.input_insert_url.setFrameShape(QtWidgets.QFrame.WinPanel)
                self.input_insert_url.setProperty("video_url", "")
                self.input_insert_url.setObjectName("input_insert_url")
                
                self.input_video_filename = QtWidgets.QTextEdit(self.centralwidget)
                self.input_video_filename.setGeometry(QtCore.QRect(160, 230, 441, 31))
                self.input_video_filename.setFrameShape(QtWidgets.QFrame.WinPanel)
                self.input_video_filename.setProperty("video_filename", "")
                self.input_video_filename.setObjectName("input_video_filename")
                
                # Start-End Time:
                self.input_insert_start_time = QtWidgets.QTimeEdit(self.centralwidget)
                self.input_insert_start_time.setGeometry(QtCore.QRect(160, 280, 118, 22))
                self.input_insert_start_time.setObjectName("input_insert_start_time")
                
                self.input_insert_end_time = QtWidgets.QTimeEdit(self.centralwidget)
                self.input_insert_end_time.setGeometry(QtCore.QRect(160, 310, 118, 22))
                self.input_insert_end_time.setObjectName("input_insert_end_time")
                
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                '# DESENHOS: ' 
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                
                # Python Logo
                self.Image_Python = QtWidgets.QLabel(self.centralwidget)
                self.Image_Python.setGeometry(QtCore.QRect(10, 10, 600, 150))
                # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
                # sizePolicy.setHorizontalStretch(60)
                # sizePolicy.setVerticalStretch(150)
                # sizePolicy.setHeightForWidth(self.Image_Python.sizePolicy().hasHeightForWidth())
                # self.Image_Python.setSizePolicy(sizePolicy)
                self.Image_Python.setMaximumSize(QtCore.QSize(600, 150))
                self.Image_Python.setStyleSheet("\n"
        "image: url(:/Window_files/Python.png);")
                self.Image_Python.setFrameShape(QtWidgets.QFrame.WinPanel)
                self.Image_Python.setText("")
                self.Image_Python.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
                self.Image_Python.setObjectName("Image_Python")
                self.Image_Objetivismo = QtWidgets.QLabel(self.centralwidget)
                self.Image_Objetivismo.setGeometry(QtCore.QRect(10, 479, 600, 150))
                
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(60)
                sizePolicy.setVerticalStretch(150)
                sizePolicy.setHeightForWidth(self.Image_Objetivismo.sizePolicy().hasHeightForWidth())
                # Objetivismo Logo
                self.Image_Objetivismo.setSizePolicy(sizePolicy)
                self.Image_Objetivismo.setMaximumSize(QtCore.QSize(600, 150))
                self.Image_Objetivismo.setStyleSheet("\n"
        "image: url(:/Window_files/Qt.png);")
                self.Image_Objetivismo.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Image_Objetivismo.setText("")
                self.Image_Objetivismo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
                self.Image_Objetivismo.setObjectName("Image_Objetivismo")
                
                # Messages:
                # Start Message
                self.text_end_time = QtWidgets.QLabel(self.centralwidget)
                self.text_end_time.setGeometry(QtCore.QRect(20, 310, 121, 21))
                self.text_end_time.setFrameShape(QtWidgets.QFrame.WinPanel)
                self.text_end_time.setFrameShadow(QtWidgets.QFrame.Raised)
                self.text_end_time.setObjectName("text_end_time")
                # End Message
                self.text_start_time = QtWidgets.QLabel(self.centralwidget)
                self.text_start_time.setGeometry(QtCore.QRect(20, 280, 121, 21))
                self.text_start_time.setFrameShape(QtWidgets.QFrame.WinPanel)
                self.text_start_time.setFrameShadow(QtWidgets.QFrame.Raised)
                self.text_start_time.setObjectName("text_start_time")
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                '# FINAL: ' 
                '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.checkbox_download.setText(_translate("MainWindow", "Download Video"))
                self.pushButton_download_edit.setText(_translate("MainWindow", "Download and Edit"))
                self.input_insert_url.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Per favore inserisci il link del video:</p></body></html>"))
                self.input_insert_start_time.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
                self.input_insert_end_time.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
                self.pushButton_edit_segment.setText(_translate("MainWindow", "Only edit"))
                self.text_end_time.setText(_translate("MainWindow", "Segment end:"))
                self.text_start_time.setText(_translate("MainWindow", "Segment Start:"))
                self.input_video_filename.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Per favore inserisci il nome per salvare il video:</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
