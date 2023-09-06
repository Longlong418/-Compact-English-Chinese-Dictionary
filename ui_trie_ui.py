# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trie_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Form_trie(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(489, 335)
        icon = QIcon()
        icon.addFile(u"ui_images/icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(Qt.LeftToRight)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 200, 491, 20))
        font = QFont()
        font.setFamilies([u"\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53"])
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.translate = QPushButton(Form)
        self.translate.setObjectName(u"translate")
        self.translate.setGeometry(QRect(250, 130, 81, 41))
        self.english = QLineEdit(Form)
        self.english.setObjectName(u"english")
        self.english.setGeometry(QRect(120, 10, 121, 31))
        self.add = QPushButton(Form)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(250, 30, 81, 41))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 250, 54, 16))
        self.word_list = QListWidget(Form)
        self.word_list.setObjectName(u"word_list")
        self.word_list.setGeometry(QRect(340, 100, 151, 111))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 140, 21, 20))
        self.chinese = QLineEdit(Form)
        self.chinese.setObjectName(u"chinese")
        self.chinese.setGeometry(QRect(120, 60, 121, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 250, 101, 31))
        font1 = QFont()
        font1.setFamilies([u"\u534e\u6587\u884c\u6977"])
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 40, 21, 16))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 90, 491, 20))
        self.label_7.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 111, 41))
        self.label.setFont(font1)
        self.delet_word = QLineEdit(Form)
        self.delet_word.setObjectName(u"delet_word")
        self.delet_word.setGeometry(QRect(120, 240, 121, 41))
        self.delet = QPushButton(Form)
        self.delet.setObjectName(u"delet")
        self.delet.setGeometry(QRect(250, 240, 81, 41))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 140, 101, 31))
        self.label_3.setFont(font1)
        self.search_word = QLineEdit(Form)
        self.search_word.setObjectName(u"search_word")
        self.search_word.setGeometry(QRect(120, 130, 121, 41))
        self.search_word.setMouseTracking(False)
        self.search_word.setTabletTracking(False)
        self.word_num = QLabel(Form)
        self.word_num.setObjectName(u"word_num")
        self.word_num.setGeometry(QRect(330, 10, 141, 21))
        font2 = QFont()
        font2.setFamilies([u"\u6977\u4f53"])
        font2.setPointSize(11)
        self.word_num.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Trie\u6811", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", None))
        self.translate.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u4e00\u4e0b\u2192", None))
        self.english.setText("")
        self.english.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u82f1\u6587", None))
        self.add.setText(QCoreApplication.translate("Form", u"add", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.chinese.setText("")
        self.chinese.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u4e2d\u6587", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5355\u8bcd", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u5355\u8bcd", None))
        self.delet_word.setText("")
        self.delet_word.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u4f60\u8981\u5220\u9664\u7684\u5355\u8bcd", None))
        self.delet.setText(QCoreApplication.translate("Form", u"delete", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5355\u8bcd\u67e5\u8be2", None))
        self.search_word.setText("")
        self.search_word.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u4f60\u8981\u67e5\u8be2\u7684\u5355\u8bcd", None))
        self.word_num.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5df2\u5f55\u51650\u4e2a\u5355\u8bcd", None))
    # retranslateUi

