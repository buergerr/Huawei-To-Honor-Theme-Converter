import os
import shutil

def delete_work_folders(work_folder,contacts_folder,icon_workfolder, incallui_folder, mms_folder, phone_folder, systemui_folder, recorder_folder, telecom_folder, launcher_folder):
        if os.path.exists(work_folder):
            shutil.rmtree(work_folder)
        if os.path.exists(icon_workfolder):
            shutil.rmtree(icon_workfolder)
        if os.path.exists(contacts_folder):
            shutil.rmtree(contacts_folder)
        if os.path.exists(incallui_folder):
            shutil.rmtree(incallui_folder)
        if os.path.exists(mms_folder):
            shutil.rmtree(mms_folder)
        if os.path.exists(phone_folder):
            shutil.rmtree(phone_folder)
        if os.path.exists(systemui_folder):
            shutil.rmtree(systemui_folder)
        if os.path.exists(recorder_folder):
            shutil.rmtree(recorder_folder)
        if os.path.exists(telecom_folder):
            shutil.rmtree(telecom_folder)
        if os.path.exists(launcher_folder):
            shutil.rmtree(launcher_folder)
   


