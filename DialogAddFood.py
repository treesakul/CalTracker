import sys
from BasicNeedBox import BasicNeedBox
from ProfileManager import ProfileManager
from BasicNeedItem import BasicNeedItem

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class BasicNeedPageUI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, None)
        self.setMinimumSize(1280, 900)
        self.parent = parent
        self.initUI()


    def initUI(self):
        loader = QUiLoader()
        form = loader.load("./UIDesigner/BasicNeedUI.ui", None)
        self.setCentralWidget(form)

        ## connect all attribute ##
        self.addItem_button = form.findChild(QPushButton, "addItemBtn")
        self.addItem_button.clicked.connect(self.addItem)

        self.submit_button = form.findChild(QPushButton, "submitBtn")
        self.submit_button.clicked.connect(self.submit)


        self.itemBoxLayout = form.findChild(QVBoxLayout, "itemLayout")

        self.userBasicNeedBox = self.parent.currentUser.getBasicNeedBox()  # Init class: BasicNeedBox
        #print(self.parent.currentUser)
        
        self.updateItemBoxLayout()



    def addItem(self):
        # Dialog box
        self.addDialog = QDialog(self)
        self.addDialog.setMinimumSize(500, 400)
        layout = QVBoxLayout()

        loader = QUiLoader()
        dialogForm = loader.load("./UIDesigner/addBasicItemUI.ui", None)

        layout.addWidget(dialogForm)

        # init all attribute
        self.nameEntry = dialogForm.findChild(QLineEdit, "nameEntry")
        self.priceEntry = dialogForm.findChild(QLineEdit, "priceEntry")
        self.categoryComboBox = dialogForm.findChild(QComboBox, "categoryComboBox")
        self.quantityEntry = dialogForm.findChild(QSpinBox, "qtySpinBox")

        # init + connect button
        self.save_button = dialogForm.findChild(QPushButton, "okBtn")
        self.connect(self.save_button, SIGNAL("clicked()"), lambda text="ok": self.close(text))

        self.cancel_button = dialogForm.findChild(QPushButton, "cancelBtn")
        self.connect(self.cancel_button, SIGNAL("clicked()"), lambda text="cancel": self.close(text))

        # show dialog box
        self.addDialog.setLayout(layout)
        self.addDialog.show()


    def deleteItem(self, key):
        self.userBasicNeedBox.deleteBasicNeedItem(key)
        self.updateItemBoxLayout()

    def updateItemBoxLayout(self):
        self.userBasicNeedBox = self.parent.currentUser.getBasicNeedBox()
        self.basicNeed_item_list = []  # Use to store basic item widget
        self.delete_button_list = [] #Use to store all the delete button
        itemList = self.userBasicNeedBox.getBasicNeedList() #All basic need item in BasicNeedBox


        # clear all the widget in that layout
        self.parent.clearLayout(self.itemBoxLayout)
        #self.clearLayout(self.itemBoxLayout)

        for i in range(len(itemList)):
            self.basicNeed_item_list.append(QHBoxLayout())

            self.delete_button_list.append(QPushButton("del"))
            self.connect(self.delete_button_list[i], SIGNAL("clicked()"), lambda key=str(i): self.deleteItem(key))

            self.basicNeed_item_list[i].addWidget(QLabel(itemList[i].getItemName()))
            self.basicNeed_item_list[i].addWidget(QLabel("x " + str(itemList[i].getItemQuantity()) + " = " + str(itemList[i].getTotalPrice())))
            self.basicNeed_item_list[i].addWidget(self.delete_button_list[i])

            self.itemBoxLayout.addLayout(self.basicNeed_item_list[i])

    def close(self, text):
        if(text == "ok"):
            # create basic need item
            try:
                float(self.priceEntry.text())
            except:
                self.parent.showError("Price must be number :(")
                return

            basicNeedItem = BasicNeedItem(self.nameEntry.text(), self.priceEntry.text(), self.categoryComboBox.currentText(), self.quantityEntry.value())
            self.userBasicNeedBox.addBasicNeedItem(basicNeedItem)

            # update UI
            self.updateItemBoxLayout()
            self.addDialog.close()

        else:
            self.addDialog.close()


    def submit(self):
        profileManager = ProfileManager()
        profileManager.updateUserBasicNeedBox(self.parent.currentUser.getUsername(), self.userBasicNeedBox)

        if(self.parent.isLogin == "no"):
            self.parent.changePage(5)

        elif(self.parent.isLogin == "yes"):
            self.parent.changePage(4)
