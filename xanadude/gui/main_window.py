from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, 
    QPushButton, QTabWidget, QLineEdit, QFormLayout, QCheckBox
)
from core.input_handler import handle_input
from core import logger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Xanadude')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        # Home Tab
        self.home_tab = QWidget()
        self.home_layout = QVBoxLayout()
        self.home_label = QLabel('Welcome to Xanadude', self)
        self.home_layout.addWidget(self.home_label)
        self.home_tab.setLayout(self.home_layout)
        self.tabs.addTab(self.home_tab, "Home")

        # Input Tab
        self.input_tab = QWidget()
        self.input_layout = QVBoxLayout()
        self.input_label = QLabel('Trigger an input event:', self)
        self.input_button = QPushButton('Trigger Input Event', self)
        self.input_button.clicked.connect(self.handle_button_click)
        self.input_layout.addWidget(self.input_label)
        self.input_layout.addWidget(self.input_button)
        self.input_tab.setLayout(self.input_layout)
        self.tabs.addTab(self.input_tab, "Input")

        # Settings Tab
        self.settings_tab = QWidget()
        self.settings_layout = QFormLayout()
        self.settings_label = QLabel('Settings:', self)
        self.settings_layout.addWidget(self.settings_label)

        self.setting_1 = QCheckBox('Enable Feature X')
        self.settings_layout.addRow('Feature X:', self.setting_1)
        self.setting_2 = QLineEdit()
        self.settings_layout.addRow('Setting 2:', self.setting_2)

        self.save_settings_button = QPushButton('Save Settings')
        self.save_settings_button.clicked.connect(self.save_settings)
        self.settings_layout.addWidget(self.save_settings_button)
        
        self.settings_tab.setLayout(self.settings_layout)
        self.tabs.addTab(self.settings_tab, "Settings")

        layout.addWidget(self.tabs)
        central_widget.setLayout(layout)

    def handle_button_click(self):
        event = 'Button Clicked'
        result = handle_input(event)
        self.home_label.setText(result)
        logger.info(f"Button clicked and input event triggered: {event}")

    def save_settings(self):
        feature_x_enabled = self.setting_1.isChecked()
        setting_2_value = self.setting_2.text()
        logger.info(f"Settings saved: Feature X: {feature_x_enabled}, Setting 2: {setting_2_value}")
        self.home_label.setText(f"Settings saved: Feature X: {feature_x_enabled}, Setting 2: {setting_2_value}")

def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()