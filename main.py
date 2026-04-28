import sys
import os

os.environ["QT_QPA_PLATFORM"] = "xcb"

import vlc
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QFrame
from PyQt6.QtCore import Qt

class Player(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VLC Qt Player")

        self.video_frame = QFrame()
        self.video_frame.setStyleSheet("background: black;")

        self.button = QPushButton("Play")
        self.button.clicked.connect(self.play)

        layout = QVBoxLayout()
        layout.addWidget(self.video_frame)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def play(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Video")
        if not file:
            return

        media = self.instance.media_new(file)
        self.player.set_media(media)

        # Embed VLC into the Qt widget
        win_id = int(self.video_frame.winId())

        if sys.platform.startswith("linux"):
            self.player.set_xwindow(win_id)
        elif sys.platform == "win32":
            self.player.set_hwnd(win_id)
        elif sys.platform == "darwin":
            self.player.set_nsobject(win_id)

        self.player.play()

def main():
    app = QApplication(sys.argv)
    window = Player()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()