import sys
from PyQt6.QtWidgets import QApplication, QWidget,  QPushButton
from PyQt6.QtCore import QPropertyAnimation



class InitApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GUI PROJECT FIRST')
        self.resize(600,400)
        self.setStyleSheet("""
            QWidget{
                    background-color: white;
                    margin: 20px 30px;
                    
                           }
        """)    
        
        self.button = QPushButton("click me!",self)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #008CBA;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;

            }
            QPushButton:hover {
                background-color: black;
            }
        """)


app = QApplication(sys.argv)

# 기본 윈도우 생성
window = QWidget()
window = InitApp()
window.show()

# 이벤트 루프 실행
sys.exit(app.exec())
