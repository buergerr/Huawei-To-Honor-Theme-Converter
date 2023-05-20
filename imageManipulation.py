import os
import shutil
import zipfile
from PIL import Image


# Resize icon_small.jpg within the preview folder
def resize_icon_small_preview(work_folder):
    preview_folder = os.path.join(work_folder, "preview")
    icon_small_path = os.path.join(preview_folder, "icon_small.jpg")

    assert os.path.exists(icon_small_path) == True, "icon_small.jpg not found"

    # Perform the image resizing using a library of your choice (e.g., PIL, OpenCV)     
    image = Image.open(icon_small_path)
    resized_image = image.resize((510, 345))
    resized_image.save(icon_small_path)
  
    assert os.path.exists(icon_small_path) == True, "Resize failed"


                    