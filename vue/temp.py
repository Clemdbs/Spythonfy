from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt

from vue.member_vue import MemberVue
from vue.music_vue import MusicVue

from controller.temp_controller import TempController
#Pour la musique
import pygame


class Ui_Dialog:
    def __init__(self, member_controller, music_controller):
        self._member_controller = member_controller
        self._member_vue = MemberVue(self._member_controller)

        self._music_controller = music_controller
        self._music_vue = MusicVue(self._music_controller)

        self._temp_controller = TempController(self._member_controller, self._music_controller)

        #Initialiser le pygame (pour le son une nouvelle fois)
        pygame.init()
        self.song = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.stackedWidget.setObjectName("stackedWidget")

        ##-------------------------------------------------------------
        #PAGE D'ACCUEIL (après connection)
        ##-------------------------------------------------------------

        self.Interface_accueil = QtWidgets.QWidget()
        self.Interface_accueil.setObjectName("Interface_accueil")
        self.widget_5 = QtWidgets.QWidget(self.Interface_accueil)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_5.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_5.setObjectName("widget_5")
        self.pushButton_Accueil_1 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_Accueil_1.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_1.setFont(font)
        self.pushButton_Accueil_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_1.setCheckable(False)
        self.pushButton_Accueil_1.setAutoRepeat(False)
        self.pushButton_Accueil_1.setAutoExclusive(False)
        self.pushButton_Accueil_1.setFlat(True)
        self.pushButton_Accueil_1.setObjectName("pushButton_Accueil_1")
        self.pushButton_Recherche_1 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_Recherche_1.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_1.setFont(font)
        self.pushButton_Recherche_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_1.setCheckable(False)
        self.pushButton_Recherche_1.setAutoRepeat(False)
        self.pushButton_Recherche_1.setAutoExclusive(False)
        self.pushButton_Recherche_1.setFlat(True)
        self.pushButton_Recherche_1.setObjectName("pushButton_Recherche_1")
        self.pushButton_Compte_1 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_Compte_1.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_1.setFont(font)
        self.pushButton_Compte_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_1.setCheckable(False)
        self.pushButton_Compte_1.setAutoRepeat(False)
        self.pushButton_Compte_1.setAutoExclusive(False)
        self.pushButton_Compte_1.setFlat(True)
        self.pushButton_Compte_1.setObjectName("pushButton_Compte_1")

        self.label_cover_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_cover_1.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_1.setText("")
        self.label_cover_1.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_1.setScaledContents(True)
        self.label_cover_1.setObjectName("label_cover_1")

        self.pushButton_gauche_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_gauche_1.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_1.setText("")
        icon_gauche = QtGui.QIcon()
        icon_gauche.addPixmap(QtGui.QPixmap(r"support\Interface\flèche_gauche.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_gauche_1.setIcon(icon_gauche)
        self.pushButton_gauche_1.setObjectName("pushButton_gauche_1")
        self.pushButton_droite_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_droite_1.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_1.setText("")
        icon_droite = QtGui.QIcon()
        icon_droite.addPixmap(QtGui.QPixmap(r"support\Interface\flèche_droite.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_droite_1.setIcon(icon_droite)
        self.pushButton_droite_1.setObjectName("pushButton_droite_1")

        self.volume_1 = QSlider(Qt.Horizontal, self.Interface_accueil)
        self.volume_1.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.volume_1.setMinimum(0)
        self.volume_1.setMaximum(100)
        self.volume_1.setValue(50)

        self.pushButton_pause_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_pause_1.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_1.setText("")
        self.icon_pause = QtGui.QIcon()
        self.icon_pause.addPixmap(QtGui.QPixmap(r"support\Interface\pause.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_play = QtGui.QIcon()
        self.icon_play.addPixmap(QtGui.QPixmap(r"support\Interface\play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pause_1.setIcon(self.icon_pause)
        self.pushButton_pause_1.setObjectName("pushButton_pause_1")

        self.pushButton_coeur_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_coeur_1.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_1.setText("")
        self.icon_coeur_vide = QtGui.QIcon()
        self.icon_coeur_vide.addPixmap(QtGui.QPixmap(r"support\Interface\coeur_vide.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_coeur_plein = QtGui.QIcon()
        self.icon_coeur_plein.addPixmap(QtGui.QPixmap(r"support\Interface\coeur_plein.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.couleur = "noir"


        self.pushButton_coeur_1.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_1.setObjectName("pushButton_coeur_1")
        self.pushButton_coeur_1.clicked.connect(self.toogle_heart)
        #Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_1.setStyleSheet("border-style:outset")

        self.nom_musique_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.nom_musique_1.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.nom_artiste_1.setGeometry(QtCore.QRect(40, 415, 151, 17))
        self.nom_artiste_1.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nom_musique_1.setFont(font)
        font2 = QtGui.QFont()
        font2.setBold(True)
        font2.setWeight(50)
        self.nom_artiste_1.setFont(font2)


        self.pushButton_4 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 50, 80, 71))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setAcceptDrops(False)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_rechercher_4 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_rechercher_4.setGeometry(QtCore.QRect(250, 20, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher_4.setFont(font)
        self.label_rechercher_4.setObjectName("label_rechercher_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 50, 80, 71))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setAcceptDrops(False)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_rechercher_5 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_rechercher_5.setGeometry(QtCore.QRect(250, 140, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher_5.setFont(font)
        self.label_rechercher_5.setObjectName("label_rechercher_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 170, 80, 71))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setAcceptDrops(False)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setText("")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 170, 80, 71))
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setAcceptDrops(False)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setText("")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(520, 170, 80, 71))
        self.pushButton_10.setMouseTracking(False)
        self.pushButton_10.setAcceptDrops(False)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setText("")
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setGeometry(QtCore.QRect(430, 170, 80, 71))
        self.pushButton_11.setMouseTracking(False)
        self.pushButton_11.setAcceptDrops(False)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setText("")
        self.pushButton_11.setCheckable(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(610, 170, 80, 71))
        self.pushButton_12.setMouseTracking(False)
        self.pushButton_12.setAcceptDrops(False)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setText("")
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setGeometry(QtCore.QRect(430, 50, 80, 71))
        self.pushButton_13.setMouseTracking(False)
        self.pushButton_13.setAcceptDrops(False)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setText("")
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setDefault(False)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")

        #On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_accueil)

        ##-------------------------------------------------------------
        ##PAGE DE RECHERCHE
        ##-------------------------------------------------------------

        self.Interface_recherche = QtWidgets.QWidget()
        self.Interface_recherche.setObjectName("Interface_recherche")
        self.widget_6 = QtWidgets.QWidget(self.Interface_recherche)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_6.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_6.setObjectName("widget_6")
        self.pushButton_Accueil_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_Accueil_2.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_2.setFont(font)
        self.pushButton_Accueil_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_2.setCheckable(False)
        self.pushButton_Accueil_2.setAutoRepeat(False)
        self.pushButton_Accueil_2.setAutoExclusive(False)
        self.pushButton_Accueil_2.setFlat(True)
        self.pushButton_Accueil_2.setObjectName("pushButton_Accueil_2")
        self.pushButton_Recherche_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_Recherche_2.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_2.setFont(font)
        self.pushButton_Recherche_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_2.setCheckable(False)
        self.pushButton_Recherche_2.setAutoRepeat(False)
        self.pushButton_Recherche_2.setAutoExclusive(False)
        self.pushButton_Recherche_2.setFlat(True)
        self.pushButton_Recherche_2.setObjectName("pushButton_Recherche_2")
        self.pushButton_Compte_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_Compte_2.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_2.setFont(font)
        self.pushButton_Compte_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_2.setCheckable(False)
        self.pushButton_Compte_2.setAutoRepeat(False)
        self.pushButton_Compte_2.setAutoExclusive(False)
        self.pushButton_Compte_2.setFlat(True)
        self.pushButton_Compte_2.setObjectName("pushButton_Compte_2")
        self.nom_utilisateur = QtWidgets.QLabel(self.Interface_recherche)
        self.nom_utilisateur.setGeometry(QtCore.QRect(250, 0, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nom_utilisateur.setFont(font)
        self.nom_utilisateur.setText("")
        self.nom_utilisateur.setObjectName("nom_utilisateur")
        self.label_rechercher = QtWidgets.QLabel(self.Interface_recherche)
        self.label_rechercher.setGeometry(QtCore.QRect(260, 100, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher.setFont(font)
        self.label_rechercher.setObjectName("label_rechercher")
        self.lineEdit_barre_de_recherche = QtWidgets.QLineEdit(self.Interface_recherche)
        self.lineEdit_barre_de_recherche.setGeometry(QtCore.QRect(260, 130, 161, 21))
        self.lineEdit_barre_de_recherche.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_barre_de_recherche.setObjectName("lineEdit_barre_de_recherche")
        self.pushButton_rechercher = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_rechercher.setGeometry(QtCore.QRect(421, 130, 31, 21))
        self.pushButton = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(260, 200, 80, 71))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(2, 82, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";https://www.hostinger.fr/tutoriels/commandes-git")
        self.pushButton.setCheckable(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 200, 80, 71))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";https://www.hostinger.fr/tutoriels/commandes-git")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_rechercher_2 = QtWidgets.QLabel(self.Interface_recherche)
        self.label_rechercher_2.setGeometry(QtCore.QRect(260, 170, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher_2.setFont(font)
        self.label_rechercher_2.setObjectName("label_rechercher_2")

        self.label_cover_2 = QtWidgets.QLabel(self.Interface_recherche)
        self.label_cover_2.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_2.setText("")
        self.label_cover_2.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_2.setScaledContents(True)
        self.label_cover_2.setObjectName("label_cover_2")

        self.pushButton_gauche_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_gauche_2.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_2.setText("")
        self.pushButton_gauche_2.setIcon(icon_gauche)
        self.pushButton_gauche_2.setObjectName("pushButton_gauche_2")
        self.pushButton_droite_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_droite_2.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_2.setText("")
        self.pushButton_droite_2.setIcon(icon_droite)
        self.pushButton_droite_2.setObjectName("pushButton_droite_2")

        self.volume_2 = QSlider(Qt.Horizontal, self.Interface_recherche)
        self.volume_2.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.volume_2.setMinimum(0)
        self.volume_2.setMaximum(100)
        self.volume_2.setValue(50)

        self.pushButton_pause_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_pause_2.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_2.setText("")
        self.pushButton_pause_2.setIcon(self.icon_pause)
        self.pushButton_pause_2.setObjectName("pushButton_pause_2")

        self.pushButton_coeur_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_coeur_2.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_2.setText("")

        self.pushButton_coeur_2.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_2.setObjectName("pushButton_coeur_2")
        self.pushButton_coeur_2.clicked.connect(self.toogle_heart)
        # Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_2.setStyleSheet("border-style:outset")

        self.nom_musique_2 = QtWidgets.QLabel(self.Interface_recherche)
        self.nom_musique_2.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_2 = QtWidgets.QLabel(self.Interface_recherche)
        self.nom_artiste_2.setGeometry(QtCore.QRect(40, 415, 151, 17))
        self.nom_artiste_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_musique_2.setFont(font)
        self.nom_artiste_2.setFont(font2)

        self.label_rechercher_3 = QtWidgets.QLabel(self.Interface_recherche)
        self.label_rechercher_3.setGeometry(QtCore.QRect(260, 270, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher_3.setFont(font)
        self.label_rechercher_3.setObjectName("label_rechercher_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 300, 80, 71))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_3.setText("")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 300, 80, 71))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setAcceptDrops(False)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(125, 255, 0, 69), stop:0.315789 rgba(64, 255, 0, 69), stop:0.423533 rgba(90, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(130, 255, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.578947 rgba(99, 255, 0, 130), stop:0.625 rgba(108, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))")
        self.pushButton_6.setText("")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 300, 80, 71))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setAcceptDrops(False)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(125, 255, 0, 69), stop:0.315789 rgba(64, 255, 0, 69), stop:0.423533 rgba(0, 207, 255, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(71, 214, 255, 130), stop:0.518717 rgba(130, 255, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.559809 rgba(71, 239, 255, 130), stop:0.578947 rgba(0, 189, 255, 130), stop:0.625 rgba(0, 251, 255, 69), stop:1 rgba(255, 255, 0, 69))")
        self.pushButton_7.setText("")
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_recherche)

        ##-------------------------------------------------------------
        ##PAGE DE COMPTE
        ##-------------------------------------------------------------

        self.Interface_compte = QtWidgets.QWidget()
        self.Interface_compte.setObjectName("Interface_compte")
        self.widget_7 = QtWidgets.QWidget(self.Interface_compte)
        self.widget_7.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_7.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_7.setObjectName("widget_7")
        self.pushButton_Accueil_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_Accueil_3.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_3.setFont(font)
        self.pushButton_Accueil_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_3.setCheckable(False)
        self.pushButton_Accueil_3.setAutoRepeat(False)
        self.pushButton_Accueil_3.setAutoExclusive(False)
        self.pushButton_Accueil_3.setFlat(True)
        self.pushButton_Accueil_3.setObjectName("pushButton_Accueil_3")
        self.pushButton_Recherche_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_Recherche_3.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_3.setFont(font)
        self.pushButton_Recherche_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_3.setCheckable(False)
        self.pushButton_Recherche_3.setAutoRepeat(False)
        self.pushButton_Recherche_3.setAutoExclusive(False)
        self.pushButton_Recherche_3.setFlat(True)
        self.pushButton_Recherche_3.setObjectName("pushButton_Recherche_3")
        self.pushButton_Compte_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_Compte_3.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_3.setFont(font)
        self.pushButton_Compte_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_3.setCheckable(False)
        self.pushButton_Compte_3.setAutoRepeat(False)
        self.pushButton_Compte_3.setAutoExclusive(False)
        self.pushButton_Compte_3.setFlat(True)
        self.pushButton_Compte_3.setObjectName("pushButton_Compte_3")


        self.label_cover_3 = QtWidgets.QLabel(self.Interface_compte)
        self.label_cover_3.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_3.setText("")
        self.label_cover_3.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_3.setScaledContents(True)
        self.label_cover_3.setObjectName("label_cover_3")

        self.pushButton_gauche_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_gauche_3.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_3.setText("")
        self.pushButton_gauche_3.setIcon(icon_gauche)
        self.pushButton_gauche_3.setObjectName("pushButton_gauche_3")
        self.pushButton_droite_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_droite_3.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_3.setText("")
        self.pushButton_droite_3.setIcon(icon_droite)
        self.pushButton_droite_3.setObjectName("pushButton_droite_3")

        self.volume_3 = QSlider(Qt.Horizontal, self.Interface_compte)
        self.volume_3.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.volume_3.setMinimum(0)
        self.volume_3.setMaximum(100)
        self.volume_3.setValue(50)

        self.pushButton_pause_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_pause_3.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_3.setText("")
        self.pushButton_pause_3.setIcon(self.icon_pause)
        self.pushButton_pause_3.setObjectName("pushButton_pause_3")

        self.pushButton_coeur_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_coeur_3.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_3.setText("")

        self.pushButton_coeur_3.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_3.setObjectName("pushButton_coeur_3")
        self.pushButton_coeur_3.clicked.connect(self.toogle_heart)
        # Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_3.setStyleSheet("border-style:outset")

        self.nom_musique_3 = QtWidgets.QLabel(self.Interface_compte)
        self.nom_musique_3.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_3 = QtWidgets.QLabel(self.Interface_compte)
        self.nom_artiste_3.setGeometry(QtCore.QRect(40, 415, 151, 17))
        self.nom_artiste_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_musique_3.setFont(font)
        self.nom_artiste_3.setFont(font2)

        self.label_connexion_2 = QtWidgets.QLabel(self.Interface_compte)
        self.label_connexion_2.setGeometry(QtCore.QRect(260, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_connexion_2.setFont(font)
        self.label_connexion_2.setObjectName("label_connexion_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_14.setGeometry(QtCore.QRect(260, 60, 201, 51))
        self.pushButton_14.setObjectName("pushButton_14")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_compte)

        ##-------------------------------------------------------------
        ##PAGE DE CONNEXION
        ##-------------------------------------------------------------

        self.Interface_connexion = QtWidgets.QWidget()
        self.Interface_connexion.setObjectName("Interface_connexion")
        self.label_connexion = QtWidgets.QLabel(self.Interface_connexion)
        self.label_connexion.setGeometry(QtCore.QRect(50, 70, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_connexion.setFont(font)
        self.label_connexion.setObjectName("label_connexion")
        self.lineEdit_adresse_mail_1 = QtWidgets.QLineEdit(self.Interface_connexion)
        self.lineEdit_adresse_mail_1.setGeometry(QtCore.QRect(50, 170, 201, 21))
        self.lineEdit_adresse_mail_1.setObjectName("lineEdit_adresse_mail_1")
        self.label_adresse_mail = QtWidgets.QLabel(self.Interface_connexion)
        self.label_adresse_mail.setGeometry(QtCore.QRect(50, 130, 201, 31))
        self.label_adresse_mail.setObjectName("label_adresse_mail")
        self.label_mot_de_passe = QtWidgets.QLabel(self.Interface_connexion)
        self.label_mot_de_passe.setGeometry(QtCore.QRect(50, 190, 201, 31))
        self.label_mot_de_passe.setObjectName("label_mot_de_passe")
        self.lineEdit_mot_de_passe_1 = QtWidgets.QLineEdit(self.Interface_connexion)
        self.lineEdit_mot_de_passe_1.setGeometry(QtCore.QRect(50, 230, 201, 21))
        self.lineEdit_mot_de_passe_1.setObjectName("lineEdit_mot_de_passe_1")
        self.pushButton_connexion = QtWidgets.QPushButton(self.Interface_connexion)
        self.pushButton_connexion.setGeometry(QtCore.QRect(50, 280, 111, 31))
        self.pushButton_connexion.setObjectName("pushButton_connexion")
        self.pushButton_pas_de_compte = QtWidgets.QPushButton(self.Interface_connexion)
        self.pushButton_pas_de_compte.setGeometry(QtCore.QRect(50, 370, 121, 31))
        self.pushButton_pas_de_compte.setObjectName("pushButton_pas_de_compte")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_connexion)

        ##-------------------------------------------------------------
        ##PAGE DE CREATION DE COMPTE
        ##-------------------------------------------------------------

        self.Interface_creation_compte = QtWidgets.QWidget()
        self.Interface_creation_compte.setObjectName("Interface_creation_compte")
        self.label_creation_de_compte = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_creation_de_compte.setGeometry(QtCore.QRect(50, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_creation_de_compte.setFont(font)
        self.label_creation_de_compte.setObjectName("label_creation_de_compte")
        self.label_adresse_mail_2 = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_adresse_mail_2.setGeometry(QtCore.QRect(50, 80, 201, 31))
        self.label_adresse_mail_2.setObjectName("label_adresse_mail_2")
        self.lineEdit_adresse_mail_2 = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_adresse_mail_2.setGeometry(QtCore.QRect(50, 120, 201, 21))
        self.lineEdit_adresse_mail_2.setObjectName("lineEdit_adresse_mail_2")
        self.label_pseudo = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_pseudo.setGeometry(QtCore.QRect(50, 140, 201, 31))
        self.label_pseudo.setObjectName("label_pseudo")
        self.lineEdit_pseudo = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_pseudo.setGeometry(QtCore.QRect(50, 170, 201, 21))
        self.lineEdit_pseudo.setObjectName("lineEdit_pseudo")
        self.label_mot_de_passe_2 = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_mot_de_passe_2.setGeometry(QtCore.QRect(50, 190, 201, 31))
        self.label_mot_de_passe_2.setObjectName("label_mot_de_passe_2")
        self.lineEdit_mot_de_passe_2 = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_mot_de_passe_2.setGeometry(QtCore.QRect(50, 220, 201, 21))
        self.lineEdit_mot_de_passe_2.setObjectName("lineEdit_mot_de_passe_2")
        self.label_confirmer_mot_de_passe = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_confirmer_mot_de_passe.setGeometry(QtCore.QRect(50, 240, 201, 31))
        self.label_confirmer_mot_de_passe.setObjectName("label_confirmer_mot_de_passe")
        self.lineEdit_confirmer_mot_de_passe = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_confirmer_mot_de_passe.setGeometry(QtCore.QRect(50, 270, 201, 21))
        self.lineEdit_confirmer_mot_de_passe.setObjectName("lineEdit_confirmer_mot_de_passe")
        self.comboBox_sexe = QtWidgets.QComboBox(self.Interface_creation_compte)
        self.comboBox_sexe.setGeometry(QtCore.QRect(50, 310, 81, 31))
        self.comboBox_sexe.setObjectName("comboBox_sexe")
        self.comboBox_sexe.addItem("")
        self.comboBox_sexe.addItem("")
        self.comboBox_sexe.addItem("")
        self.comboBox_sexe.addItem("")
        self.checkBox_accepter_les_conditions = QtWidgets.QCheckBox(self.Interface_creation_compte)
        self.checkBox_accepter_les_conditions.setGeometry(QtCore.QRect(50, 360, 281, 31))
        self.checkBox_accepter_les_conditions.setObjectName("checkBox_accepter_les_conditions")
        self.pushButton_creer_compte = QtWidgets.QPushButton(self.Interface_creation_compte)
        self.pushButton_creer_compte.setGeometry(QtCore.QRect(50, 420, 111, 31))
        self.pushButton_creer_compte.setObjectName("pushButton_creer_compte")
        self.pushButton_annuler = QtWidgets.QPushButton(self.Interface_creation_compte)
        self.pushButton_annuler.setGeometry(QtCore.QRect(170, 420, 111, 31))
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_creation_compte)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Appel de la fonction page qui permet de switcher de page comme son nom l'indique
        #Chaque page possède ses propres items
        #--------------------------------------------------------------------------------
        self.pushButton_Accueil_1.clicked.connect(lambda: self.page(0))
        self.pushButton_Accueil_2.clicked.connect(lambda: self.page(0))
        self.pushButton_Accueil_3.clicked.connect(lambda: self.page(0))

        self.pushButton_Recherche_1.clicked.connect(lambda: self.page(1))
        self.pushButton_Recherche_2.clicked.connect(lambda: self.page(1))
        self.pushButton_Recherche_3.clicked.connect(lambda: self.page(1))

        self.pushButton_Compte_1.clicked.connect(lambda: self.page(2))
        self.pushButton_Compte_2.clicked.connect(lambda: self.page(2))
        self.pushButton_Compte_3.clicked.connect(lambda: self.page(2))
        # --------------------------------------------------------------------------------

        #Si l'on se connecte, on arrive sur la page d'accueil
        self.pushButton_connexion.clicked.connect(lambda: self.page(0))
        #Si l'on appuie sur le bouton "Pas de compte", on arrive sur la page de création de compte
        self.pushButton_pas_de_compte.clicked.connect(lambda: self.page(4))
        #Si l'on appuie sur annuler, on arrive sur la page de connection
        self.pushButton_annuler.clicked.connect(lambda: self.page(3))
        #Si l'on appuie sur le bouton de deconnexion :
        self.pushButton_14.clicked.connect(lambda: self.page(3))

        #Ici, on va appeler la fonction qui va gérer la connection :
        self.pushButton_connexion.clicked.connect(lambda: self.connection())
        #Ici la recherche d'une musique (pour l'instant)
        self.pushButton_rechercher.clicked.connect(lambda: self.rechercher())

        #Gestion du bouton pause & play
        self.etat_musique = "Play"
        #À l'appui du bouton, on appelle la fonction toogle_etat_musique qui mettra en pause ou redémarrera la musique
        self.pushButton_pause_1.clicked.connect(lambda: self.toogle_etat_musique())
        self.pushButton_pause_2.clicked.connect(lambda: self.toogle_etat_musique())
        self.pushButton_pause_3.clicked.connect(lambda: self.toogle_etat_musique())

        #Gestion du slider volume
        self.volume_1.sliderMoved.connect(lambda: self.set_volume(1))
        self.volume_2.sliderMoved.connect(lambda: self.set_volume(2))
        self.volume_3.sliderMoved.connect(lambda: self.set_volume(3))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Accueil_1.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_1.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_1.setText(_translate("Dialog", "Mon compte"))
        self.label_rechercher_4.setText(_translate("Dialog", "Albums populaires"))
        self.label_rechercher_5.setText(_translate("Dialog", "Musiques populaires"))
        self.pushButton_Accueil_2.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_2.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_2.setText(_translate("Dialog", "Mon compte"))
        self.label_rechercher.setText(_translate("Dialog", "Rechercher"))
        self.lineEdit_barre_de_recherche.setPlaceholderText("Artistes, titres")
        self.pushButton_rechercher.setText(_translate("Dialog", "Ok"))
        self.pushButton.setText(_translate("Dialog", "Rap"))
        self.pushButton_2.setText(_translate("Dialog", "Pop"))
        self.label_rechercher_2.setText(_translate("Dialog", "Vos genres préférés"))
        self.label_rechercher_3.setText(_translate("Dialog", "Vos artistes préférés"))
        self.pushButton_Accueil_3.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_3.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_3.setText(_translate("Dialog", "Mon compte"))
        self.label_connexion_2.setText(_translate("Dialog", "Deconnexion"))
        self.pushButton_14.setText(_translate("Dialog", "Se deconnecter"))
        self.label_connexion.setText(_translate("Dialog", "Connexion"))
        self.label_adresse_mail.setText(_translate("Dialog", "Adresse mail :"))
        self.label_mot_de_passe.setText(_translate("Dialog", "Mot de passe :"))
        self.pushButton_connexion.setText(_translate("Dialog", "Connexion"))
        self.pushButton_pas_de_compte.setText(_translate("Dialog", "Pas de compte ?"))
        self.label_creation_de_compte.setText(_translate("Dialog", "Création de compte"))
        self.label_adresse_mail_2.setText(_translate("Dialog", "Adresse mail :"))
        self.label_pseudo.setText(_translate("Dialog", "Pseudo :"))
        self.label_mot_de_passe_2.setText(_translate("Dialog", "Mot de passe :"))
        self.label_confirmer_mot_de_passe.setText(_translate("Dialog", "Confirmation mot de passe :"))
        self.comboBox_sexe.setItemText(0, _translate("Dialog", "Sexe"))
        self.comboBox_sexe.setItemText(1, _translate("Dialog", "Femme"))
        self.comboBox_sexe.setItemText(2, _translate("Dialog", "Homme"))
        self.comboBox_sexe.setItemText(3, _translate("Dialog", "Autre"))
        self.checkBox_accepter_les_conditions.setText(_translate("Dialog", "J\'accèpte les conditions d\'utilisation"))
        self.pushButton_creer_compte.setText(_translate("Dialog", "Créer compte "))
        self.pushButton_annuler.setText(_translate("Dialog", "Annuler"))
        self.nom_musique_1.setText(_translate("Dialog", ""))
        self.nom_artiste_1.setText(_translate("Dialog", ""))
        self.lineEdit_mot_de_passe_1.setEchoMode(QtWidgets.QLineEdit.Password)


    def page(self, numero):
        if numero == 0:
            self.stackedWidget.setCurrentIndex(0)
        elif numero == 1:
            self.stackedWidget.setCurrentIndex(1)
        elif numero == 2:
            self.stackedWidget.setCurrentIndex(2)
        elif numero == 3:
            self.stackedWidget.setCurrentIndex(3)
        elif numero == 4:
            self.stackedWidget.setCurrentIndex(4)

    def toogle_heart(self):
        #Permet de changer la couleur du coeur, si l'utilisateur clique dessus
        #Pour savoir s'il aime la musique ou pas
        if self.couleur == "rouge":
            self.couleur = "noir"
            self.pushButton_coeur_1.setIcon(self.icon_coeur_vide)
            self.pushButton_coeur_2.setIcon(self.icon_coeur_vide)
            self.pushButton_coeur_2.setIcon(self.icon_coeur_vide)
        else:
            self.couleur = "rouge"
            self.pushButton_coeur_1.setIcon(self.icon_coeur_plein)
            self.pushButton_coeur_2.setIcon(self.icon_coeur_plein)
            self.pushButton_coeur_3.setIcon(self.icon_coeur_plein)

    def set_heart_black(self):
        #Permet de mettre le coeur en noir à chaque nouvelle musique non aimée, c'est un reset en gros
        self.couleur = "noir"
        self.pushButton_coeur_1.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_2.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_2.setIcon(self.icon_coeur_vide)

    def connection(self):
        #Petit affichage de test :
        self._member_vue.show_members()
        #Essaie de connection grâce au controller :
        Membre = self._temp_controller.test_connection([self.lineEdit_adresse_mail_1.text(), self.lineEdit_mot_de_passe_1.text()])
        if Membre == None:
            print("Nom d'utilisateur ou mot de passe faux")
        else:
            self.nom_utilisateur.setText(Membre['pseudo'])

    def rechercher(self):
        #Essaie de recherche grâce au controller :
        Musique = self._temp_controller.recherche_musique(self.lineEdit_barre_de_recherche.text())
        if Musique == None:
            print("Musique non trouvée")
        else:
            #Au début on gère pas encore les différents trucs obtenus
            #Mais un seul résultat
            #Après il faudra faire un affichage où on clique sur la musique désirée
            musique = Musique[0]

            chemin_cover_image = musique['chemin_cover_image']
            chemin_musique = musique['chemin_musique']

            #Bien faire attention de mettre à jour les autres pages :
            #Ici, on va modifier la pochette de la musique
            #Le nom de la musique
            #Et le nom de l'artiste

            self.label_cover_1.setPixmap(QtGui.QPixmap(r""+chemin_cover_image))
            self.nom_musique_1.setText(musique['titre'])
            self.nom_artiste_1.setText(musique['artiste'])

            self.label_cover_2.setPixmap(QtGui.QPixmap(r"" + chemin_cover_image))
            self.nom_musique_2.setText(musique['titre'])
            self.nom_artiste_2.setText(musique['artiste'])

            self.label_cover_3.setPixmap(QtGui.QPixmap(r"" + chemin_cover_image))
            self.nom_musique_3.setText(musique['titre'])
            self.nom_artiste_3.setText(musique['artiste'])

            #Si un son était là, alors, on le stop, pour ne pas avoir une superposition de son
            if self.song != None:
                self.song.stop()
            self.song = pygame.mixer.Sound(r"" + chemin_musique)
            self.song.play()
            self.song.set_volume(0.4)

            #Et on reset le coeur
            self.set_heart_black()

    def toogle_etat_musique(self):
    #Si on appuie sur le bouton play ou pause, pour stopper ou redémarrer la musique
        if self.etat_musique == "Play":
            pygame.mixer.pause()
            self.etat_musique = "Pause"
            self.pushButton_pause_1.setIcon(self.icon_play)
            self.pushButton_pause_2.setIcon(self.icon_play)
            self.pushButton_pause_3.setIcon(self.icon_play)
        else:
            pygame.mixer.unpause()
            self.etat_musique = "Play"
            self.pushButton_pause_1.setIcon(self.icon_pause)
            self.pushButton_pause_2.setIcon(self.icon_pause)
            self.pushButton_pause_3.setIcon(self.icon_pause)

    def set_volume(self, numero):
    #On met à jour les sliders des autres pages en même temps que
    #de récupérer la valeur du slider de la page active.
        if numero == 1:
            valeur = self.volume_1.value()
            self.volume_2.setValue(valeur)
            self.volume_3.setValue(valeur)
        elif numero == 2:
            valeur = self.volume_2.value()
            self.volume_1.setValue(valeur)
            self.volume_3.setValue(valeur)
        else:
            valeur = self.volume_3.value()
            self.volume_2.setValue(valeur)
            self.volume_1.setValue(valeur)
    #Et on va aussi venir modifier la valeur du volume sonnore.
        if self.song != None:   #Pour éviter de modifier la valeur de volume d'un son s'il n'est pas lancé
                                #Ne fonctionne pas encore
            self.song.set_volume(float(valeur) / 100.0)

    def set_prochaine_musique(self):
        pass

    def set_musique_precedente(self):
        pass