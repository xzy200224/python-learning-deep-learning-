# Form implementation generated from reading ui file 'QToolBox工具盒控件.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(201, 456)
        self.toolBox = QtWidgets.QToolBox(parent=Form)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 181, 411))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 181, 295))
        self.page.setObjectName("page")
        self.toolButton = QtWidgets.QToolButton(parent=self.page)
        self.toolButton.setGeometry(QtCore.QRect(0, 10, 181, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/java1234/Desktop/1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(parent=self.page)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 50, 181, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/java1234/Desktop/2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(parent=self.page)
        self.toolButton_3.setGeometry(QtCore.QRect(0, 90, 181, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/java1234/Desktop/3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 181, 295))
        self.page_2.setObjectName("page_2")
        self.toolButton_4 = QtWidgets.QToolButton(parent=self.page_2)
        self.toolButton_4.setGeometry(QtCore.QRect(0, 10, 181, 31))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.toolButton_5 = QtWidgets.QToolButton(parent=self.page_3)
        self.toolButton_5.setGeometry(QtCore.QRect(0, 10, 181, 31))
        self.toolButton_5.setIcon(icon)
        self.toolButton_5.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.toolButton_6 = QtWidgets.QToolButton(parent=self.page_4)
        self.toolButton_6.setGeometry(QtCore.QRect(0, 10, 181, 31))
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolBox.addItem(self.page_4, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(3)
        self.toolBox.layout().setSpacing(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "张三"))
        self.toolButton_2.setText(_translate("Form", "李四"))
        self.toolButton_3.setText(_translate("Form", "阿香"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "我的好友"))
        self.toolButton_4.setText(_translate("Form", "赵六"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "同学"))
        self.toolButton_5.setText(_translate("Form", "张三"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "家人"))
        self.toolButton_6.setText(_translate("Form", "张三"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "朋友"))
