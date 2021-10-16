import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(button)

    def the_button_was_clicked(self) -> None:
        print("Clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()