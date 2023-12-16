import sys
import os
from getDND import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Settings import SettingsWindow
from itemDisplay import itemDisplay

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setMaximumSize(QSize(16777215, 16777215))
        
        grid = QGridLayout()
        central_widget.setLayout(grid)
        grid.setColumnMinimumWidth(1, 10)  

        self.random_item_button = QPushButton("Random Item")
        self.random_magic_item_button = QPushButton("Random Magic Item")
        self.random_weapon_button = QPushButton("Random Weapon")
        self.random_armor_button = QPushButton("Random Armor")
        self.random_monster_button = QPushButton("Random Monster")
        self.cr_low = QSpinBox()  # QSpinBox for number input with arrow
        self.cr_high = QSpinBox() 
        self.cr_label = QLabel("        CR Range")
        
        self.random_item_button.clicked.connect(self.randomItem) 

        # Placing the widgets according to the wireframe layout
        grid.addWidget(self.random_item_button, 0, 0)
        grid.addWidget(self.random_magic_item_button, 1, 0)
        grid.addWidget(self.random_weapon_button, 2, 0)
        grid.addWidget(self.random_armor_button, 3, 0)
        grid.addWidget(self.random_monster_button, 0, 2)
        grid.addWidget(self.cr_label, 1, 2)
        grid.addWidget(self.cr_low, 2, 2)
        grid.addWidget(self.cr_high, 2, 3)
        

        
        #File Menu
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        file_menu = QMenu("File", self)
        self.menu_bar.addMenu(file_menu)
        self.export_action = file_menu.addAction("Export")
        self.export_action_2 = file_menu.addAction("Settings")
        self.export_action_2.triggered.connect(self.settingsWindow)

    def settingsWindow(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.exec_()

    def resizeWindow(self, size):
        desktop = QDesktopWidget()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
           
        if size == "Large":
            pass
            
        elif size == "Medium":        
            pass
            
        elif size == "Small": 
            pass
        
    def randomItem(self):
        item = getRandomItem()
        print(item)
        
        itemWindow = itemDisplay(self)
        itemWindow.show()
        if not hasattr(self, 'itemWindows'):
            self.itemWindows = []
        self.itemWindows.append(itemWindow)
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())