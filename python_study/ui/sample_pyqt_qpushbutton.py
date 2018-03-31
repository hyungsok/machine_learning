import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My QMainWindow")
        self.setGeometry(100, 100, 400, 400)

        btn1 = QPushButton("Button Click", self)
        btn1.move(50, 50)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        lblName = QLabel("Name")
        self.editName = QLineEdit()
        btnOk = QPushButton("OK")

        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(self.editName)
        layout.addWidget(btnOk)
        self.setLayout(layout)

        btnOk.clicked.connect(self.btnOkClicked)

    def btnOkClicked(self):
        name = self.editName.text()
        QMessageBox.information(self, "Info", name)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    myDialog = MyDialog()
    myDialog.show()

    app.exec_()
