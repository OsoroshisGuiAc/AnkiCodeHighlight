from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextBrowser, QVBoxLayout ,QHBoxLayout, QTextEdit, QCheckBox, QMainWindow, QGridLayout, QTabWidget, QAbstractItemView, QComboBox, QLabel
from PySide6.QtGui import QIcon, QPalette
from databaseHistoryLogic import DataBaseLogicHistory, PullDataBaseItens

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        dataBaseLogicHistory = DataBaseLogicHistory() #Deletes every and all instances of any previous databases
        dataBaseLogicHistory.resetDatabase()

        self.setWindowTitle("AnkiCodeHighlight")
        self.setWindowIcon(QIcon(r"Images\Icon.ico"))

        qWidget01 = QWidget() ##Submit should add 2 txtBoxes and a button of submit in the historic window
        qWidget02 = QWidget() #Config buttons
        qWidget03 = QWidget() #Output view in Css
        qWidget04 = QWidget() #Patreon Link IDK
            #TabWidget 4 Basic slots
        qTabWidget = QTabWidget()
        qTabWidget.addTab(qWidget01, "Submit")
        qTabWidget.addTab(qWidget02, "Config")
        qTabWidget.addTab(qWidget03, "Preview")
        qTabWidget.addTab(qWidget04, "BuyMeACoffe!")
            #Text Placeholder
        qTextEdit01 = QTextEdit('Css')
        qTextEdit01.overwriteMode()
        qTextEdit02 = QTextEdit('Preview')
        qTextEdit02.overwriteMode()

        vLayoutSubmitTab01 = QVBoxLayout()
        vLayoutSubmitTab01.addWidget(qTextEdit01)
        vLayoutSubmitTab01.addWidget(qTextEdit02)

        #SuperiorButtons

            ##Button "Erase"
        self.butn01 = QPushButton('Erase')#Erase everything (QWidgetSpace)
        self.butn01.pressed.connect(self.clearText)
        self.butn01.setIcon(QIcon(r"Images\Icon.ico")) #PROVISÓRIO!!!! (FZR ICONE)
            ##Button "KeepTextWhenSubmit"
        self.butn02 = QPushButton('KeepTextWhenSubmit') #Should togle the keep  of the text when submit is pressed (QWidgetSpace)
        self.butn02.toggled.connect(self.changeButtonTwoIcon)
        self.butn02.toggled.connect(self.KeepTextWhenSubmited)
        self.butn02.setIcon(QIcon(r"Images\Icon.ico")) #PROVISÓRIO!!!! (FZR ICONE)
        self.butn02.setCheckable(True)
        self.butn02.isChecked()

            ##Button "Submit"
        butn03 = QPushButton('Submit') #Process data(qTabWidget > qWidget1 >)
        butn03.pressed.connect(self.processTheFormatationToCssStyleAndInputIntoAnki) #(Implementar a lógica na classe em baixo)
        self.qComboBox01 = QComboBox() #RecentSubmitedListSelector HERE !!!
        self.qComboBox01.addItem("Recent Submited")
        self.qComboBox01.currentIndexChanged.connect(self.qComboBoxPressed)
        
            #Do a horizontal layout that implement the "submit" button and the "Recent Submited" comboBox
        hLayoutSubmitTab01 = QHBoxLayout()
        hLayoutSubmitTab01.addWidget(butn03)
        hLayoutSubmitTab01.addWidget(self.qComboBox01)
        vLayoutSubmitTab01.addLayout(hLayoutSubmitTab01)
        qWidget01.setLayout(vLayoutSubmitTab01)

        self.qTextEdit = QTextEdit() #Caixa principal de input (deve ser implementada uma lógica na qual atualizara as outras 2 caixas de tempo em tempo.)
        #self.qTextEdit.setHtml(False)
        'self.qTextEdit.changeEvent.connect(self.mainQTextEditLogic)#Implementar a lógica nesse método' #Alterar isso dps
        
        hLayoutToButtons01 = QHBoxLayout()
        hLayout01 = QHBoxLayout()
        hLayout01.addLayout(hLayoutToButtons01)
        
        hLayout01.addWidget(self.butn01)
        hLayout01.addWidget(self.butn02)
        #Lembra de trocar os textos desses 3 botões para imagens
        

        #Horizontal Layout #02
        hLayout02 = QHBoxLayout()
        hLayout02.addWidget(self.qTextEdit)
        hLayout02.addWidget(qTabWidget)

        v_Layout01 = QVBoxLayout()
        v_Layout01.addLayout(hLayout01)
        v_Layout01.addLayout(hLayout02)
        self.setLayout(v_Layout01)

        self.valor = 0

    def qComboBoxPressed(self): #Pull an item from the DB.
        '''Quando o valor do QComboBox for alterado o mesmo devera pegar o ID do item e pedir para o banco de dados pegar o respectivo item digitado e colar o texto na QTextEdit (self.qTextEdit) 
        
        #PROPRIEDADES DO COMBOX
        
        count - The number of items in the combobox
        currentData - The data for the current item
        currentIndex - The index of the current item in the combobox
        editable - Whether the combo box can be edited by the user
        maxVisibleItems - The maximum allowed size on screen of the combo box, measured in items

        #FUNÇÕES
        def addItem (icon, text[, userData=None])
        def addItem (text[, userData=None])
        def currentData ([role=Qt.UserRole])
        def removeItem (index)

        #SINAIS
        def activated (index)
        def currentIndexChanged (index)
        def currentTextChanged (arg__1)
        def editTextChanged (arg__1)
        def highlighted (index)
        def textActivated (arg__1)
        def textHighlighted (arg__1)
        '''
        valor = self.qComboBox01.currentIndex()

        pDBI = PullDataBaseItens()
        #self.qTextEdit.setPlainText(pDBI.pullStuff(self.qComboBox01.currentIndex()))
        self.qTextEdit.setPlainText(str(pDBI.pullStuff(self.qComboBox01.currentIndex())))


    def changeButtonTwoIcon(self, ktws): #Quando acabar o app trocar para 2 icones de alfinete e arrancar esse print
        if ktws != 1:
            self.butn02.setIcon(QIcon(r"Images\Icon.ico"))
            ktws != 0
        else:
            self.butn02.setIcon(QIcon(r"Images\Icon.ico"))
            ktws = 1
        return
    
    def clearText(self):
        self.qTextEdit.clear() #Clean the inputTextBox

    def KeepTextWhenSubmited(self, ktws):
        #ktws = KeepTextWhenSubmited Boolean
        return
    
    def mainQTextEditLogic(self):
        return
    
        
    def processTheFormatationToCssStyleAndInputIntoAnki(self):
            
            #O toPlainText() Retorna o texto excrito no bang isso deve ir para 2 lugares pór hora são eles:
                #Banco de dados
                #Area de processamento
            dataToProcess = self.qTextEdit.toPlainText()

            self.valor += 1
            self.qComboBox01.addItem("Caixa: " + str(self.valor))
 
            if self.butn02.isChecked() == False:
                dataBaseLogicHistory = DataBaseLogicHistory() #DataBase Class
                dataBaseLogicHistory.insertIntoDatabase(self.qTextEdit.toPlainText())

                self.qTextEdit.clear()
                print(dataToProcess)
                #print("The butn02 is checked")

                
            else:
                dataBaseLogicHistory = DataBaseLogicHistory() #DataBase Class
                dataBaseLogicHistory.insertIntoDatabase(self.qTextEdit.toPlainText())

                print(dataToProcess)
                #print("The butn02 is NOT checked")