from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
import transform_img_ui
import cv2
from ultilities import hpf, lpf
from PIL import Image, ImageQt
import numpy as np
from matplotlib import pyplot as plt
import qimage2ndarray

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = transform_img_ui.Ui_MainWindow()
        self.ui.setupUi(self)        

        self.ui.btn_upload.clicked.connect(self.get_image_file)
        self.ui.btn_transform.clicked.connect(self.transform_image)

    

    def get_image_file(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image File', r"", "Image files (*.jpg *.jpeg *.gif)")
        
        img = Image.open(self.fileName).convert('LA')
        img.save('input/file.png')
        image = QPixmap('input/file.png').scaled(299,499,QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.image_label_2.setPixmap(image)
    def transform_image(self):
        currentValue = self.ui.cbo_algorithms.currentText()
        print('---------------------------------------------------')
        image = cv2.imread(self.fileName,0)    
        if currentValue == 'High Pass Filtering':
            image_result = hpf(image)           
        else:
            image_result = lpf(image)        

        im = (((image_result - image_result.min()) / (image_result.max() - image_result.min())) * 255.9).astype(np.uint8)
        img = Image.fromarray(im)
        path = img.save("output/file.png")

        image = QPixmap('output/file.png').scaled(299,499,QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)       
        self.ui.image_label_3.setPixmap(image)


                    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("Fourier Transform")
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())