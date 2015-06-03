__author__ = 'yjuarez'
from windowMax import Ui_MainWindow
from PyQt4 import QtGui
from PyQt4.QtGui import (QTreeWidgetItem,QIcon)
import sys,os,stat
from os import getcwd, listdir, stat
from os.path import dirname, isdir, isfile, join
from time import localtime, strftime
from hurry.filesize import size

class mainInitial(QtGui.QMainWindow):
  def  __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow() #treeview  UI
        self.ui.setupUi(self)
        self.showMaximized()
        self.home=os.getcwd()
        #print (self.home)
        self.fillGrid(self.home)

  def fillGrid(self,home):
        self.ui.treeWidget.setHeaderLabels(("File Name", "Size (Bites)", "Path" ))
        print (home)
        items = listdir(unicode(self.home))
        self.ui.treeWidget.clear()
        #self.ui.treeView.clear()
        for i in items:
            # Omitir archivos ocultos.
            if i.startswith("."):
                continue
            filepath = join(home, i)
            # Obtener informacion del archivo.
            stats = stat(filepath)
            # Crear el control item.
            item_widget = QTreeWidgetItem(
                (i, strftime("%c", localtime(stats.st_mtime)).decode("utf-8"),
                 size(stats.st_size) if isfile(filepath) else "")
            )
            print ("archivo",i,  size(stats.st_size))
            # Establecer el iono correspondiente.
            item_widget.setIcon(0, QIcon("images/%s.png" %
                ("file" if isfile(filepath) else "folder")))
            # Anadir elemento.
            self.ui.treeWidget.addTopLevelItem(item_widget)




if __name__ == '__main__':
    #import sys
    app = QtGui.QApplication(sys.argv)
    myapp = mainInitial()
    myapp.show()
    myapp.maximumSize()
    sys.exit(app.exec_())