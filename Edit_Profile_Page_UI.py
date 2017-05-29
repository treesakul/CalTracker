import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Edit_Profile_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.edit_profile_page_init()

    def edit_profile_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Edit_page_ui.ui", None)
        self.setCentralWidget(form)


        #set QLabel
        #self.EditPro_pic = form.findChild(QLabel, "EditPro_pic")
        #self.EditPro_pic.setPixmap("./fresh-healthy-apples.jpg")
        #self.EditPro_pic.setScaledContents(True)

        # set QLineEdit
        self.EditPro_Fname_textEdit = form.findChild(QLineEdit, "EditPro_Fname_textEdit")
        self.EditPro_Lname_textEdit = form.findChild(QLineEdit, "EditPro_Lname_textEdit")
        self.EditPro_userName_textEdit = form.findChild(QLineEdit, "EditPro_userName_textEdit")
        self.EditPro_passWord_textEdit = form.findChild(QLineEdit, "EditPro_passWord_textEdit")
        self.EditPro_weight_textEdit = form.findChild(QLineEdit, "EditPro_weight_textEdit")
        self.EditPro_height_textEdit = form.findChild(QLineEdit, "EditPro_height_textEdit")


        #set QRadioButton
        self.EditPro_Gender_Female_radioBT = form.findChild(QRadioButton, "EditPro_Gender_Female_radioBT")
        self.EditPro_Gender_Male_radioBT = form.findChild(QRadioButton, "EditPro_Gender_Male_radioBT")
        self.GenderGroup = QButtonGroup()
        self.GenderGroup.addButton(self.EditPro_Gender_Female_radioBT)
        self.GenderGroup.addButton(self.EditPro_Gender_Male_radioBT)

        #set QDateEdit
        self.EditPro_Bday_dateEdit = form.findChild(QDateEdit, "EditPro_Bday_dateEdit")


        #set QTextEdit
        self.show_textEdit = form.findChild(QTextEdit, "show_textEdit")


        #set QPushButton
        self.EditPro_save_bt = form.findChild(QPushButton, "EditPro_save_bt")
        self.EditPro_back_bt = form.findChild(QPushButton, "EditPro_back_bt")
        self.EditPro_pic_bt = form.findChild(QPushButton, "EditPro_pic_bt")



        #connect QPushButton
        self.EditPro_back_bt.clicked.connect(self.back_main)
        self.EditPro_save_bt.clicked.connect(self.save)
        self.EditPro_pic_bt.clicked.connect(self.choose_pic)


        #connect QRadioButton
        self.EditPro_Gender_Female_radioBT.clicked.connect(self.genderclick)
        self.EditPro_Gender_Male_radioBT.clicked.connect(self.genderclick)


    def genderclick(self):
        if self.sender() == self.EditPro_Gender_Female_radioBT:
            print("female")
            self.gender = "female"
        elif self.sender() == self.EditPro_Gender_Male_radioBT:
            print("male")
            self.gender = "male"


    def choose_pic(self):
        #filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
        filename,type = QFileDialog.getOpenFileName(self, 'Open Image','./' , "Image files(*.png *.jpg *.bmp *.gif)")
        print('Path file :', filename)
        self.pic = QPixmap(filename)

        width = self.EditPro_pic_bt.size().width()
        height = self.EditPro_pic_bt.size().height()

        self.pic.scaled(width, height, Qt.KeepAspectRatio)
        icon = QIcon(self.pic)
        #icon = QIcon(QPixmap(filename))

        self.EditPro_pic_bt.setText("")
        self.EditPro_pic_bt.setIcon(icon)

        self.EditPro_pic_bt.setIconSize(QSize(self.EditPro_pic_bt.size().width(), self.EditPro_pic_bt.size().height()))
        #self.EditPro_pic_bt.setScaledContents(True)

    def back_main(self):
        #self.show_textEdit.setText("")
        self.parent.changePage("Main_Page")


    def save(self):
        ###### .text() use with lineedit  ###### .toPlainText() use with textedit
        lis = []
        self.show_textEdit.setText("")
        self.pic = self.parent.current_user.pic

        self.Fname = self.EditPro_Fname_textEdit.text()
        self.Lname = self.EditPro_Lname_textEdit.text()
        self.Username = self.EditPro_userName_textEdit.text()
        self.password = self.EditPro_passWord_textEdit.text()
        self.weight = self.EditPro_weight_textEdit.text()
        self.height = self.EditPro_height_textEdit.text()

        self.date = self.EditPro_Bday_dateEdit.date().day()
        self.month = self.EditPro_Bday_dateEdit.date().month()
        self.year = self.EditPro_Bday_dateEdit.date().year()

        lis.append(self.Fname)
        lis.append(self.Lname)
        lis.append(str(self.date) + str(self.month) + str(self.year))
        lis.append(self.pic)
        
        lis.append(self.Username)
        lis.append(self.password)
        
        lis.append(self.weight)  ## not in use
        lis.append(self.height)

        print(lis)

        self.parent.current_user.edit_profile(self.parent.current_user.id,
                                              lis[0], lis[1], lis[2], lis[3])
        
        self.parent.current_account.edit_account(self.parent.current_user.id,
                                                 lis[4], lis[5])


        #self.show_textEdit.append(self.user_list)
        '''
        self.show_textEdit.append(self.Fname)
        self.show_textEdit.append(self.Lname)
        self.show_textEdit.append(self.Username)
        self.show_textEdit.append(self.password)
        self.show_textEdit.append(self.gender)
        self.show_textEdit.append(self.weigth)
        self.show_textEdit.append(self.heigth)
        self.show_textEdit.append(str(self.date))
        self.show_textEdit.append(str(self.month))
        self.show_textEdit.append(str(self.year))'''

    def get_pic(self):
        return self.pic


