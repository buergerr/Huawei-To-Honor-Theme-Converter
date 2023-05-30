import os
import shutil
from PyQt5.QtWidgets import QMessageBox

def delete_work_folders(folder):
        if os.path.exists(folder):
            shutil.rmtree(folder)
        if os.path.exists("icon_workfolder"):
            shutil.rmtree("icon_workfolder")

# display a messagebox to inform the user that he needs to verify the previews
def display_messagebox():
    msg = QMessageBox()
    msg.setWindowTitle("Verify Previews")
    msg.setText("Please verify the previews and close the folder afterwards.")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()