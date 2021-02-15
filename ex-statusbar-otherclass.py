import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.win_widget = Example(self)
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.win_widget)
        self.setCentralWidget(widget)
        self.statusBar().showMessage("İlk açılış mesajı") 

class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        
        self.myButton = QPushButton( "SA", self)
        self.myButton2 = QPushButton("SA2", self)

        self.myButton2.clicked.connect(self.process)
        
        # create the layout area for tab widget
        self.mylayout = QVBoxLayout()
        self.mylayout.addWidget(self.myButton)
        self.mylayout.addWidget(self.myButton2)
        self.setLayout(self.mylayout)

    def process(self):
        self.parent().parent().statusBar().showMessage("Buton tıklandığında mesaj")



def main():    
    try:
        app = QApplication(sys.argv) 
    except:
        app = QApplication.instance()            
    app.aboutToQuit.connect(app.deleteLater) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
main()