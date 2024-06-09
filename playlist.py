import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 340)
        Dialog.setStyleSheet("background-color: black;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.label.setStyleSheet("QLabel{\n"
"font: 63 18pt \"Segoe UI\";\n"
"color: white;\n"
"}")
        self.label.setObjectName("label")
        self.playlistName = QtWidgets.QLineEdit(Dialog)
        self.playlistName.setGeometry(QtCore.QRect(210, 20, 221, 41))
        self.playlistName.setStyleSheet("QLineEdit{\n"
"color: white;\n"
"background-color: rgba(255,255,255,50);\n"
"border-radius: 5px;\n"
"border-bottom: 2px solid green;\n"
"}")
        self.playlistName.setObjectName("playlistName")
        self.selectSongs = QtWidgets.QPushButton(Dialog)
        self.selectSongs.setGeometry(QtCore.QRect(20, 120, 151, 41))
        self.selectSongs.setStyleSheet("QPushButton{\n"
"color: white;\n"
"font: 75 12pt \"Segoe UI Semibold\";\n"
"background-color: green;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: darkgreen;\n"
"}")
        self.selectSongs.setObjectName("selectSongs")
        self.noOfSongs = QtWidgets.QLabel(Dialog)
        self.noOfSongs.setGeometry(QtCore.QRect(210, 120, 221, 41))
        self.noOfSongs.setStyleSheet("QLabel{\n"
"font: 63 18pt \"Segoe UI\";\n"
"color: white;\n"
"}")
        self.noOfSongs.setObjectName("noOfSongs")
        self.createPlaylist = QtWidgets.QPushButton(Dialog)
        self.createPlaylist.setGeometry(QtCore.QRect(150, 220, 151, 41))
        self.createPlaylist.setStyleSheet("QPushButton{\n"
"color: white;\n"
"font: 75 12pt \"Segoe UI Semibold\";\n"
"background-color: green;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: darkgreen;\n"
"}")
        self.createPlaylist.setObjectName("createPlaylist")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.selectSongs.clicked.connect(self.select_songs)
        self.createPlaylist.clicked.connect(self.create_playlist)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create new playlist"))
        self.label.setText(_translate("Dialog", "playlist name:"))
        self.selectSongs.setText(_translate("Dialog", "Select songs..."))
        self.noOfSongs.setText(_translate("Dialog", "0 songs selected."))
        self.createPlaylist.setText(_translate("Dialog", "Create playlist"))

    def select_songs(self):
        file_paths, _ = QFileDialog.getOpenFileNames(None, "Select Songs", "", "Audio Files (*.mp3 *.wav)")
        self.selected_songs = file_paths
        self.noOfSongs.setText(f"{len(file_paths)} songs selected.")

    def create_playlist(self):
        playlist_name = self.playlistName.text()
        if hasattr(self, 'selected_songs'):
            playlist_data = Playlist(playlist_name, self.selected_songs)
            with open('playlists.dat', 'ab') as f:
                pickle.dump(playlist_data, f)
            print("Playlist Data:", playlist_data.__dict__)
        else:
            print("No songs selected!")
    def show_playlists(self):
        with open('playlists.dat', 'rb') as f:
            try:
                c=0
                while True:
                    obj= pickle.load(f)
                    c+= 1
                    print(f"Name: {obj.name}")
            except:
                print(f"Finished reading. Found {c} playlists.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.show_playlists()
    ui.setupUi(Dialog)
    Dialog.show()
    
    sys.exit(app.exec_())
