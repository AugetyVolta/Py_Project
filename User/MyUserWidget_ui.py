# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyUserWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyUserWidget(object):
    def setupUi(self, MyUserWidget):
        MyUserWidget.setObjectName("MyUserWidget")
        MyUserWidget.resize(1032, 665)
        self.layoutWidget = QtWidgets.QWidget(MyUserWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 979, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(838, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.TitleLabel = TitleLabel(self.layoutWidget)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TitleLabel.setProperty("pixelFontSize", 32)
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.CardWidget = CardWidget(MyUserWidget)
        self.CardWidget.setGeometry(QtCore.QRect(20, 110, 982, 141))
        self.CardWidget.setObjectName("CardWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.CardWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ImageLabel = ImageLabel(self.CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setMinimumSize(QtCore.QSize(128, 128))
        self.ImageLabel.setMaximumSize(QtCore.QSize(128, 128))
        self.ImageLabel.setObjectName("ImageLabel")
        self.horizontalLayout_4.addWidget(self.ImageLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.UserName = BodyLabel(self.CardWidget)
        self.UserName.setProperty("pixelFontSize", 24)
        self.UserName.setObjectName("UserName")
        self.horizontalLayout_2.addWidget(self.UserName)
        spacerItem3 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.line_2 = QtWidgets.QFrame(self.CardWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        spacerItem4 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.FavouriteNum = BodyLabel(self.CardWidget)
        self.FavouriteNum.setProperty("pixelFontSize", 20)
        self.FavouriteNum.setObjectName("FavouriteNum")
        self.horizontalLayout_2.addWidget(self.FavouriteNum)
        self.BodyLabel = BodyLabel(self.CardWidget)
        self.BodyLabel.setProperty("pixelFontSize", 20)
        self.BodyLabel.setObjectName("BodyLabel")
        self.horizontalLayout_2.addWidget(self.BodyLabel)
        spacerItem5 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.line_3 = QtWidgets.QFrame(self.CardWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        spacerItem6 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.EatenNum = BodyLabel(self.CardWidget)
        self.EatenNum.setProperty("pixelFontSize", 20)
        self.EatenNum.setObjectName("EatenNum")
        self.horizontalLayout_2.addWidget(self.EatenNum)
        self.BodyLabel_4 = BodyLabel(self.CardWidget)
        self.BodyLabel_4.setProperty("pixelFontSize", 20)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.horizontalLayout_2.addWidget(self.BodyLabel_4)
        spacerItem7 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.SignatureLable = CaptionLabel(self.CardWidget)
        self.SignatureLable.setProperty("pixelFontSize", 18)
        self.SignatureLable.setObjectName("SignatureLable")
        self.verticalLayout_4.addWidget(self.SignatureLable)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.layoutWidget_2 = QtWidgets.QWidget(MyUserWidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 260, 301, 391))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.CardWidget_2 = CardWidget(self.layoutWidget_2)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SubtitleLabel = SubtitleLabel(self.CardWidget_2)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.verticalLayout_3.addWidget(self.SubtitleLabel)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ProgressRing = ProgressRing(self.CardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressRing.sizePolicy().hasHeightForWidth())
        self.ProgressRing.setSizePolicy(sizePolicy)
        self.ProgressRing.setMinimumSize(QtCore.QSize(70, 70))
        self.ProgressRing.setMaximumSize(QtCore.QSize(70, 70))
        self.ProgressRing.setObjectName("ProgressRing")
        self.horizontalLayout_7.addWidget(self.ProgressRing)
        self.ProgressRing_2 = ProgressRing(self.CardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressRing_2.sizePolicy().hasHeightForWidth())
        self.ProgressRing_2.setSizePolicy(sizePolicy)
        self.ProgressRing_2.setMinimumSize(QtCore.QSize(70, 70))
        self.ProgressRing_2.setMaximumSize(QtCore.QSize(70, 70))
        self.ProgressRing_2.setObjectName("ProgressRing_2")
        self.horizontalLayout_7.addWidget(self.ProgressRing_2)
        self.ProgressRing_3 = ProgressRing(self.CardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressRing_3.sizePolicy().hasHeightForWidth())
        self.ProgressRing_3.setSizePolicy(sizePolicy)
        self.ProgressRing_3.setMinimumSize(QtCore.QSize(70, 70))
        self.ProgressRing_3.setMaximumSize(QtCore.QSize(70, 70))
        self.ProgressRing_3.setObjectName("ProgressRing_3")
        self.horizontalLayout_7.addWidget(self.ProgressRing_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ProgressRing_4 = ProgressRing(self.CardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressRing_4.sizePolicy().hasHeightForWidth())
        self.ProgressRing_4.setSizePolicy(sizePolicy)
        self.ProgressRing_4.setMinimumSize(QtCore.QSize(70, 70))
        self.ProgressRing_4.setMaximumSize(QtCore.QSize(70, 70))
        self.ProgressRing_4.setObjectName("ProgressRing_4")
        self.horizontalLayout_8.addWidget(self.ProgressRing_4)
        self.ProgressRing_5 = ProgressRing(self.CardWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressRing_5.sizePolicy().hasHeightForWidth())
        self.ProgressRing_5.setSizePolicy(sizePolicy)
        self.ProgressRing_5.setMinimumSize(QtCore.QSize(70, 70))
        self.ProgressRing_5.setMaximumSize(QtCore.QSize(70, 70))
        self.ProgressRing_5.setObjectName("ProgressRing_5")
        self.horizontalLayout_8.addWidget(self.ProgressRing_5)
        self.IndeterminateProgressRing = IndeterminateProgressRing(self.CardWidget_2)
        self.IndeterminateProgressRing.setMinimumSize(QtCore.QSize(70, 70))
        self.IndeterminateProgressRing.setMaximumSize(QtCore.QSize(70, 70))
        self.IndeterminateProgressRing.setObjectName("IndeterminateProgressRing")
        self.horizontalLayout_8.addWidget(self.IndeterminateProgressRing)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.CardWidget_2)
        self.CardWidget_3 = CardWidget(self.layoutWidget_2)
        self.CardWidget_3.setObjectName("CardWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CardWidget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SubtitleLabel_2 = SubtitleLabel(self.CardWidget_3)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.verticalLayout_2.addWidget(self.SubtitleLabel_2)
        self.FavouriteList = ListWidget(self.CardWidget_3)
        self.FavouriteList.setObjectName("FavouriteList")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FavouriteList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FavouriteList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FavouriteList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FavouriteList.addItem(item)
        self.verticalLayout_2.addWidget(self.FavouriteList)
        self.verticalLayout_5.addWidget(self.CardWidget_3)
        self.CardWidget_4 = CardWidget(MyUserWidget)
        self.CardWidget_4.setGeometry(QtCore.QRect(330, 260, 671, 391))
        self.CardWidget_4.setObjectName("CardWidget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.CardWidget_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.SegmentedWidget = SegmentedWidget(self.CardWidget_4)
        self.SegmentedWidget.setObjectName("SegmentedWidget")
        self.horizontalLayout_6.addWidget(self.SegmentedWidget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem14 = QtWidgets.QSpacerItem(448, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.CardWidget_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 80, 651, 53))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem15 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem15)
        self.SubtitleLabel_4 = SubtitleLabel(self.layoutWidget_3)
        self.SubtitleLabel_4.setProperty("pixelFontSize", 24)
        self.SubtitleLabel_4.setObjectName("SubtitleLabel_4")
        self.horizontalLayout_10.addWidget(self.SubtitleLabel_4)
        spacerItem16 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.CardWidget_6 = CardWidget(self.layoutWidget_3)
        self.CardWidget_6.setMinimumSize(QtCore.QSize(251, 51))
        self.CardWidget_6.setMaximumSize(QtCore.QSize(251, 51))
        self.CardWidget_6.setObjectName("CardWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.CardWidget_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.BodyLabel_3 = BodyLabel(self.CardWidget_6)
        self.BodyLabel_3.setProperty("pixelFontSize", 18)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.verticalLayout_9.addWidget(self.BodyLabel_3)
        self.horizontalLayout_10.addWidget(self.CardWidget_6)
        spacerItem17 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.layoutWidget_4 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 200, 651, 53))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem18 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem18)
        self.SubtitleLabel_6 = SubtitleLabel(self.layoutWidget_4)
        self.SubtitleLabel_6.setProperty("pixelFontSize", 24)
        self.SubtitleLabel_6.setObjectName("SubtitleLabel_6")
        self.horizontalLayout_12.addWidget(self.SubtitleLabel_6)
        spacerItem19 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem19)
        self.CardWidget_8 = CardWidget(self.layoutWidget_4)
        self.CardWidget_8.setMinimumSize(QtCore.QSize(251, 51))
        self.CardWidget_8.setMaximumSize(QtCore.QSize(251, 51))
        self.CardWidget_8.setObjectName("CardWidget_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.CardWidget_8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.BodyLabel_6 = BodyLabel(self.CardWidget_8)
        self.BodyLabel_6.setProperty("pixelFontSize", 18)
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.verticalLayout_11.addWidget(self.BodyLabel_6)
        self.horizontalLayout_12.addWidget(self.CardWidget_8)
        spacerItem20 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem20)
        self.layoutWidget_5 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 20, 651, 53))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem21 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem21)
        self.SubtitleLabel_3 = SubtitleLabel(self.layoutWidget_5)
        self.SubtitleLabel_3.setProperty("pixelFontSize", 24)
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")
        self.horizontalLayout_9.addWidget(self.SubtitleLabel_3)
        spacerItem22 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        self.CardWidget_5 = CardWidget(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget_5.sizePolicy().hasHeightForWidth())
        self.CardWidget_5.setSizePolicy(sizePolicy)
        self.CardWidget_5.setMinimumSize(QtCore.QSize(251, 51))
        self.CardWidget_5.setMaximumSize(QtCore.QSize(251, 51))
        self.CardWidget_5.setObjectName("CardWidget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.CardWidget_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.BodyLabel_2 = BodyLabel(self.CardWidget_5)
        self.BodyLabel_2.setProperty("pixelFontSize", 18)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.verticalLayout_8.addWidget(self.BodyLabel_2)
        self.horizontalLayout_9.addWidget(self.CardWidget_5)
        spacerItem23 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem23)
        self.layoutWidget_6 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_6.setGeometry(QtCore.QRect(0, 140, 651, 53))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem24 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem24)
        self.SubtitleLabel_5 = SubtitleLabel(self.layoutWidget_6)
        self.SubtitleLabel_5.setProperty("pixelFontSize", 24)
        self.SubtitleLabel_5.setObjectName("SubtitleLabel_5")
        self.horizontalLayout_11.addWidget(self.SubtitleLabel_5)
        spacerItem25 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem25)
        self.CardWidget_7 = CardWidget(self.layoutWidget_6)
        self.CardWidget_7.setMinimumSize(QtCore.QSize(251, 51))
        self.CardWidget_7.setMaximumSize(QtCore.QSize(251, 51))
        self.CardWidget_7.setObjectName("CardWidget_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.CardWidget_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.BodyLabel_5 = BodyLabel(self.CardWidget_7)
        self.BodyLabel_5.setProperty("pixelFontSize", 18)
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.verticalLayout_10.addWidget(self.BodyLabel_5)
        self.horizontalLayout_11.addWidget(self.CardWidget_7)
        spacerItem26 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem26)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.PushButton = PushButton(self.page_4)
        self.PushButton.setGeometry(QtCore.QRect(530, 220, 102, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PushButton.setFont(font)
        self.PushButton.setObjectName("PushButton")
        self.PushButton_2 = PushButton(self.page_4)
        self.PushButton_2.setGeometry(QtCore.QRect(530, 280, 102, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PushButton_2.setFont(font)
        self.PushButton_2.setObjectName("PushButton_2")
        self.layoutWidget_16 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_16.setGeometry(QtCore.QRect(0, 220, 391, 53))
        self.layoutWidget_16.setObjectName("layoutWidget_16")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.layoutWidget_16)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem27 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem27)
        self.SubtitleLabel_19 = SubtitleLabel(self.layoutWidget_16)
        self.SubtitleLabel_19.setProperty("pixelFontSize", 22)
        self.SubtitleLabel_19.setObjectName("SubtitleLabel_19")
        self.horizontalLayout_25.addWidget(self.SubtitleLabel_19)
        spacerItem28 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem28)
        self.LineEdit_3 = LineEdit(self.layoutWidget_16)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit_3.setFont(font)
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.horizontalLayout_25.addWidget(self.LineEdit_3)
        self.layoutWidget_7 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_7.setGeometry(QtCore.QRect(0, 70, 651, 53))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem29 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem29)
        self.SubtitleLabel_10 = SubtitleLabel(self.layoutWidget_7)
        self.SubtitleLabel_10.setProperty("pixelFontSize", 22)
        self.SubtitleLabel_10.setObjectName("SubtitleLabel_10")
        self.horizontalLayout_16.addWidget(self.SubtitleLabel_10)
        spacerItem30 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem30)
        self.LineEdit = LineEdit(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit.setFont(font)
        self.LineEdit.setObjectName("LineEdit")
        self.horizontalLayout_16.addWidget(self.LineEdit)
        spacerItem31 = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem31)
        self.layoutWidget_8 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_8.setGeometry(QtCore.QRect(0, 120, 651, 53))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem32 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem32)
        self.SubtitleLabel_7 = SubtitleLabel(self.layoutWidget_8)
        self.SubtitleLabel_7.setProperty("pixelFontSize", 22)
        self.SubtitleLabel_7.setObjectName("SubtitleLabel_7")
        self.horizontalLayout_13.addWidget(self.SubtitleLabel_7)
        spacerItem33 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem33)
        self.ComboBox = ComboBox(self.layoutWidget_8)
        self.ComboBox.setObjectName("ComboBox")
        self.horizontalLayout_13.addWidget(self.ComboBox)
        spacerItem34 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem34)
        self.layoutWidget_9 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_9.setGeometry(QtCore.QRect(0, 20, 651, 51))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem35 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem35)
        self.SubtitleLabel_9 = SubtitleLabel(self.layoutWidget_9)
        self.SubtitleLabel_9.setProperty("pixelFontSize", 22)
        self.SubtitleLabel_9.setObjectName("SubtitleLabel_9")
        self.horizontalLayout_15.addWidget(self.SubtitleLabel_9)
        spacerItem36 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem36)
        self.LineEdit_2 = LineEdit(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit_2.setFont(font)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.horizontalLayout_15.addWidget(self.LineEdit_2)
        spacerItem37 = QtWidgets.QSpacerItem(257, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem37)
        self.layoutWidget_10 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_10.setGeometry(QtCore.QRect(0, 170, 651, 53))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem38 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem38)
        self.SubtitleLabel_8 = SubtitleLabel(self.layoutWidget_10)
        self.SubtitleLabel_8.setProperty("pixelFontSize", 22)
        self.SubtitleLabel_8.setObjectName("SubtitleLabel_8")
        self.horizontalLayout_14.addWidget(self.SubtitleLabel_8)
        spacerItem39 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem39)
        self.ComboBox_3 = ComboBox(self.layoutWidget_10)
        self.ComboBox_3.setObjectName("ComboBox_3")
        self.horizontalLayout_14.addWidget(self.ComboBox_3)
        self.ComboBox_4 = ComboBox(self.layoutWidget_10)
        self.ComboBox_4.setObjectName("ComboBox_4")
        self.horizontalLayout_14.addWidget(self.ComboBox_4)
        self.ComboBox_5 = ComboBox(self.layoutWidget_10)
        self.ComboBox_5.setObjectName("ComboBox_5")
        self.horizontalLayout_14.addWidget(self.ComboBox_5)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem40)
        self.layoutWidget_17 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_17.setGeometry(QtCore.QRect(0, 270, 391, 53))
        self.layoutWidget_17.setObjectName("layoutWidget_17")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem41 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem41)
        self.SubtitleLabel_20 = SubtitleLabel(self.layoutWidget_17)
        self.SubtitleLabel_20.setProperty("pixelFontSize", 22)
        self.SubtitleLabel_20.setObjectName("SubtitleLabel_20")
        self.horizontalLayout_26.addWidget(self.SubtitleLabel_20)
        spacerItem42 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem42)
        self.LineEdit_4 = LineEdit(self.layoutWidget_17)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit_4.setFont(font)
        self.LineEdit_4.setObjectName("LineEdit_4")
        self.horizontalLayout_26.addWidget(self.LineEdit_4)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_7.addWidget(self.stackedWidget)

        self.retranslateUi(MyUserWidget)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MyUserWidget)

    def retranslateUi(self, MyUserWidget):
        _translate = QtCore.QCoreApplication.translate
        MyUserWidget.setWindowTitle(_translate("MyUserWidget", "Form"))
        self.TitleLabel.setText(_translate("MyUserWidget", "用户中心"))
        self.UserName.setText(_translate("MyUserWidget", "Manager"))
        self.FavouriteNum.setText(_translate("MyUserWidget", "1001"))
        self.BodyLabel.setText(_translate("MyUserWidget", "收藏"))
        self.EatenNum.setText(_translate("MyUserWidget", "666"))
        self.BodyLabel_4.setText(_translate("MyUserWidget", "吃过"))
        self.SignatureLable.setText(_translate("MyUserWidget", "关于吃什么，还得好好想一想"))
        self.SubtitleLabel.setText(_translate("MyUserWidget", "你的口味"))
        self.SubtitleLabel_2.setText(_translate("MyUserWidget", "你的最爱"))
        __sortingEnabled = self.FavouriteList.isSortingEnabled()
        self.FavouriteList.setSortingEnabled(False)
        item = self.FavouriteList.item(0)
        item.setText(_translate("MyUserWidget", "奶奶滴茶"))
        item = self.FavouriteList.item(1)
        item.setText(_translate("MyUserWidget", "王大队长"))
        item = self.FavouriteList.item(2)
        item.setText(_translate("MyUserWidget", "红烧坤"))
        item = self.FavouriteList.item(3)
        item.setText(_translate("MyUserWidget", "九转大肠"))
        self.FavouriteList.setSortingEnabled(__sortingEnabled)
        self.SubtitleLabel_4.setText(_translate("MyUserWidget", "昵称"))
        self.BodyLabel_3.setText(_translate("MyUserWidget", "小猪佩奇"))
        self.SubtitleLabel_6.setText(_translate("MyUserWidget", "生日"))
        self.BodyLabel_6.setText(_translate("MyUserWidget", "2000-01-01"))
        self.SubtitleLabel_3.setText(_translate("MyUserWidget", "用户名"))
        self.BodyLabel_2.setText(_translate("MyUserWidget", "This is the only indentity"))
        self.SubtitleLabel_5.setText(_translate("MyUserWidget", "性别"))
        self.BodyLabel_5.setText(_translate("MyUserWidget", "男"))
        self.PushButton.setText(_translate("MyUserWidget", "保存"))
        self.PushButton_2.setText(_translate("MyUserWidget", "重置"))
        self.SubtitleLabel_19.setText(_translate("MyUserWidget", "旧密码"))
        self.LineEdit_3.setText(_translate("MyUserWidget", "xzcXV"))
        self.SubtitleLabel_10.setText(_translate("MyUserWidget", "昵称"))
        self.LineEdit.setText(_translate("MyUserWidget", "xzcXV"))
        self.SubtitleLabel_7.setText(_translate("MyUserWidget", "性别"))
        self.SubtitleLabel_9.setText(_translate("MyUserWidget", "用户名"))
        self.LineEdit_2.setText(_translate("MyUserWidget", "xzcXV"))
        self.SubtitleLabel_8.setText(_translate("MyUserWidget", "生日"))
        self.SubtitleLabel_20.setText(_translate("MyUserWidget", "新密码"))
        self.LineEdit_4.setText(_translate("MyUserWidget", "xzcXV"))
from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, ComboBox, ImageLabel, IndeterminateProgressRing, LineEdit, ListWidget, ProgressRing, PushButton, SegmentedWidget, SubtitleLabel, TitleLabel