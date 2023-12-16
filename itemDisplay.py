from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from edit_Config import getConfigData  # Assuming this function exists and works as intended

class itemDisplay(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Magic Item Information")
        self.config = getConfigData()  # Retrieve configuration data
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        # Create labels and fields for displaying item information
        self.name_label = QLabel("Name:")
        self.name_value = QLabel()  # Will be populated with the item's name
        
        self.category_label = QLabel("Category:")
        self.category_value = QLabel()  # Will be populated with the item's category
        
        self.rarity_label = QLabel("Rarity:")
        self.rarity_value = QLabel()  # Will be populated with the item's rarity
        
        self.description_label = QLabel("Description:")
        self.description_value = QTextEdit()  # Will be populated with the item's description
        self.description_value.setReadOnly(True)  # Make the text edit read-only
        
        # Add widgets to the layout
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_value)
        layout.addWidget(self.category_label)
        layout.addWidget(self.category_value)
        layout.addWidget(self.rarity_label)
        layout.addWidget(self.rarity_value)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_value)
        
        self.setLayout(layout)  # Set the dialog's layout
        







        

        
        
        