import os
import shutil
import zipfile
from PIL import Image


# Unzip .hwt file into work folder   
def unzip_hwt(file_path, work_folder):
           
    os.makedirs(work_folder, exist_ok=True)
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(work_folder)
            
    assert os.path.exists(work_folder) == True, "Unzip failed"
   

# Rename files
def rename_files(work_folder, old_filename, new_filename):
    old_file_path = os.path.join(work_folder, old_filename)
    new_file_path = os.path.join(work_folder, new_filename)
    os.rename(old_file_path, new_file_path)
    assert os.path.exists(new_file_path) == True, "Rename failed"

# Unzip icons file within the workfolder with shutil
def unzip_icons(work_folder,icon_file_name,icons_folder,archive_format):    
    shutil.unpack_archive(os.path.join(work_folder, icon_file_name), icons_folder, archive_format)
    assert os.path.exists(icons_folder) == True, "Unzip icons failed"

# Zip icon files and all folders within the icon_folder into "icons" file
def zip_icons(work_folder,icon_file_name,icons_folder, archive_format):
    shutil.make_archive(os.path.join(work_folder, icon_file_name), archive_format, icons_folder)    
    assert os.path.exists(os.path.join(work_folder, icon_file_name + "." + archive_format)) == True, "Zip icons failed"

# Rename icon files that starts with "com.huawei" or "com.hicloud" to "com.hihonor"
def rename_icons(work_folder,icons_folder):
    for root, dirs, files in os.walk(icons_folder):
        for file in files:
            if file.startswith("com.huawei") or file.startswith("com.hicloud"):
                old_file = os.path.join(root, file)
                new_file = os.path.join(root, file.replace("com.huawei.music", "com.google.android.apps.youtube.music").replace("com.huawei", "com.hihonor").replace("com.hicloud", "com.hihonor").replace("com.hihonor.tipsove", "com.hihonor.tips"))
                os.rename(old_file, new_file)
                assert os.path.exists(new_file) == True, "Rename Icons huwei to hihonor failed"

# delete workfolder/preview/preview_mms_0.jpg if it exists
def delete_preview_mms(work_folder):
    if os.path.exists(os.path.join(work_folder, "preview/preview_mms_0.jpg")):
        os.remove(os.path.join(work_folder, "preview/preview_mms_0.jpg"))
        assert os.path.exists(os.path.join(work_folder, "preview/preview_mms_0.jpg")) == False, "Delete preview_mms_0.jpg failed"
    else:
        pass

    

# copy com.hihonor.appmarket.png from icons_folder into icons_folder and rename it to com.hihonor.hstore.global.png
def copy_appmarket(icons_folder):
    shutil.copy(os.path.join(icons_folder, "com.vmall.client.png"), os.path.join(icons_folder, "com.hihonor.hstore.global.png"))
    assert os.path.exists(os.path.join(icons_folder, "com.hihonor.hstore.global.png")) == True, "Copy Hstore Icons failed"
    # delete com.hihonor.appmarket.png from icons_folder
    os.remove(os.path.join(icons_folder, "com.hihonor.appmarket.png"))
    shutil.copy(os.path.join(icons_folder, "com.vmall.client.png"), os.path.join(icons_folder, "com.hihonor.appmarket.png"))
    assert os.path.exists(os.path.join(icons_folder, "com.hihonor.appmarket.png")) == True, "Copy AppMarket Icons failed"




# rename folder within icons folder /dynamic_icons/com.huawei.android.totemweather to /dynamic_icons/com.hihonor.android.totemweather or continue if folder does not exist
    old_folder = os.path.join(icons_folder, "dynamic_icons/com.huawei.android.totemweather")
    new_folder = os.path.join(icons_folder, "dynamic_icons/com.hihonor.android.totemweather")
    if os.path.exists(old_folder):
        os.rename(old_folder, new_folder)
        assert os.path.exists(new_folder) == True, "Rename 'totemweather'failed"
    else:
        pass


# rename folder within icons folder com.android.deskclock OR com.huawei.deskclock to /dynamic_icons/com.hihonor.deskclock or continue if folder does not exist
    old_folder = os.path.join(icons_folder, "dynamic_icons/com.android.deskclock")
    new_folder = os.path.join(icons_folder, "dynamic_icons/com.hihonor.deskclock")
    if os.path.exists(old_folder):
        os.rename(old_folder, new_folder)        
    elif os.path.exists(os.path.join(icons_folder, "dynamic_icons/com.huawei.deskclock")):
        old_folder = os.path.join(icons_folder, "dynamic_icons/com.huawei.deskclock")
        new_folder = os.path.join(icons_folder, "dynamic_icons/com.hihonor.deskclock")
        os.rename(old_folder, new_folder)
        assert os.path.exists(new_folder) == True, "Rename 'deskclock'failed"
    else:
        pass
        
  



# delete original icon file
def delete_icons_file (work_folder,icon_file_name):      
    os.remove(os.path.join(work_folder, icon_file_name))
    assert os.path.exists(os.path.join(work_folder, icon_file_name)) == False, "Delete icon file failed"

#remove .zip extension from the file
def remove_icons_zip_extension(work_folder,icon_file_name,archive_format):
    os.rename(os.path.join(work_folder, icon_file_name + "." + archive_format), os.path.join(work_folder, icon_file_name))
    assert os.path.exists(os.path.join(work_folder, icon_file_name + "." + archive_format)) == False, "Remove Zip from Icons.zip failed"        

# Delete icon workspace
def delete_icons_workspace(icons_folder):
    shutil.rmtree(icons_folder)
    assert os.path.exists(icons_folder) == False, "Delete failed"

# Unzip com.android.contacts file within the workfolder with shutil
def unzip_contacts(work_folder,icon_file_name,contacts_folder,archive_format):    
    shutil.unpack_archive(os.path.join(work_folder, icon_file_name), contacts_folder, archive_format)
    assert os.path.exists(contacts_folder) == True, "Unzip icons failed"

# iterate through the png files in the folders and rename them from "emui" to "magic"
def rename_framework_pngs(folders,):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".png"):
                    old_file = os.path.join(root, file)
                    new_file = os.path.join(root, file.replace("emui", "magic"))
                    os.rename(old_file, new_file)
                    assert os.path.exists(new_file) == True, "Rename Icons huwei to hihonor failed"



  