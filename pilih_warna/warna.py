import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QColorDialog, QLabel, QHBoxLayout
from PySide2.QtGui import QColor

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Button to pick color
        self.pick_color_button = QPushButton('Pick Color', self)
        self.pick_color_button.clicked.connect(self.pickColor)
        self.layout.addWidget(self.pick_color_button)

        # Label to display hexadecimal value
        self.hex_label = QLabel('Hex Value:', self)
        self.layout.addWidget(self.hex_label)

        # Placeholder for showing the picked color
        self.color_widget = QWidget(self)
        self.color_widget.setMinimumSize(100, 100)
        self.color_widget.setStyleSheet("background-color: white;")
        self.layout.addWidget(self.color_widget)

        # Add predefined color buttons
        self.predefined_colors_layout = QHBoxLayout()
        self.layout.addLayout(self.predefined_colors_layout)

        predefined_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']

        for color_code in predefined_colors:
            color_button = QPushButton(self)
            color_button.setFixedSize(20, 20)
            color_button.setStyleSheet(f"background-color: {color_code};")
            color_button.clicked.connect(lambda _, code=color_code: self.setPredefinedColor(code))
            self.predefined_colors_layout.addWidget(color_button)

    def pickColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_widget.setStyleSheet(f"background-color: {color.name()};")
            self.hex_label.setText(f'Hex Value: {color.name()}')

    def setPredefinedColor(self, color_code):
        color = QColor(color_code)
        self.color_widget.setStyleSheet(f"background-color: {color.name()};")
        self.hex_label.setText(f'Hex Value: {color.name()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    picker = ColorPicker()
    picker.show()
    sys.exit(app.exec_())
