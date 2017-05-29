import sys, time
from PySide.QtCore import *
from PySide.QtGui import *

class PbWidget(QProgressBar):
    def __init__(self, parent=None, total=20):
        super(PbWidget, self).__init__()
        self.setMinimum(1)
        self.setMaximum(total)        
        self._active = False  

    def update_bar(self, to_add_number):
        while True:
            time.sleep(0.5)
            value = self.value() + to_add_number            
            self.setValue(value)
            if value > 50:
                self.change_color("yellow")
            qApp.processEvents()
            if (value >= self.maximum()):                
                break
        self._active = False

    def closeEvent(self, event):
        self._active = False

    def change_color(self, color):
        template_css = """QProgressBar::chunk { background: %s; }"""
        css = template_css % color
        self.setStyleSheet(css)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_layout = QVBoxLayout()

        self.pb=PbWidget(total=101)
        self.main_layout.addWidget(self.pb)

        ok_button = QPushButton("Press to update Progress Bar")
        ok_button.clicked.connect(self.OK)      
        self.main_layout.addWidget(ok_button)       

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def OK(self):
        self.pb.update_bar(10)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(480, 320)
    window.show()
    sys.exit(app.exec_())
