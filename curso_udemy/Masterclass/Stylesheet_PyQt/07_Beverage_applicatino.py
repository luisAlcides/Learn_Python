import sys

from PyQt6.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QCheckBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        tab_widget = QTabWidget()

        tea_tab = QWidget()
        coffe_tab = QWidget()

        tab_widget.addTab(tea_tab, 'Tea')
        tab_widget.addTab(coffe_tab, 'Coffe')

        # Tea Layout
        tea_layout = QVBoxLayout()

        liquid_label = QLabel("Select Milk/Water")
        milk_button = QRadioButton('Milk')
        water_button = QRadioButton('Water')

        # create container for milk/water
        liquid_group = QGroupBox()

        # Creating a layout for liquid container
        liquid_group_layout = QVBoxLayout()
        liquid_group_layout.addWidget(milk_button)
        liquid_group_layout.addWidget(water_button)

        liquid_group.setLayout(liquid_group_layout)
        tea_layout.addWidget(liquid_label)
        tea_layout.addWidget(liquid_group)
        tea_tab.setLayout(tea_layout)

        spice_label = QLabel('Select spices to add')
        tea_layout.addWidget(spice_label)

        # Creating spice container
        spice_box = QGroupBox()
        # Creating layout for spicebox
        spice_box_layout = QVBoxLayout()
        spice_box.setLayout(spice_box_layout)

        spices = ['sugar', 'clove', 'black pepper', 'cinamon', 'tumrmuric']
        for spice in spices:
            spice_check_box = QCheckBox(spice)
            spice_box_layout.addWidget(spice_check_box)

        tea_layout.addWidget(spice_box)


        main_layout = QVBoxLayout(self)
        main_layout.addWidget(tab_widget)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
