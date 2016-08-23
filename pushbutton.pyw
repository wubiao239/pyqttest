from PySide import *
from PySide import *
import sys
app=QtGui.QApplication(sys.argv)
b=QtGui.QPushButton()
b.setText("button")
b.show()
app.connect(b,QtCore.SIGNAL("clicked()"),app,QtCore.SLOT("quit()"))
app.exec_()
