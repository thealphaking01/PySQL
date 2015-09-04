import MySQLdb as mdb
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,subprocess

class Form(QDialog):

	def __init__(self, parent=None):

		super(Form, self).__init__(parent)
		
		self.intext=QTextEdit()
		self.outtext=QTextBrowser()
		self.bt1=QPushButton()
		self.output=""

		self.bt1.setText("Run")

		grid = QGridLayout()
		grid.addWidget(self.intext, 1, 0)
		grid.addWidget(self.outtext, 2, 0)
		grid.addWidget(self.bt1,1,1)
		self.setLayout(grid)

		self.connect(self.bt1, SIGNAL("clicked()"),self.updateUi)
		self.setWindowTitle("PySQL- Doing SQL the easy way!")
		pass

	def updateUi(self): 
		self.outtext.append(os.system("mysql -u root -p"))
		pass



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()	