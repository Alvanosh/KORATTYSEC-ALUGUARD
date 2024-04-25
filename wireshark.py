import sys
import os
import time
import threading
import scapy.all as scapy
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread

class PacketSniffer(QThread):
    packet_received = pyqtSignal(str)

    def __init__(self, interface, display_filter=None):
        super().__init__()
        self.interface = interface
        self.display_filter = display_filter

    def run(self):
        try:
            scapy.sniff(iface=self.interface, prn=self.process_packet, filter=self.display_filter)
        except Exception as e:
            print("Error:", e)

    def process_packet(self, packet):
        self.packet_received.emit(str(packet))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced Packet Sniffer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.interface_label = QLabel("Interface:")
        self.layout.addWidget(self.interface_label)

        self.interface_input = QLineEdit()
        self.layout.addWidget(self.interface_input)

        self.display_filter_label = QLabel("Display Filter:")
        self.layout.addWidget(self.display_filter_label)

        self.display_filter_input = QLineEdit()
        self.layout.addWidget(self.display_filter_input)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_sniffer)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_sniffer)
        self.layout.addWidget(self.stop_button)
        self.stop_button.setDisabled(True)

        self.log_label = QLabel("Log:")
        self.layout.addWidget(self.log_label)

        self.log_textedit = QTextEdit()
        self.log_textedit.setReadOnly(True)
        self.layout.addWidget(self.log_textedit)

        self.sniffer = None

    def start_sniffer(self):
        interface = self.interface_input.text()
        if not interface:
            self.log_message("Please enter an interface.")
            return

        display_filter = self.display_filter_input.text()

        self.sniffer = PacketSniffer(interface, display_filter)
        self.sniffer.packet_received.connect(self.handle_packet_received)
        self.sniffer.start()

        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)

        self.log_message(f"Sniffing started on interface {interface}.")

    def stop_sniffer(self):
        if self.sniffer:
            self.sniffer.terminate()
            self.sniffer.wait()
            self.sniffer = None

            self.start_button.setEnabled(True)
            self.stop_button.setDisabled(True)

            self.log_message("Sniffing stopped.")

    def handle_packet_received(self, packet):
        self.log_message(packet)

    def log_message(self, message):
        self.log_textedit.append(message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
