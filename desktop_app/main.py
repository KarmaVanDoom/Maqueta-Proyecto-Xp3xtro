import sys
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView

class LauncherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sp3xtr0 - App Launcher & Control Panel")
        self.resize(1000, 700)

        # Widget principal y Layout
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Barra superior con botón de inicio
        top_bar = QWidget()
        top_bar.setStyleSheet("background-color: #0f0f0f; border-bottom: 1px solid #eab308;")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(10, 5, 10, 5)

        home_btn = QPushButton("🏠 Menú Principal")
        home_btn.setStyleSheet("""
            QPushButton {
                background-color: #eab308;
                color: #000000;
                font-weight: bold;
                border-radius: 5px;
                padding: 6px 14px;
            }
            QPushButton:hover {
                background-color: #facc15;
            }
        """)
        home_btn.clicked.connect(self.go_home)
        top_layout.addWidget(home_btn)
        top_layout.addStretch()

        layout.addWidget(top_bar)

        # Navegador WebEngine dentro de la ventana de escritorio
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        self.setCentralWidget(main_widget)

        # Cargar launcher inicial
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_file = os.path.join(self.base_dir, 'templates', 'index.html')
        self.go_home()

    def go_home(self):
        self.browser.setUrl(QUrl.fromLocalFile(self.html_file))

def start_app():
    app = QApplication(sys.argv)
    window = LauncherApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    start_app()
