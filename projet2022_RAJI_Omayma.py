# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:29:56 2022

@author: Omimiya
"""
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QWidget, QLabel, QRadioButton, QPlainTextEdit)

class PageAccueil:
    class ViewAccueil(QWidget):
        
        def ouvrirDossier(self):
            self.ouvrir = PageDossier.ViewDossier()
            self.hide()
            
        def __init__(self):
            super().__init__()

            self.myCtrl = ctrl


            self.labelImage = QLabel(self)
            self.pixmap = QPixmap('logo2.png')
            self.labelImage.setPixmap(self.pixmap)
            self.labelImage.resize(self.pixmap.width(),self.pixmap.height())

            self.labelPlatformName = QLabel(self)
            self.labelPlatformName.setText('E-Pharma')

            self.labelWelcomeMessage = QLabel(self)
            self.labelWelcomeMessage.setText('Bienvenue sur la plateforme E-Pharma')

            self.buttonCreate = QPushButton('Créer un dossier')
            self.buttonImport = QPushButton('Importer un dossier')

            self.init_ui()
            self.show()

        def init_ui(self):

            h_box_image = QHBoxLayout()
            h_box_image.addWidget(self.labelImage)

            h_box_label = QHBoxLayout()
            h_box_label.addWidget(self.labelPlatformName)

            h_box_message = QHBoxLayout()
            h_box_message.addWidget(self.labelWelcomeMessage)

            v_box_button = QVBoxLayout()
            v_box_button.addWidget(self.buttonCreate)
            v_box_button.addWidget(self.buttonImport)

            v_box = QVBoxLayout()
            v_box.addLayout(h_box_image)
            v_box.addLayout(h_box_label)
            v_box.addLayout(h_box_message)
            v_box.addLayout(v_box_button)

            self.labelPlatformName.setAlignment(QtCore.Qt.AlignCenter)
            self.labelWelcomeMessage.setAlignment(QtCore.Qt.AlignCenter)

            self.setLayout(v_box)
            self.setWindowTitle('E-Pharma')
            

            self.buttonCreate.clicked.connect(self.ouvrirDossier)


    #%%
    class Controller:
        def __init__(self):
            self.myModel = model


    #%%
    class Model:
        def __init__(self):
            pass


class PageDossier:
    class ViewDossier(QWidget):
            
        def __init__(self):
            super().__init__()

            self.myCtrl = ctrl

            self.labelSurname = QLabel(self)
            self.labelSurname.setText('Nom')

            self.labelName = QLabel(self)
            self.labelName.setText('Prénom')

            self.labelAge = QLabel(self)
            self.labelAge.setText('Age')

            self.labelGender = QLabel(self)
            self.labelGender.setText('Sexe')
            
            self.inputSurname = QLineEdit('')
            self.inputName = QLineEdit('')
            self.inputAge = QLineEdit('')
            self.inputGenderF = QRadioButton('F')   
            self.inputGenderM = QRadioButton('M')
            
            self.inputText1 = QPlainTextEdit('Veuillez entrer les symptômes et ordonnances ici')
            self.inputText2 = QPlainTextEdit('Propositions de médicaments')

            self.buttonHistory = QPushButton('Historique')
            self.buttonSave = QPushButton('Sauvegarder')
            self.buttonClose = QPushButton('Fermer')
            
            self.medicaments = {'Doliprane':['douleur','fièvre','paracétamol','comprimés','gélules'], 
                                'Dafalgan':['douleur','fièvre','paracétamol','comprimés','effervescent'],
                                'Efferalgan':['douleur','fièvre','paracétamol','effervescent'],
                                'Kardegic':['antiagrégant', 'aspirine', 'sang','vasculaires','cérébraux','cardiaque','AVC'],
                                'Spasfon':['antispasmodique', 'douleur', 'digestif', 'contractions', 'voies', 'biliaires', 'urinaires', 'règles'],
                                'Gaviscon':['antiacide', 'brulûre','estomac','indigestion', 'acide'],
                                'Dexeryl':['irritation','cutanée', 'sécheresse','peau', 'dermatite','psoriasis','brulûre'],
                                'Meteospasmyl':['antispasmodique' 'digestif','ballonnement'],
                                'Biseptine':['antiseptique', 'plaie', 'blessure', 'lésion','cutanée','infectée','infection'],
                                'Eludril':['bain', 'antiseptique', 'dents', 'gencive', 'infecion','bouche']}
            
            self.init_ui()
            self.show()

        def init_ui(self):
            
            v_box1 = QVBoxLayout()
            v_box1.addWidget(self.labelSurname)
            v_box1.addWidget(self.labelName)
            v_box1.addWidget(self.labelAge)
            v_box1.addWidget(self.labelGender)
            
            v_box2 = QVBoxLayout()
            v_box2.addWidget(self.inputSurname)
            v_box2.addWidget(self.inputName)
            v_box2.addWidget(self.inputAge)
            
            h_box3 = QHBoxLayout()
            h_box3.addWidget(self.inputGenderF)
            h_box3.addWidget(self.inputGenderM)  
            
            v_box2.addLayout(h_box3)
            
            h_box1 = QHBoxLayout()
            h_box1.addWidget(self.inputText1)
            h_box1.addWidget(self.inputText2)

            h_box2 = QHBoxLayout()
            h_box2.addWidget(self.buttonHistory)
            h_box2.addWidget(self.buttonSave)
            h_box2.addWidget(self.buttonClose)
                
            h_box = QHBoxLayout()
            h_box.addLayout(v_box1)
            h_box.addLayout(v_box2)

            v_box = QVBoxLayout()
            v_box.addLayout(h_box1)
            v_box.addLayout(h_box2)
            
            box = QVBoxLayout()
            box.addLayout(h_box)
            box.addLayout(v_box)
            
            self.setLayout(box)
            self.setWindowTitle('E-Pharma')
            self.inputText2.setDisabled(True)
            
            self.buttonSave.setToolTip('Enregistrer les informations dans la fiche du patient')
            self.buttonHistory.setToolTip('Afficher les notes du médecin concernant le patient ainsi que les ordonnances passées')
            self.buttonClose.setToolTip('Fermer cette page et revenir à la fenêtre d’accueil')
            
            self.buttonClose.clicked.connect(self.ouvrirAccueil)
            self.buttonHistory.clicked.connect(self.ouvrirHistorique)
            self.buttonSave.clicked.connect(self.enregistrer)
            
        def ouvrirAccueil(self):
            self.ouvrir = PageAccueil.ViewAccueil()
            self.hide()
                
        def ouvrirHistorique(self):
            self.ouvrir = PageHistorique.ViewHistorique()
            self.hide()
            
        def enregistrer(self):
            self.surname = self.labelSurname.text()
            self.name = self.labelName.text()
            self.age = self.labelAge.text()



    #%%
    class Controller:
        def __init__(self):
            self.myModel = model
        


    #%%
    class Model:
        
        def __init__(self):
            pass

        
class PageHistorique:
    class ViewHistorique(QWidget):
        def ouvrirDossier(self):
            self.ouvrir = PageDossier.ViewDossier()
            self.hide()
            
        def __init__(self):

            super().__init__()

            self.myCtrl = ctrl

            self.labelSurname = QLabel(self)
            self.labelSurname.setText('Nom')

            self.labelName = QLabel(self)
            self.labelName.setText('Prénom')

            self.labelAge = QLabel(self)
            self.labelAge.setText('Age')
        
            self.inputSurname = QLineEdit('')
            self.inputName = QLineEdit('')
            self.inputAge = QLineEdit('')
        
            self.inputText1 = QPlainTextEdit('Historique des symptômes et ordonnances du patient')
            self.buttonClose = QPushButton('Fermer')
        
            self.init_ui()
            self.show()

        def init_ui(self):
        
            v_box1 = QVBoxLayout()
            v_box1.addWidget(self.labelSurname)
            v_box1.addWidget(self.labelName)
            v_box1.addWidget(self.labelAge)
            
            v_box2 = QVBoxLayout()
            v_box2.addWidget(self.inputSurname)
            v_box2.addWidget(self.inputName)
            v_box2.addWidget(self.inputAge)
        
            h_box = QHBoxLayout()
            h_box.addLayout(v_box1)
            h_box.addLayout(v_box2)

        
            v_box = QVBoxLayout()
            v_box.addWidget(self.inputText1)
            v_box.addWidget(self.buttonClose)


            box = QVBoxLayout()
            box.addLayout(h_box)
            box.addLayout(v_box)

            self.setLayout(box)
            self.setWindowTitle("E-Pharma - Fenêtre d'historique")
            self.inputText1.setDisabled(True)
            self.inputSurname.setDisabled(True)
            self.inputName.setDisabled(True)
            self.inputAge.setDisabled(True)
        
            self.buttonClose.setToolTip('Fermer cette page et revenir à la fenêtre dossier')
            self.buttonClose.clicked.connect(self.ouvrirDossier)

print(__name__)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = PageAccueil.Model()
    ctrl = PageAccueil.Controller()
    view = PageAccueil.ViewAccueil()
    sys.exit(app.exec_())
        
        
        
        
        
        
        
