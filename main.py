import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
# 导入我们生成的界面
from ui_main_ui import Ui_Form
from ui_avl_ui import Ui_Form_avl
from ui_hash_ui import Ui_Form_hash
from ui_trie_ui import Ui_Form_trie
from avl import *
from hash import *
from trie import *
from load_data import *


# 继承QWidget类，以获取其属性和方法
class main(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.AVL.clicked.connect(self.avl_menu)
        self.ui.Hash_table.clicked.connect(self.hash_menu)
        self.ui.Trie.clicked.connect(self.trie_menu)
        
    def avl_menu(self):
        self.avl=Avl()
        self.avl.show()
    def hash_menu(self):
        self.hash=hash_table()
        self.hash.show()
    def trie_menu(self):
        self.trie=trie()
        self.trie.show()
        


class Avl(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form_avl()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.add_word)
        self.ui.delet.clicked.connect(self.delet_word)
        self.ui.translate.clicked.connect(self.search_word)
        self.ui.word_num.setText('当前已录入{}个单词'.format(hashtable.num))

    def add_word(self):
        english=self.ui.english.text().strip()#strip去掉空格
        chinese=self.ui.chinese.text().strip()
        if  chinese==""or english=="":
            QMessageBox.critical(self,'录入失败','输入不能为空！')
        elif english.encode('utf-8').isalpha():
            temp=avl_tree.insert(english,'=>'+chinese)
            if temp ==False:
                QMessageBox.critical(self,'录入失败','该单词已存在')
            else:
                QMessageBox.about(self,'提示','录入成功！') 
                self.ui.word_num.setText('当前已录入{}个单词'.format(avl_tree.num))
        else:
            QMessageBox.critical(self,'录入失败','请输入正确格式的英文')
    def delet_word(self):
        word=self.ui.delet_word.text().strip()#strip去掉空格
        if  word=='':
            QMessageBox.critical(self,'提示','输入不能为空！')
        elif word.encode('utf-8').isalpha():
            temp=avl_tree.delete(word)
            if temp ==False:
                QMessageBox.critical(self,'提示','该单词不存在')
            else:
                self.ui.word_num.setText('当前已录入{}个单词'.format(avl_tree.num))
                QMessageBox.about(self,'提示','删除成功！') 
                
        else:
            QMessageBox.critical(self,'错误','请输入正确格式的英文')
    def search_word(self):
        tword=self.ui.search_word.text().strip()#strip去掉空格
        if  tword=='':
            QMessageBox.critical(self,'提示','输入不能为空！')
        elif tword.encode('utf-8').isalpha():
            self.ui.word_list.clear()
            temp=avl_tree.search_word(tword)
            if temp ==False:
                self.ui.word_list.addItem("Not Found")
            else:
                self.ui.word_list.addItem(temp)
        else:
            QMessageBox.critical(self,'错误','请输入正确格式的英文')
class hash_table(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form_hash()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.add_word)
        self.ui.delet.clicked.connect(self.delet_word)
        self.ui.translate.clicked.connect(self.search_word)
        self.ui.word_num.setText('当前已录入{}个单词'.format(hashtable.num))

    def add_word(self):
        english=self.ui.english.text().strip()#strip去掉空格
        chinese=self.ui.chinese.text().strip()
        if  chinese==""or english=="":
            QMessageBox.critical(self,'录入失败','输入不能为空！')
        elif english.encode('utf-8').isalpha():
            temp=hashtable.insert(english,'=>'+chinese)
            if temp ==False:
                QMessageBox.critical(self,'录入失败','该单词已存在')
            else:
                QMessageBox.about(self,'提示','录入成功！')
                self.ui.word_num.setText('当前已录入{}个单词'.format(hashtable.num))
                #QApplication.processEvents() 
        else:
            QMessageBox.critical(self,'录入失败','请输入正确格式的英文')
    def delet_word(self):
        word=self.ui.delet_word.text().strip()#strip去掉空格
        if  word=='':
            QMessageBox.critical(self,'提示','输入不能为空！')
        elif  word=='':
            QMessageBox.critical(self,'提示','输入不能为空！')
        elif word.encode('utf-8').isalpha():
            temp=hashtable.delete(word)
            if temp ==False:
                QMessageBox.critical(self,'提示','该单词不存在')
            else:
                QMessageBox.about(self,'提示','删除成功！')
                self.ui.word_num.setText('当前已录入{}个单词'.format(hashtable.num))
                #QApplication.processEvents() 
        else:
            QMessageBox.critical(self,'错误','请输入正确格式的英文')
    def search_word(self):
        tword=self.ui.search_word.text().strip()#strip去掉空格
        if  tword=='':
            QMessageBox.critical(self,'提示','输入不能为空！')
        elif tword.encode('utf-8').isalpha():
            self.ui.word_list.clear()
            temp=hashtable.search_word(tword)
            if temp ==False:
                self.ui.word_list.addItem("Not Found")
            else:
                self.ui.word_list.addItem(temp)
        else:
            QMessageBox.critical(self,'错误','请输入正确格式的英文')

class trie(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form_trie()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.add_word)
        self.ui.delet.clicked.connect(self.delet_word)
        self.ui.translate.clicked.connect(self.search_word)
        self.ui.word_num.setText('当前已录入{}个单词'.format(hashtable.num))

    def add_word(self):
        english=self.ui.english.text().strip()#strip去掉空格
        chinese=self.ui.chinese.text().strip()
        if  chinese==""or english=="":
            QMessageBox.critical(self,'录入失败','输入不能为空！')
        elif english.encode('utf-8').isalpha():
            temp=trie_tree.insert(english,'=>'+chinese)
            if temp ==False:
                QMessageBox.critical(self,'录入失败','该单词已存在')
            else:
                QMessageBox.about(self,'提示','录入成功！') 
                self.ui.word_num.setText('当前已录入{}个单词'.format(trie_tree.num))
        else:
            QMessageBox.critical(self,'录入失败','请输入正确格式的英文')
    def delet_word(self):
        word=self.ui.delet_word.text().strip()#strip去掉空格
        if  word=='':
            QMessageBox.critical(self,'录入失败','输入不能为空！')
        elif word.encode('utf-8').isalpha():
            temp=trie_tree.delete(word)
            if temp ==False:
                QMessageBox.critical(self,'提示','该单词不存在')
            else:
                QMessageBox.about(self,'提示','删除成功！')
                self.ui.word_num.setText('当前已录入{}个单词'.format(trie_tree.num))
        else:
            QMessageBox.critical(self,'错误','请输入正确格式的英文')
    def search_word(self):
        tword=self.ui.search_word.text().strip()#strip去掉空格
        if  tword=='':
            QMessageBox.critical(self,'录入失败','输入不能为空！')
        elif tword.encode('utf-8').isalpha():
            self.ui.word_list.clear()
            temp=trie_tree.search_word(tword)
            if temp ==False:
                self.ui.word_list.addItem("Not Found")
            elif isinstance(temp,list):
                self.ui.word_list.addItem("Not Found")
                for t in temp:
                    self.ui.word_list.addItem(t)
            else:
                self.ui.word_list.addItem(temp)
        else:
            QMessageBox.critical(self,'错误','请输入正确格式的英文')


# 程序入口 
if __name__ == "__main__":
    #将单词录入三种数据结构中
    avl_tree=Avl_tree()
    trie_tree=Trie()
    hashtable=Hashtable()
    for i in words:
        avl_tree.insert(i,words[i])
        trie_tree.insert(i,words[i])
        hashtable.insert(i,words[i])
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)


    # 初始化并展示我们的界面组件
    window = main()
    window.setStyleSheet('''QWidget{background-color:CornflowerBlue;}''')#颜色
    window.setFixedSize(window.width(), window.height());    #禁止拉伸窗口
   
    window.show()
    
    # 结束QApplication
    sys.exit(app.exec_())
