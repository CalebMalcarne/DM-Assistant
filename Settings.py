"""
Copyright © 2023 Malcarne Contracting Inc. All rights reserved.
"""
from edit_Config import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class SettingsWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Settings")
        self.config = getConfigData()
        self.initUI()
    

    def initUI(self):
        
        layout = QVBoxLayout()

        # Window size settings
        self.size_label = QLabel("Window Size:")
        layout.addWidget(self.size_label)

        self.size_combobox = QComboBox()
        self.size_combobox.addItems(["Small", "Medium", "Large"])
        layout.addWidget(self.size_combobox)

        # Log settings
        self.log_checkbox = QCheckBox("Enable Logs")
        self.log_checkbox.setTristate(False)
        layout.addWidget(self.log_checkbox)
        self.log_checkbox.setChecked(False)
        
        # New File
        self.log_newfile = QCheckBox("New File on Export")
        self.log_newfile.setTristate(False)
        layout.addWidget(self.log_newfile)
        self.log_newfile.setChecked(False)

        #Topic Number
        self.topicNum_label = QLabel("Dafault Topic Number:")
        layout.addWidget(self.topicNum_label)
        
        self.lineEdit_topic_Num = QSpinBox()
        layout.addWidget(self.lineEdit_topic_Num) 
        self.lineEdit_topic_Num.setValue(0)

        #Topic amount
        self.topicNum_label = QLabel("Dafault Words per Topic:")
        layout.addWidget(self.topicNum_label)
        
        self.lineEdit_word_Num = QSpinBox()
        layout.addWidget(self.lineEdit_word_Num) 
        self.lineEdit_word_Num.setValue(0)

        # Save button
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.applyChanges)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.applyChanges()
        else:
            super().keyPressEvent(event)

    def applyChanges(self):
        selected_size = self.size_combobox.currentText()
        self.main_window.resizeWindow(selected_size)

        log_state = self.log_checkbox.isChecked()
        self.main_window.toggleLogs(log_state)
        
        self.saveConfig()

        self.accept()

        
    def saveConfig(self):
        log_state = self.log_checkbox.isChecked()
        wordNum = int(self.lineEdit_word_Num.value())
        topicNum = int(self.lineEdit_topic_Num.value())
        new_file_state = self.log_newfile.isChecked()
        
        
        if(log_state > 0):
            self.config["enable_logs"] = True
        else:
            self.config["enable_logs"] = False
        
        self.config["default_topics"] = topicNum
        self.config["dafault_num_words"] = wordNum
        self.config["new_file"] = new_file_state
        
        writeConfigData(self.config)
        
        
        