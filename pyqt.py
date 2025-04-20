import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QPushButton

# Create app instance
app = QApplication(sys.argv)

# Create main window
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 300, 200)

# Add a label widget
label = QLabel("Hello PyQt!", parent=window)
label.move(50, 50)


# Create a button and connect it to show message slot
def showmessage():
    QMessageBox.information(None, "Message", "Button Clicked!")


button = QPushButton("Click ME!", parent=window)
button.move(50, 100)
button.clicked.connect(showmessage)

# Show window
window.show()

# Exit when the application is closed
sys.exit(app.exec_())
