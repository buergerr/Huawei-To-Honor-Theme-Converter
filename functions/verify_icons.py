import os
import sys
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import shutil


app_packages = [
            "com.hihonor.notepad",
            "com.hihonor.email",
            "com.hihonor.android.clone",
            "com.hihonor.calculator",
            "com.hihonor.mirror",
            "com.hihonor.contacts",
            "com.hihonor.soundrecorder",
            "com.hihonor.calendar",
            #"com.hihonor.hstore.global",
            "com.hihonor.deskclock",
            "com.hihonor.android.totemweather",
            "com.hihonor.photos",
            "com.hihonor.tips",
            "com.hihonor.filemanager",
            "com.hihonor.phoneservice",
            "com.hihonor.camera",
            "com.hihonor.android.thememanager",
            #"com.hihonor.appmarket",
            "com.hihonor.gamecenter",
            "com.hihonor.compass",
            "com.android.settings",
            "com.hihonor.systemmanager",
            "com.google.android.apps.messaging",
            "com.android.chrome",
            "com.google.android.googlequicksearchbox",
            "com.google.android.gm",
            "com.google.android.apps.maps",
            "com.google.android.youtube",
            "com.google.android.apps.docs",
            "com.google.android.apps.youtube.music",
            "com.google.android.apps.tachyon",
            "com.google.android.apps.photos",
            "com.android.vending",
            "com.google.android.videos",
            "com.android.calendar"
        ]

def upload_icons(icons_folder):
    # Code to upload missing icons to the icons_workfolder goes here
    # Open a file dialog to select the icon files
    # Copy the icons to the icons_workfolder

    def upload_icons_to_workfolder():
        # Open a file dialog to select the icon files
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("PNG Files (*.png)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for selected_file in selected_files:
                # Copy the icons to the icons_workfolder
                shutil.copy(selected_file, icons_folder)

    upload_icons_to_workfolder()



    
    # After uploading the icons, show a success message box
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Icons uploaded successfully!")
    msg.setWindowTitle("Upload Icons")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

# check if icons are missing from the icons_workfolder.
# compare the icon file names with the app_packages list and return the missing icons
# return missing icons in a GUI message box
# add an upload button to the GUI message box to upload the missing icons to the icons_workfolder
# if the user clicks ok the file dialog will open to select the icons folder
# display sample icons for the missing icons in the GUI message box /assets/icons/

def check_icons_in_workfolder(icons_folder):
    missing_icons = []
    for package in app_packages:
        icon_path = os.path.join(icons_folder, package + ".png")
        if not os.path.exists(icon_path):
            missing_icons.append(package)
    if len(missing_icons) > 0:
        missing_icons_str = "\n".join(missing_icons)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(" Upload missing Icons now!")
        msg.setInformativeText("The following icons are missing from the icons folder:\n\n" + missing_icons_str)
        msg.setWindowTitle("Missing Icons")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec_() == QMessageBox.Ok:
            upload_icons(icons_folder)
        else:
            sys.exit()
    else:
        pass    
    return missing_icons

# Pause the app until all missing icons are uploaded
# Continue the app after all missing icons are uploaded
# Continue the app if no icons are missing
def pause_if_icons_missing(icons_folder):
    missing_icons = check_icons_in_workfolder(icons_folder)
    if len(missing_icons) > 0:
        while len(missing_icons) > 0:
            missing_icons = check_icons_in_workfolder(icons_folder)
    else:
        pass


# open icon_workfolder in file explorer and display a messagebox, after confirming the messagebox the app will continue
def open_icons_workfolder(icons_folder):
    os.startfile(icons_folder)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Please check for HUAWEI related texts in icons (com.vmall.client) and replace them with HONOR.\n And add Google Icons")
    msg.setWindowTitle("Check for Huawei")
    msg.setStandardButtons(QMessageBox.Ok)
    # pause until the user clicks ok
    while msg.exec_() == QMessageBox.Ok:
        break