from PIL import Image, ImageDraw, ImageFont
import xml.etree.ElementTree as ET
import zipfile
import shutil

def generate_previews():
    # ////////////////////////////////
    # Unzip Icons
    # ////////////////////////////////
    zip_file = "workfolder\icons"
    extract_folder = "workfolder\icons_preview"

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    xml_file = "com.hihonor.android.launcher/theme.xml"
    xml_file_system= "com.android.systemui/framework-res-hnext/theme.xml"

    # ////////////////////////////////
    # Generate Preview Widget 0 Texts
    # ////////////////////////////////

    def crop_and_paste(icon_preview_source_image, coordinates, icon_preview_destination_image):
        icon_preview_cropped_image = icon_preview_source_image.crop(coordinates)
        icon_preview_destination_image.paste(icon_preview_cropped_image, coordinates)

    def add_text_widget(image, text, font_size, coordinates, color):
        
        font = ImageFont.truetype("assets/Roboto-Regular.ttf", font_size)
        draw = ImageDraw.Draw(image)
        
        shadow_offset = (2, 2)
        shadow_coordinates = (coordinates[0] + shadow_offset[0], coordinates[1] + shadow_offset[1])
        draw.text(shadow_coordinates, text, font=font, fill="black")
        draw.text(coordinates, text, font=font, fill=color)

    homescreen_image = "workfolder\wallpaper\home_wallpaper_0.jpg"
    preview_widget_0_image = "workfolder\preview\preview_widget_0.jpg"
    preview_icons_0_image = "workfolder\preview\preview_icons_0.jpg"

    # Open the source image
    icon_preview_source_image = Image.open(homescreen_image)

     # Get the dimensions of the source image
    source_width, source_height = icon_preview_source_image.size

    # Coordinates for cropping image 1
    crop1_x1 = (source_width - 1080) // 2
    crop1_y1 = 840
    crop1_x2 = crop1_x1 + 1080
    crop1_y2 = crop1_y1 + 3000

    # Crop image 1
    icon_preview_cropped_image1 = icon_preview_source_image.crop((crop1_x1, crop1_y1, crop1_x2, crop1_y2))

    # Open the destination image
    icon_preview_destination_image = Image.open(preview_widget_0_image)

    # Coordinates for pasting cropped image 1
    paste1_x = 0
    paste1_y = 840

    # Paste image 1 onto the destination image
    icon_preview_destination_image.paste(icon_preview_cropped_image1, (paste1_x, paste1_y))
    


    tree = ET.parse(xml_file)
    root = tree.getroot()

    color_name_widget_text = root.find("color[@name='workspace_app_text_color']").text
    color_value_widget_text = color_name_widget_text[3:]  # Ignoriere die ersten beiden Zeichen "#"

    text_color = tuple(int(color_value_widget_text[i:i+2], 16) for i in (0, 2, 4))

    # first row of icons from left to right
    add_text_widget(icon_preview_destination_image, "Music", 34,            (120, 1085), text_color)
    add_text_widget(icon_preview_destination_image, "Reader", 34,           (355, 1085), text_color)
    add_text_widget(icon_preview_destination_image, "Themes", 34,           (605, 1085), text_color)
    add_text_widget(icon_preview_destination_image, "Wallet", 34,           (855, 1085), text_color)

    # second row of icons from left to right
    add_text_widget(icon_preview_destination_image, "Health", 34,           (120, 1389), text_color)
    add_text_widget(icon_preview_destination_image, "Game Center", 34,      (300, 1389), text_color)
    add_text_widget(icon_preview_destination_image, "Tips", 34,             (630, 1389), text_color)
    add_text_widget(icon_preview_destination_image, "Settings", 34,         (850, 1389), text_color)

    # third row of icons from left to right
    add_text_widget(icon_preview_destination_image, "Gallery", 34,          (120, 1700), text_color)
    add_text_widget(icon_preview_destination_image, "System Manager", 34,   (290, 1700), text_color)
    add_text_widget(icon_preview_destination_image, "Notepad", 34,          (600, 1700), text_color)
    add_text_widget(icon_preview_destination_image, "Smart Remote", 34,     (800, 1700), text_color)
    
    


    icon_preview_destination_image.save("workfolder\preview\preview_widget_0.jpg")


    # ////////////////////////////////
    # Generate Preview Icons O Texts
    # ////////////////////////////////


    def add_text_icons(image, text, font_size, coordinates, color):
        
        font = ImageFont.truetype("assets/Roboto-Regular.ttf", font_size)
        draw = ImageDraw.Draw(image)
        
        shadow_offset = (2, 2)
        shadow_coordinates = (coordinates[0] + shadow_offset[0], coordinates[1] + shadow_offset[1])
        draw.text(shadow_coordinates, text, font=font, fill="black")
        draw.text(coordinates, text, font=font, fill=color)


    # Open the source image
    icon_preview_source_image = Image.open(homescreen_image)

    # Get the dimensions of the source image
    source_width, source_height = icon_preview_source_image.size

    # Coordinates for cropping image 1
    crop1_x1 = (source_width - 1080) // 2
    crop1_y1 = 100
    crop1_x2 = crop1_x1 + 1080
    crop1_y2 = crop1_y1 + 3000

    # Crop image 1
    icon_preview_cropped_image1 = icon_preview_source_image.crop((crop1_x1, crop1_y1, crop1_x2, crop1_y2))

    # Open the destination image
    icon_preview_destination_image = Image.open(preview_icons_0_image)

    # Coordinates for pasting cropped image 1
    paste1_x = 0
    paste1_y = 100

    # Paste image 1 onto the destination image
    icon_preview_destination_image.paste(icon_preview_cropped_image1, (paste1_x, paste1_y))

    # Save the final image
    icon_preview_destination_image.save("workfolder\preview\preview_icons_0.jpg")   

    tree = ET.parse(xml_file)
    root = tree.getroot()

    color_name_widget_text = root.find("color[@name='workspace_app_text_color']").text
    color_value_widget_text = color_name_widget_text[3:]  # Ignoriere die ersten beiden Zeichen "#"

    text_color = tuple(int(color_value_widget_text[i:i+2], 16) for i in (0, 2, 4))

    # first row of icons from left to right
    add_text_icons(icon_preview_destination_image, "Settings", 34,      (112, 334), text_color)
    add_text_icons(icon_preview_destination_image, "Calculator", 34,    (336, 334), text_color)
    add_text_icons(icon_preview_destination_image, "GameCenter", 34,    (574, 334), text_color)
    add_text_icons(icon_preview_destination_image, "Email", 34,         (865, 334), text_color)
    # second row of icons from left to right
    add_text_icons(icon_preview_destination_image, "Recorder", 34,      (105, 643), text_color)     
    add_text_icons(icon_preview_destination_image, "HONOR Store", 34,   (324, 643), text_color)
    add_text_icons(icon_preview_destination_image, "Device Clone", 34,  (574, 643), text_color)
    add_text_icons(icon_preview_destination_image, "Calendar", 34,      (845, 643), text_color)
    # third row of icons from left to right
    add_text_icons(icon_preview_destination_image, "FM Radio", 34,      (100, 952), text_color)
    add_text_icons(icon_preview_destination_image, "Contacts", 34,      (340, 952), text_color)
    add_text_icons(icon_preview_destination_image, "Smart Remote", 34,  (555, 952), text_color)
    add_text_icons(icon_preview_destination_image, "SIM Toolkit", 34,   (830, 952), text_color)


    
    
    

    icon_preview_destination_image.save("workfolder\preview\preview_icons_0.jpg")

    # ////////////////////////////////
    # Generate Preview Icons 
    # ////////////////////////////////

    def resize_png(png_path, width, height):
        image = Image.open(png_path)
        resized_image = image.resize((width, height))
        resized_image.save(png_path)

    def insert_png_into_jpeg(jpeg_path, png_paths, positions):
        jpeg_image = Image.open(jpeg_path)

        for png_path, position in zip(png_paths, positions):
            png_image = Image.open(png_path).convert("RGBA")
            jpeg_image.paste(png_image, position, png_image)

        jpeg_image.save(jpeg_path)

    # resize all pngs
    resize_x = 182
    resize_y = 182

    icon_list = [
    "com.android.chrome.png",
    "com.android.contacts.activities.DialtactsActivity.png",
    "com.android.mediacenter.png",
    "com.android.settings.png",
    "com.android.stk.StkLauncherActivity2.png",
    "com.google.android.apps.messaging.png",
    "com.hihonor.android.clone.png",
    "com.hihonor.android.FMRadio.png",
    "com.hihonor.android.remotecontroller.png",
    "com.hihonor.android.thememanager.png",
    "com.hihonor.android.tips.png",
    "com.hihonor.calculator.png",
    "com.hihonor.camera.png",
    "com.hihonor.contacts.png",
    "com.hihonor.email.png",
    "com.hihonor.gamebox.png",
    "com.hihonor.health.png",
    "com.hihonor.calendar",
    "com.hihonor.hstore.global.png",
    "com.hihonor.hwireader.png",
    "com.hihonor.notepad.png",
    "com.hihonor.photos.png",
    "com.hihonor.soundrecorder.png",
    "com.hihonor.systemmanager.png",
    "com.hihonor.wallet.png"
    "com.hihonor.filemanager.png"
    ]
    
    # go through all icons and resize them. continue even if an error occurs
    for icon in icon_list:
        try:
            resize_png("workfolder\icons_preview\\" + icon, resize_x, resize_y)
        except:
            print("Error while resizing " + icon)


    # insert all icons into the widget preview image
    widget_jpeg_path = "workfolder\preview\preview_widget_0.jpg"
    widget_png_paths = [
        # first row
        "workfolder\icons_preview\com.android.mediacenter.png",
        "workfolder\icons_preview\com.hihonor.hwireader.png",
        "workfolder\icons_preview\com.hihonor.android.thememanager.png",
        "workfolder\icons_preview\com.hihonor.wallet.png",
        # second row
        "workfolder\icons_preview\com.hihonor.health.png",
        "workfolder\icons_preview\com.hihonor.gamecenter.png",
        "workfolder\icons_preview\com.hihonor.tips.png",
        "workfolder\icons_preview\com.android.settings.png",
        # third row
        "workfolder\icons_preview\com.hihonor.photos.png",
        "workfolder\icons_preview\com.hihonor.systemmanager.png",
        "workfolder\icons_preview\com.hihonor.notepad.png",
        "workfolder\icons_preview\com.hihonor.android.remotecontroller.png",
        # fourth row
        "workfolder\icons_preview\com.android.contacts.activities.DialtactsActivity.png",
        "workfolder\icons_preview\com.google.android.apps.messaging.png",
        "workfolder\icons_preview\com.android.chrome.png",
        "workfolder\icons_preview\com.hihonor.camera.png"
        
    ]
    widget_positions = [
        # first row
        (77,880), # 1 media center
        (322,880), # 2 hwireader
        (574, 880), # 3 theme manager
        (817, 880), # 4 wallet
        # second row
        (77, 1190), # health
        (322, 1190), # game center
        (574, 1190), # tips
        (817, 1190), # settings
        # third row
        (77, 1500), # gallery
        (322, 1500), # system manager
        (574, 1500), # notepad
        (817, 1500), # remote controller
        # fourth row
        (77, 1870), # phone
        (322, 1870), # messages
        (574, 1870), # chrome
        (817, 1870) # camera
         
    ]
    
    insert_png_into_jpeg(widget_jpeg_path, widget_png_paths, widget_positions)

    # insert all icons into the icon preview image
    systemui_jpeg_path = "workfolder\preview\preview_icons_0.jpg"
    systemui_png_paths = [
        # first row
        "workfolder\icons_preview\com.android.settings.png", 
        "workfolder\icons_preview\com.hihonor.calculator.png",
        "workfolder\icons_preview\com.hihonor.gamecenter.png",
        "workfolder\icons_preview\com.hihonor.email.png",
        # second row
        "workfolder\icons_preview\com.hihonor.soundrecorder.png", 
        "workfolder\icons_preview\com.hihonor.hstore.global.png",
        "workfolder\icons_preview\com.hihonor.android.clone.png",
        "workfolder\icons_preview\com.android.calendar.png",
        # third row
        "workfolder\icons_preview\com.hihonor.android.FMRadio.png",
        "workfolder\icons_preview\com.hihonor.contacts.png",
        "workfolder\icons_preview\com.hihonor.android.remotecontroller.png",
        "workfolder\icons_preview\com.android.stk.StkLauncherActivity2.png",
        # fourth row
        "workfolder\icons_preview\com.android.contacts.activities.DialtactsActivity.png",
        "workfolder\icons_preview\com.google.android.apps.messaging.png",
        "workfolder\icons_preview\com.android.chrome.png",
        "workfolder\icons_preview\com.hihonor.camera.png"
    ]
    systemui_positions = [
        # first row
        (77, 136), # 1 settings
        (322, 136), # 2 calculator
        (574, 136), # 3 game center
        (817, 136), # 4 email
        # second row
        (77, 446), # 5 sound recorder
        (322, 446), # 6 app gallery
        (574, 446), # 7 phone clone
        (817, 446), # 8 file manager
        # third row
        (77, 750), # 9 fm radio
        (322, 750), # 10 contacts
        (574, 750), # 11 remote controller
        (817, 750), # 12 sim toolkit
        # fourth row
        (77, 1870), # 13 phone
        (322, 1870), # 14 messages
        (574, 1870), # 15 chrome
        (817, 1870), # 16 camera

    ]
    insert_png_into_jpeg(systemui_jpeg_path, systemui_png_paths, systemui_positions)


    # ////////////////////////////////
    # Generate Preview Systm UI
    # ////////////////////////////////


    def crop_and_paste(system_preview_source_image, coordinates, system_preview_destination_image):
        system_preview_cropped_image = system_preview_source_image.crop(coordinates)
        system_preview_destination_image.paste(system_preview_cropped_image, coordinates)

    def add_text_system(image, text, font_size, coordinates, color):
        font = ImageFont.truetype("assets/Roboto-Regular.ttf", font_size)
        draw = ImageDraw.Draw(image)
        draw.text(coordinates, text, font=font, fill=color)

    system_preview_source_image = Image.open("workfolder\preview\preview_systemui_0.jpg")
    system_preview_crop_coordinates1 = (317, 812, 317 + 213, 812 + 35)
    system_preview_cropped_image1 = system_preview_source_image.crop(system_preview_crop_coordinates1)

    system_preview_destination_image = Image.open("workfolder\preview\preview_systemui_0.jpg")
    system_preview_paste_coordinates1 = (317, 843)
    system_preview_destination_image.paste(system_preview_cropped_image1, system_preview_paste_coordinates1)

    tree = ET.parse(xml_file_system)
    root = tree.getroot()

    color_name_system_text = root.find("color[@name='magic_primary']").text
    color_value_system_text = color_name_system_text[3:]  # Ignoriere die ersten beiden Zeichen "#"

    text_color = tuple(int(color_value_system_text[i:i+2], 16) for i in (0, 2, 4))

    add_text_system(system_preview_destination_image, "HONOR Share", 38, (319, 839), text_color)

    system_preview_destination_image.save("workfolder\preview\preview_systemui_0.jpg")

    # ////////////////////////////////
    # Delete Temp Files
    # ////////////////////////////////

    folder_to_delete = "workfolder/icons_preview"
    shutil.rmtree(folder_to_delete)