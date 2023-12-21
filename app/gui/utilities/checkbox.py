def checkbox(parent, geometry):
    checkbox = QCheckBox(parent)
    checkbox.setGeometry(*geometry)
    checkbox.setStyleSheet("QCheckBox::indicator{width: 20px;height: 20px;} QCheckBox::indicator:pressed{background-color: orange;}")
    return checkbox