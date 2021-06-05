from PyQt5 import QtCore, QtGui, QtWidgets
from controller.music_controller import MusicController
from controller.playlist_controller import Playlistcontroller
from controller.playlist_controller import Playlist
from vue.music_vue import MusicVue


class Ajout_musique(MusicVue):
    def __init__(self, music_controller, music_like_controller):
        self._music_controller = music_controller
        self._music_like_controller = music_like_controller
        super().__init__(music_controller)
    def setupUi(self, Dialog):
        #affichage et boutons de la page musique
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1081, 651))
        self.widget.setObjectName("widget")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 430, 201, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(40, 185, 201, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(40, 285, 201, 21))
        self.label_15.setObjectName("label_15")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setGeometry(QtCore.QRect(40, 160, 201, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(40, 135, 201, 21))
        self.label_16.setObjectName("label_16")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setGeometry(QtCore.QRect(40, 110, 201, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_15.setGeometry(QtCore.QRect(40, 260, 201, 21))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(40, 335, 201, 21))
        self.label_17.setObjectName("label_17")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_16.setGeometry(QtCore.QRect(40, 310, 201, 21))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setGeometry(QtCore.QRect(40, 75, 201, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_17.setGeometry(QtCore.QRect(40, 210, 201, 21))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setGeometry(QtCore.QRect(40, 235, 201, 21))
        self.label_19.setObjectName("label_19")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_18.setGeometry(QtCore.QRect(40, 360, 201, 21))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1081, 651))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 280, 201, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setGeometry(QtCore.QRect(40, 185, 201, 21))
        self.label_20.setObjectName("label_20")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(40, 160, 201, 21))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_22 = QtWidgets.QLabel(self.widget_2)
        self.label_22.setGeometry(QtCore.QRect(40, 135, 201, 21))
        self.label_22.setObjectName("label_22")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(40, 110, 201, 21))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_24 = QtWidgets.QLabel(self.widget_2)
        self.label_24.setGeometry(QtCore.QRect(40, 85, 201, 21))
        self.label_24.setObjectName("label_24")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(40, 210, 201, 21))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_26 = QtWidgets.QLabel(self.widget_2)
        self.label_26.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setObjectName("label_26")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.widget_3 = QtWidgets.QWidget(self.tab_5)
        self.widget_3.setEnabled(True)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 1081, 651))
        self.widget_3.setObjectName("widget_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 270, 201, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_21 = QtWidgets.QLabel(self.widget_3)
        self.label_21.setGeometry(QtCore.QRect(40, 185, 201, 21))
        self.label_21.setObjectName("label_21")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_21.setGeometry(QtCore.QRect(40, 160, 201, 21))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_25 = QtWidgets.QLabel(self.widget_3)
        self.label_25.setGeometry(QtCore.QRect(40, 135, 201, 21))
        self.label_25.setObjectName("label_25")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(40, 110, 201, 21))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_28 = QtWidgets.QLabel(self.widget_3)
        self.label_28.setGeometry(QtCore.QRect(40, 85, 201, 21))
        self.label_28.setObjectName("label_28")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_26.setGeometry(QtCore.QRect(40, 210, 201, 21))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_30 = QtWidgets.QLabel(self.widget_3)
        self.label_30.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        #changement de la police
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_30.setFont(font)
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setObjectName("label_30")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 30, 181, 22))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 80, 181, 22))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 130, 181, 22))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 180, 181, 22))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.tab_6, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        # Ici, on va faire en sorte que le programme exécute une fonction s'il clique sur "Ajouter"
        self.pushButton_3.clicked.connect(lambda: self.creation_du_compte(Dialog))
        self.pushButton_7.clicked.connect(lambda: self.show())
        self.pushButton_6.clicked.connect(lambda: self.ask())
        self.pushButton_4.clicked.connect(lambda: self.supprimer_musique())

        self.pushButton_9.clicked.connect(lambda: self.ajoutertouteslesmusiques())

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        # affichage des boutons et option de la page des musiques
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "Valider"))
        self.label_14.setText(_translate("Dialog", "Album :"))
        self.label_15.setText(_translate("Dialog", "Chemin musique :"))
        self.label_16.setText(_translate("Dialog", "Artiste :"))
        self.label_17.setText(_translate("Dialog", "Chemin image cover :"))
        self.label_18.setText(_translate("Dialog", "Titre :"))
        self.label_19.setText(_translate("Dialog", "Type :"))
        self.label.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Ajouter une musique"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Ajouter une musique"))
        self.pushButton_4.setText(_translate("Dialog", "Valider"))
        self.label_20.setText(_translate("Dialog", "Album :"))
        self.label_22.setText(_translate("Dialog", "Artiste :"))
        self.label_24.setText(_translate("Dialog", "Titre :"))
        self.label_26.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Supprimer une musique"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Supprimer une musique"))
        self.pushButton_5.setText(_translate("Dialog", "Valider"))
        self.label_21.setText(_translate("Dialog", "Album :"))
        self.label_25.setText(_translate("Dialog", "Artiste :"))
        self.label_28.setText(_translate("Dialog", "Titre :"))
        self.label_30.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Modifier une musique"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Modifier une musique"))
        self.pushButton_6.setText(_translate("Dialog", "Chercher une musique"))
        self.pushButton_7.setText(_translate("Dialog", "Afficher la bdd"))
        self.pushButton_8.setText(_translate("Dialog", "Playlists"))
        self.pushButton_9.setText(_translate("Dialog", "AJOUTER TOUTES LES MUSIQUES"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Tests"))

    #creation du compte / affichage
    def creation_du_compte(self, Dialog):
        titre = self.lineEdit_14.text()
        artiste = self.lineEdit_13.text()
        album = self.lineEdit_17.text()
        type = self.lineEdit_15.text()
        chemin_musique = self.lineEdit_16.text()
        chemin_cover_image = self.lineEdit_18.text()

        music = self.add_music([titre, artiste, album, type, chemin_musique, chemin_cover_image])
        if isinstance(music, str):
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage(music)

        self.show_music(music)

    def supprimer_musique(self):
        titre = self.lineEdit_20.text()
        artiste = self.lineEdit_19.text()
        album = self.lineEdit_23.text()
        self.delete_music(titre, artiste, album)
    def show(self):
        self.show_musics()
    def ask(self):
        self.search_music()

    def ajoutertouteslesmusiques(self):
        print(self._music_controller.list_musics())
        self._music_like_controller.reinitialisation_de_la_base_de_donnees()
        musiques = self._music_controller.initialisation_de_la_base_de_donnees()
        for musique in musiques:
            music = self.add_music(musique)
            self.show_music(music)



