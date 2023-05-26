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

# create a function for the AOD cover image that needs to be enlarded by 1080x2160, background color is black
def resize_aod_cover(work_folder):
    preview_folder = os.path.join(work_folder, "preview")
    aod_cover_path = os.path.join(preview_folder, "cover_aod.jpg")

    assert os.path.exists(aod_cover_path) == True, "cover_aod.jpg not found"

    new_size = (1080, 1920)
    background_color = (0, 0, 0)  # Black color

    # Perform the image resizing using PIL (Python Imaging Library)
    image = Image.open(aod_cover_path)
    resized_image = image.resize(new_size, Image.ANTIALIAS)

    # Create a new image with 1920x2160 with the specified background color and paste the resized image onto it
    new_image = Image.new("RGB", (new_size[0], new_size[1] + 240), background_color)
    new_image.paste(resized_image, (0, 120))
    

    # Save the resized and modified image
    resized_aod_cover_path = os.path.join(preview_folder, "cover_aod.jpg")
    new_image.save(resized_aod_cover_path)

    assert os.path.exists(resized_aod_cover_path) == True, "Failed to resize AOD cover image"



                    