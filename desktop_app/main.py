import sys
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView

class LauncherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sp3xtr0 - App Launcher & Control Panel")
        self.resize(1100, 750)

        # Widget principal y Layout
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Barra superior ultradelgada con botón de inicio
        top_bar = QWidget()
        top_bar.setStyleSheet("background-color: #0b0b0b; border-bottom: 1px solid #eab308; min-height: 40px; max-height: 40px;")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(15, 4, 15, 4)

        home_btn = QPushButton("🏠 Menú Principal")
        home_btn.setStyleSheet("""
            QPushButton {
                background-color: #eab308;
                color: #000000;
                font-weight: 800;
                border-radius: 6px;
                padding: 4px 12px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #facc15;
            }
        """)
        home_btn.clicked.connect(self.go_home)
        top_layout.addWidget(home_btn)
        top_layout.addStretch()

        # 0 = la barra mide solo lo necesario (40px)
        layout.addWidget(top_bar, 0)

        # 1 = el navegador ocupa todo el resto del espacio de la ventana
        self.browser = QWebEngineView()
        layout.addWidget(self.browser, 1)

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
