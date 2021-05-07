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
def numpyQImage(image):
    qImg = QtGui.QImage()
    if image.dtype == np.uint8:
        if len(image.shape) == 2:
            channels = 1
            height, width = image.shape
            bytesPerLine = channels * width
            qImg = QtGui.QImage(
                image.data, width, height, bytesPerLine, QtGui.QImage.Format_Indexed8
            )
            qImg.setColorTable([QtGui.qRgb(i, i, i) for i in range(256)])
        elif len(image.shape) == 3:
            if image.shape[2] == 3:
                height, width, channels = image.shape
                bytesPerLine = channels * width
                qImg = QtGui.QImage(
                    image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888
                )
            elif image.shape[2] == 4:
                height, width, channels = image.shape
                bytesPerLine = channels * width
                fmt = QtGui.QImage.Format_ARGB32
                qImg = QtGui.QImage(
                    image.data, width, height, bytesPerLine, QtGui.QImage.Format_ARGB32
                )
    return qImg
class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = transform_img_ui.Ui_MainWindow()
        self.ui.setupUi(self)        

        self.ui.btn_upload.clicked.connect(self.get_image_file)
        self.ui.btn_transform.clicked.connect(self.transform_image)

    

    def get_image_file(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image File', r"", "Image files (*.jpg *.jpeg *.gif)")
        
        image = QPixmap(self.fileName).scaled(299,499,QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        
        self.ui.image_label_2.setPixmap(image)
    def transform_image(self):
        currentValue = self.ui.cbo_algorithms.currentText()
        print('---------------------------------------------------')
        image = cv2.imread(self.fileName,0)        
        if currentValue == 'High Pass Filtering':
            image_result = hpf(image)           
        else:
            image_result = lpf(image)        
        print(image_result.data)     

        # Convert Numpy Array to QImage Object :
        
        # qImg = numpyQImage(image_result)        
            # or : 
        height, width = image_result.shape[:2]
        fmt = QtGui.QImage.Format_RGB888
        qimage = QtGui.QImage(image_result.data, height, width,fmt)
        print(height,width,fmt)
        pixmap = QPixmap(qimage)
            # or :
        # qImg = qimage2ndarray.array2qimage(image_result)
        # print(qImg.isGrayscale())
        # pixmap = QPixmap.fromImage(qImg)
        # print(pixmap)

        # Convert Numpy Array to Image :
        # im = Image.fromarray(image_result).convert(mode="L")
        # im.save("result.jpg")
        # pixmap = QPixmap("result.jpeg")

        # Display Image
        pixmap = pixmap.scaled(299,499,QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)        
        self.ui.image_label_3.setPixmap(pixmap)
        # plt.imshow(image_result, cmap = 'gray')
        # plt.show()

                    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())