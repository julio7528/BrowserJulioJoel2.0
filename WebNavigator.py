import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QRect
from Navigator import *
from PyQt5 import QtCore, QtWidgets

class WebNavigator(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        #Start the browser
        self.browser = QWebEngineView(self.tab)
        self.browser.load(QtCore.QUrl('https://firefox.com'))
        self.showMaximized()
        self.setWindowTitle('WebNavigator')        
        self.menuMenu.addAction('Close', self.close)
        #Call the resizeEvent method to fit the browser to the tab
        self.resizeEvent(None)
        #call methods when buttons are clicked
        self.btnBack.clicked.connect(self.back)
        self.btnHome.clicked.connect(self.home)
        self.btnRefresh.clicked.connect(self.refresh)
        self.btnForWard.clicked.connect(self.forward)
        
        #add navbar
        self.navbar = QLineEdit(self.tab)
        self.navbar.returnPressed.connect(self.go_url)
        self.gridLayout.addWidget(self.navbar, 0, 4, 1, 1)
        self.browser.urlChanged.connect(self.update_url)

        #Add new tab
        self.btnAddTab.clicked.connect(self.addTab)
        self.tabNavigator.setTabsClosable(True)
        self.tabNavigator.tabCloseRequested.connect(self.closeTab)      

    #Manage the url
    def update_url(self, url):
        self.navbar.setText(url.toString())
    def go_url(self):
        url = self.navbar.text()
        self.browser.setUrl(QUrl(url))

    #Method where btnBack, btnHome, btnRefresh, btnForWard has clicked
    def back(self):
        self.browser.back()
    def home(self):
        self.browser.setUrl(QUrl('https://www.ciccopn.pt/'))
    def refresh(self):
        self.browser.reload()
    def forward(self):
        self.browser.forward()        
    #Method to resize the browser when the window is resized
    def resizeEvent(self, event):
        self.browser.setGeometry(QRect(0, 0, self.tab.width(), self.tab.height()))
    #Add new tab
    def addTab(self):
        #Insert a new tab in tabNavigator will be in the side of "Tab 1"
        self.tabNavigator.insertTab(1, QtWidgets.QWidget(), "New Tab")
        #Create a new browser
        self.browser = QWebEngineView(self.tabNavigator.widget(1))
        self.browser.load(QtCore.QUrl('https://firefox.com'))
        self.browser.setGeometry(QRect(0, 0, self.tabNavigator.widget(1).width(), self.tabNavigator.widget(1).height()))
        self.tabNavigator.setCurrentIndex(1)
        self.tabNavigator.setTabsClosable(True)
        self.resizeEvent(None)
        
    def closeTab(self):
        self.tabNavigator.removeTab(self.tabNavigator.currentIndex())        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = WebNavigator()
    app.show()
    qt.exec_()
