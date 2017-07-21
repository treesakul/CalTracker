import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from pony.orm import *

from MainSystem import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Edit_Profile_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.user = None
        self.system = MainSystem()
        self.set_user()
        self.cur_pic = ""
        self.edit_profile_page_init()
        
        

    def set_user(self):
        self.system.set_user(self.parent.getUser())
        self.user = self.parent.getUser()
        
    def edit_profile_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Edit_page_ui.ui", None)
        self.setCentralWidget(form)

        
        # set QLineEdit
        self.EditPro_Fname_textEdit = form.findChild(QLineEdit, "EditPro_Fname_textEdit")
        self.EditPro_Lname_textEdit = form.findChild(QLineEdit, "EditPro_Lname_textEdit")
        self.EditPro_userName_textEdit = form.findChild(QLineEdit, "EditPro_userName_textEdit")
        self.EditPro_passWord_textEdit = form.findChild(QLineEdit, "EditPro_passWord_textEdit")
        self.EditPro_passWord_textEdit.setEchoMode(QLineEdit.Password)

        #set QPushButton
        self.EditPro_save_bt = form.findChild(QPushButton, "EditPro_save_bt")
        self.EditPro_back_bt = form.findChild(QPushButton, "EditPro_back_bt")
        self.EditPro_pic_bt = form.findChild(QPushButton, "EditPro_pic_bt")


        #connect QPushButton
        self.EditPro_back_bt.clicked.connect(self.back_main) 
        self.EditPro_save_bt.clicked.connect(self.save)
        self.EditPro_pic_bt.clicked.connect(self.choose_pic)

        self.error_login = form.findChild(QLabel, "error_login")
        self.error_login.hide()


    def set_pic(self):
        self.cur_pic = self.system.user.pic
        if self.cur_pic is not None:
            self.EditPro_pic_bt.setText("")
           # print("cur2 : ",self.cur_pic)
            self.cur_pic = self.system.user.pic
           # print("cur3 : ",self.cur_pic)
            self.in_stylesheet = "QPushButton {border-image: url("+str(self.cur_pic)+") }"
            #print("stylesheet : ",self.in_stylesheet)
            self.EditPro_pic_bt.setStyleSheet(self.in_stylesheet)

            
        else:
            self.EditPro_pic_bt.setText("")
            self.cur_pic = self.system.user.pic
            self.in_stylesheet = "QPushButton {border-image: url("+str(self.cur_pic)+") }"
            self.EditPro_pic_bt.setStyleSheet(self.in_stylesheet)

            


    def choose_pic(self):
        
            self.EditPro_pic_bt.setText("")
            #self.in_stylesheet = "QPushButton {border-image: url("+str(self.cur_pic)+") }"
            #self.EditPro_pic_bt.setStyleSheet(self.in_stylesheet)
            

            #filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
            filename,type = QFileDialog.getOpenFileName(self, 'Open Image','./' , "Image files(*.png *.jpg *.bmp *.gif)")
            self.cur_pic = filename
            self.in_stylesheet = "QPushButton {border-image: url("+str(self.cur_pic)+") }"
            self.EditPro_pic_bt.setStyleSheet(self.in_stylesheet)

  

    def back_main(self):
        self.parent.changePage("Main_Page")


    def save(self):
        lis = []
        self.pic = self.parent.current_user.pic

        self.Fname = self.EditPro_Fname_textEdit.text()
        self.Lname = self.EditPro_Lname_textEdit.text()
        self.Username = self.EditPro_userName_textEdit.text()
        self.password = self.EditPro_passWord_textEdit.text()

        lis.append(self.Fname)
        lis.append(self.Lname)
        lis.append(self.cur_pic)
        
        lis.append(self.Username)
        lis.append(self.password)

        print("before save: ",self.system.user.fname," : ",self.system.user.pic)

        
        if '' not in lis:
##            self.parent.current_user.edit_profile(self.parent.current_user.id,lis[0], lis[1], lis[2])
##            self.parent.current_account.edit_account(self.parent.current_user.id,lis[3], lis[4])
            self.system.user.edit_profile(self.parent.current_user.id,lis[0], lis[1], lis[2])
            self.parent.current_account.edit_account(self.parent.current_user.id,lis[3], lis[4])
            self.update()
            print(self.parent.current_account)
        else:
            self.error_login.show()

    def get_pic(self):
        return self.pic


    def update(self):
        self.set_user()

        if(self.user != None):

            self.cur_pic = self.system.user.pic
            print(self.cur_pic)
            self.set_pic()
            


