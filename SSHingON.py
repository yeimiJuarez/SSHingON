__author__ = 'yjuarez'
from windowMax import Ui_MainWindow
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import (QTreeWidgetItem,QIcon,QMouseEvent,QFileSystemModel)
from PyQt4.QtCore import (SIGNAL,QEvent,Qt,QDir)
import sys,os,stat
from os import getcwd, listdir, stat
from os.path import dirname, isdir, isfile, join
from time import localtime, strftime
from hurry.filesize import size
_fromUtf8 = QtCore.QString.fromUtf8

class mainInitial(QtGui.QMainWindow):
  def  __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow() #treeview  UI
        self.ui.setupUi(self)
        self.showMaximized()
        self.home=os.getcwd()
        self.fileSystemModel = QFileSystemModel()


        #self.home=self.home + "/connections"
        #print (self.home)
        self.fillGrid2(self.home)
        #self.ui.treeWidget.isSortingEnabled()
        #self.ui.treeWidget.setSortingEnabled(True)
        self.ui.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.treeView, QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), self.onclick)
        #self.connect(self.ui.treeView.selectionModel(),
        #    SIGNAL("customContextMenuRequested(pressed)"), self.onclick)


#  def eventFilter(self, obj, event):
#        if event.type() in (QtCore.QEvent.MouseButtonPress, QtCore.QEvent.MouseButtonDblClick):
#            if event.button() == QtCore.Qt.LeftButton:
#                print "left"
#                return True
#            elif event.button() == QtCore.Qt.RightButton:
#                print "Right"
#                return True
#        return super(mainInitial, self).eventFilter(obj, event)
#
#       #self.button2.clicked.connect(self.on_button_clicked)
#
#       #self.button1.installEventFilter(self)

  @QtCore.pyqtSlot(QtCore.QModelIndex)
  def onclick(self,selected):
      index=self.ui.treeView.indexAt(selected)
      #getSelected= self.ui.treeView.selectedItems()
      print (index)
      fileinfo = QtCore.QFileInfo(self.fileSystemModel.fileInfo(index) )
      print (fileinfo)
      path = self.fileSystemModel.filePath(index)
      #pathABS =self.fileSystemModel.rootPath(index)
      print path
      #print pathABS
      if self.fileSystemModel.isDir(index):
          print ("es directorio")
      else:
          print ("es archivo")

      menu=QtGui.QMenu(self)
      action_1=menu.addAction("crear coneccion")
      action_1.triggered.connect(self.action1)
      action_2=menu.addAction("borrar coneccion")
      action_3=menu.addAction("Modificar coneccion")
      action_4=menu.addAction("Crear Carpeta")
      menu.exec_(QtGui.QCursor.pos())
      #menu1=self.menu.addAction(u'algo')

      #menu1.triggered.connect(self.M1clear)
      #print ("determinar si esta vacio, es archivo o carpeta derecho")

  def action1(self, index):
      print "accion lanzada action_1"
      #self.fileSystemModel.mkdir()
      #print (self.ui.treeView.indexAt(index))

  def fillGrid2(self,home):
        print (QDir.currentPath())
        self.fileSystemModel.setRootPath(QDir.currentPath())
        self.ui.treeView.setModel(self.fileSystemModel)
        self.ui.treeView.setRootIndex(self.fileSystemModel.index(QDir.currentPath()))
        self.ui.treeView.hideColumn(1)
        self.ui.treeView.hideColumn(2)
        self.ui.treeView.hideColumn(3)




  #def fillGrid(self,home):
  #      self.ui.treeWidget.setHeaderLabels(("Connection Name", "Size (Bites)", "Path" ))
  #      #print (home)
  #      items = listdir(unicode(self.home))
  #      self.ui.treeWidget.setModel(QFileSystemModel())
  #      self.ui.treeWidget.clear()
  #      #self.ui.treeView.clear()
  #      for i in items:
  #          # Omitir archivos ocultos.
  #          if i.startswith("."):
  #              continue
  #          filepath = join(home, i)
  #          # Obtener informacion del archivo.
  #          stats = stat(filepath)
  #          # Crear el control item.
  #          item_widget = QTreeWidgetItem(
  #              (i, strftime("%c", localtime(stats.st_mtime)).decode("utf-8"),
  #               size(stats.st_size) if isfile(filepath) else "")
  #          )
  #          print ("archivo",i,  size(stats.st_size))
  #          # Establecer el iono correspondiente.
  #          item_widget.setIcon(0, QIcon("images/%s.png" %
  #              ("file" if isfile(filepath) else "folder")))
  #          # Anadir elemento.
  #          self.ui.treeWidget.addTopLevelItem(item_widget)
  #          self.ui.treeWidget.isSortingEnabled()




if __name__ == '__main__':
    #import sys
    app = QtGui.QApplication(sys.argv)
    myapp = mainInitial()
    myapp.show()
    myapp.maximumSize()
    sys.exit(app.exec_())