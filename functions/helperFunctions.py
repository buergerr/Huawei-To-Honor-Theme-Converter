import os
import shutil

def delete_work_folders(folder):
        if os.path.exists(folder):
            shutil.rmtree(folder)
        if os.path.exists("icon_workfolder"):
            shutil.rmtree("icon_workfolder")

   


