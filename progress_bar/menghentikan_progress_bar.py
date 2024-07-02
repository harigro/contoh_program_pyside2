import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar
from PySide2.QtCore import QThread, Signal
import time

class WorkerThread(QThread):
    progress_update = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False

    def run(self):
        length = 100
        self.running = True
        for i in range(length):
            time.sleep(0.1)  # Simulating work
            if not self.running:
                break
            self.progress_update.emit(int((i + 1) * 100 / length))
        self.running = False

    def stop(self):
        self.running = False
        self.wait()  # Wait for the thread to finish

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random String Generation")
        self.setGeometry(200, 200, 300, 150)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)

        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.start_generation)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

        self.worker_thread = None  # Initialize worker_thread attribute

    def start_generation(self):
        if self.worker_thread is not None and self.worker_thread.isRunning():
            self.worker_thread.stop()
        self.progress_bar.setValue(0)
        self.worker_thread = WorkerThread()
        self.worker_thread.progress_update.connect(self.update_progress)
        self.worker_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def closeEvent(self, event):
        if self.worker_thread is not None and self.worker_thread.isRunning():
            self.worker_thread.stop()
            self.worker_thread.wait()  # Wait for the thread to finish
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

