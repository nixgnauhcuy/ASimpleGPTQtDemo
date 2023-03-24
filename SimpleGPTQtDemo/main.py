import sys
import openai
import requests

from Ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal


class chatThread(QThread):
    chatSignal = pyqtSignal(str)

    def __int__(self, text=None):
        super(chatThread, self).__init__()
        self.text = text

    def run(self):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages = [{"role":"user", "content": self.text}],
            )

            ask = response['choices'][0]['message']['content']
            self.chatSignal.emit(ask)
        except Exception as result:
            ask = str(result)
            self.chatSignal.emit(ask)


class createImgThread(QThread):
    createImgSignal = pyqtSignal(str, str)

    def __int__(self, text=None):
        super(createImgThread, self).__init__()
        self.text = text

    def run(self):
        try:
            response = openai.Image.create(
                prompt=self.text,
                n=1,
                size="512x512"
            )

            image_url = response['data'][0]['url']
            self.createImgSignal.emit(image_url, 'True')
        except Exception as result:
            image_url = str(result)
            self.createImgSignal.emit(image_url, 'False')



class MyPyQT_Form(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.chatRunFlag = False
        self.chat = chatThread()
        self.chat.chatSignal.connect(self.chatAskEvent)
        self.chatPushButton.clicked.connect(self.chatPushButtonEvent)

        self.createImgRunFlag = False
        self.createImg = createImgThread()
        self.createImg.createImgSignal.connect(self.createImgEvent)
        self.createImgPushButton.clicked.connect(self.createImgPushButtonEvent)


    def chatAskEvent(self, str):
        self.chatTextEdit.append('ask：\n' + str + '\n----------------------------------\n')
        self.statusBar.clearMessage()
        self.chatRunFlag = False

    def chatPushButtonEvent(self):
        if self.chatLineEdit.text() == "":
            return
        
        if self.chatRunFlag != False:
            return
        
        openai.api_key = self.apiKeyLineEdit.text()

        self.chatRunFlag = True
        self.chat.text = self.chatLineEdit.text()
        self.chatTextEdit.append('user：\n' + self.chat.text + '\n')

        self.statusBar.showMessage('正在生成中...')
        self.chat.start()
        

    def createImgEvent(self, url, flag):
        if flag == 'True':
            res = requests.get(url)
            photo = QPixmap()
            photo.loadFromData(res.content)
            self.createImgLabel.setPixmap(photo)
        else:
            self.createImgLabel.setText(url)

        self.createImgRunFlag = False
        self.statusBar.clearMessage()


    def createImgPushButtonEvent(self):
        if self.createImgLineEdit.text() == "":
            return
        
        if self.createImgRunFlag != False:
            return
        
        openai.api_key = self.apiKeyLineEdit.text()
    
        self.createImgRunFlag = True
        self.createImg.text = self.createImgLineEdit.text()

        self.statusBar.showMessage('正在生成中...')
        self.createImg.start()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())

