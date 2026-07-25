import sys
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView

class ExternalBrowserPage(QWebEnginePage):
    """Página personalizada que abre enlaces web externos en el navegador por defecto del sistema."""
    def acceptNavigationRequest(self, url, nav_type, is_main_frame):
        url_str = url.toString()
        # Si el enlace es HTTP o HTTPS, abrir en navegador por defecto (Chrome, Edge, etc)
        if url_str.startswith("http://") or url_str.startswith("https://"):
            QDesktopServices.openUrl(url)
            return False  # No navegar dentro del launcher
        return super().acceptNavigationRequest(url, nav_type, is_main_frame)

def start_app():
    app = QApplication(sys.argv)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(base_dir, 'templates', 'index.html')
    
    view = QWebEngineView()
    page = ExternalBrowserPage(view)
    view.setPage(page)
    
    view.setWindowTitle("Sp3xtr0 - Launcher Oficial")
    view.resize(850, 580)
    
    # Carga la interfaz visual HTML original
    view.setUrl(QUrl.fromLocalFile(html_file))
    view.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    start_app()
