import os
import shutil

def cleanup_work_folder(self):
        work_folder = "workfolder"
        if os.path.exists(work_folder):
            shutil.rmtree(work_folder)
        if os.path.exists("icon_workfolder"):
            shutil.rmtree("icon_workfolder")

        assert os.path.exists(work_folder) == False
        assert os.path.exists("icon_workfolder") == False