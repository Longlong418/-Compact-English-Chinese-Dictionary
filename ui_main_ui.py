# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(499, 408)
        Form.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u"../../../\u58c1\u7eb8/\u5fae\u4fe1\u56fe\u7247_20220108212543.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.AVL = QPushButton(Form)
        self.AVL.setObjectName(u"AVL")
        self.AVL.setGeometry(QRect(190, 100, 121, 71))
        font = QFont()
        font.setFamilies([u"\u65b0\u5b8b\u4f53"])
        font.setPointSize(20)
        self.AVL.setFont(font)
        self.Trie = QPushButton(Form)
        self.Trie.setObjectName(u"Trie")
        self.Trie.setGeometry(QRect(190, 190, 121, 61))
        self.Trie.setFont(font)
        self.Trie.setCursor(QCursor(Qt.ArrowCursor))
        self.Hash_table = QPushButton(Form)
        self.Hash_table.setObjectName(u"Hash_table")
        self.Hash_table.setGeometry(QRect(190, 280, 121, 61))
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(16)
        self.Hash_table.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 10, 281, 41))
        font2 = QFont()
        font2.setFamilies([u"\u6977\u4f53"])
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 40, 111, 31))
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(10)
        self.label_3.setFont(font3)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 260, 161, 151))
        self.label.setPixmap(QPixmap(u"ui_images/3aa5199a-64ef-46ff-b499-d1a33c9217c9.jpg"))
        self.label.setScaledContents(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 260, 151, 151))
        self.label_4.setPixmap(QPixmap(u"ui_images/8dbfaa7d-5565-441c-85fd-69df778e09f0.jpg"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 70, 151, 161))
        self.label_5.setPixmap(QPixmap(u"ui_images/bb66d25b-f85f-4877-8d1c-062801b9a1ed.jpg"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 70, 161, 161))
        self.label_6.setPixmap(QPixmap(u"ui_images/\u56fe\u68072.jpg"))
        self.label_6.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5c0f\u578b\u82f1\u6c49\u8bcd\u5178", None))
        self.AVL.setText(QCoreApplication.translate("Form", u"AVL\u6811", None))
        self.Trie.setText(QCoreApplication.translate("Form", u"Trie\u6811", None))
        self.Hash_table.setText(QCoreApplication.translate("Form", u"Hash_Table", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u57fa\u4e8e\u4e09\u79cd\u6570\u636e\u7ed3\u6784\u7684\u82f1\u6c49\u8bcd\u5178", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"made by Longlong", None))
        self.label.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
    # retranslateUi

