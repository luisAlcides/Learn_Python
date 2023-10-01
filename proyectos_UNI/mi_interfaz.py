import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QTextBrowser
import ipaddress

class IPSubnetCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IP Subnet Calculator")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.form_layout = QFormLayout()

        self.ip_label = QLabel("IP Address:")
        self.ip_input = QLineEdit()
        self.form_layout.addRow(self.ip_label, self.ip_input)

        self.subnet_label = QLabel("Subnet Mask:")
        self.subnet_input = QLineEdit()
        self.form_layout.addRow(self.subnet_label, self.subnet_input)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        self.form_layout.addRow(self.calculate_button)

        self.result_text = QTextBrowser()
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.result_text)

    def calculate(self):
        ip = self.ip_input.text()
        subnet = self.subnet_input.text()

        try:
            network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
        except ValueError:
            self.result_text.setText("Invalid IP or Subnet Mask")
            return

        num_subnets = 2 ** (32 - network.prefixlen)

        self.result_text.clear()
        self.result_text.append(f"IP Address: {network.network_address}")
        self.result_text.append(f"Network Address: {network.network_address}")
        self.result_text.append(f"Usable Host IP Range: {network.network_address + 1} - {network.broadcast_address - 1}")
        self.result_text.append(f"Broadcast Address: {network.broadcast_address}")
        self.result_text.append(f"Total Number of Hosts: {network.num_addresses}")
        self.result_text.append(f"Number of Usable Hosts: {network.num_addresses - 2}")
        self.result_text.append(f"Subnet Mask: {network.netmask}")
        self.result_text.append(f"Wildcard Mask: {network.hostmask}")
        self.result_text.append(f"Binary Subnet Mask: {network.netmask.exploded.replace('0', '1').replace('1', '0')}")
        ipclass = network.network_address.exploded.split('.')[0]
        if ipclass < '128':
            self.result_text.append(f"IP Class: A")
        elif ipclass < '192':
            self.result_text.append(f"IP Class: B")
        elif ipclass < '224':
            self.result_text.append(f"IP Class: C")
        self.result_text.append(f"Prefix: /{network.prefixlen}")
        self.result_text.append(f"Number of Subnets: {num_subnets}")

        self.result_text.append("\nSubnet Table:")
        self.result_text.append("\nNetwork Addres\t Usable HOST\t Brodcast Addres ")
        subnets_displayed = 0
        for subnet in network.subnets():
            self.result_text.append(f"{subnet.network_address}\t{subnet.network_address + 1} - {subnet.broadcast_address - 1}\t{subnet.broadcast_address}")
            subnets_displayed += 1
            if subnets_displayed >= 8:
                break

def main():
    app = QApplication(sys.argv)
    window = IPSubnetCalculator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
