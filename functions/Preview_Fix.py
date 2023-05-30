from PIL import Image, ImageDraw, ImageFont
import xml.etree.ElementTree as ET
import zipfile
import shutil

def generate_previews():
    # Unzip Icons
    zip_file = "workfolder/icons"
    extract_folder = "workfolder/icons_preview"

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    xml_file = "com.hihonor.android.launcher/theme.xml"
    xml_file_system = "com.android.systemui/framework-res-hnext/theme.xml"

    def crop_and_paste(icon_preview_source_image, coordinates, icon_preview_destination_image):
        icon_preview_cropped_image = icon_preview_source_image.crop(coordinates)
        icon_preview_destination_image.paste(icon_preview_cropped_image, coordinates)

    def add_text(image, text, font_size, coordinates, color):
        font = ImageFont.truetype("assets/Roboto-Regular.ttf", font_size)
        draw = ImageDraw.Draw(image)
        draw.text(coordinates, text, font=font, fill=color)

    # Generate Preview Widget 0 Texts
    icon_preview_source_image = Image.open("workfolder/wallpaper/home_wallpaper_0.jpg")
    icon_preview_crop_coordinates1 = (849, 1176, 849 + 483, 1176 + 279)
    icon_preview_cropped_image1 = icon_preview_source_image.crop(icon_preview_crop_coordinates1)
    icon_preview_destination_image = Image.open("workfolder/preview/preview_widget_0.jpg")
    icon_preview_paste_coordinates1 = (308, 1176)

    icon_preview_destination_image.paste(icon_preview_cropped_image1, icon_preview_paste_coordinates1)
    icon_preview_crop_coordinates2 = (1365, 1692, 1365 + 209, 1692 + 64)
    icon_preview_cropped_image2 = icon_preview_source_image.crop(icon_preview_crop_coordinates2)
    icon_preview_paste_coordinates2 = (825, 1692)
    icon_preview_destination_image.paste(icon_preview_cropped_image2, icon_preview_paste_coordinates2)

    tree = ET.parse(xml_file)
    root = tree.getroot()

    color_name_widget_text = root.find("color[@name='widget_text_color']").text
    color_value_widget_text = color_name_widget_text[2:]  # Ignore the first two characters "#"

    text_color = tuple(int(color_value_widget_text[i:i + 2], 16) for i in (0, 2, 4))

    add_text(icon_preview_destination_image, "Game Center", 34, (333, 1389), text_color)
    add_text(icon_preview_destination_image, "Tips", 34, (630, 1389), text_color)
    add_text(icon_preview_destination_image, "Smart Remote", 34, (811, 1700), text_color)
    icon_preview_destination_image.save("workfolder/preview/preview_widget_0.jpg")

    # Generate Preview Icons O Texts
    icon_preview_source_image = Image.open("workfolder/wallpaper/home_wallpaper_0.jpg")
    icon_preview_crop_coordinates1 = (540, 88, 540 + 540, 88 + 629)
    icon_preview_cropped_image1 = icon_preview_source_image.crop(icon_preview_crop_coordinates1)

    icon_preview_destination_image = Image.open("workfolder/preview/preview_icons_0.jpg")
    icon_preview_paste_coordinates1 = (0, 88)
    icon_preview_destination_image.paste(icon_preview_cropped_image1, icon_preview_paste_coordinates1)

    tree = ET.parse(xml_file)
    root = tree.getroot()

    color_name_widget_text = root.find("color[@name='widget_text_color']").text
    color_value_widget_text = color_name_widget_text[2:]  # Ignore the first two characters "#"

    text_color = tuple(int(color_value_widget_text[i:i + 2], 16) for i in (0, 2, 4))

    add_text(icon_preview_destination_image, "Settings", 34, (112, 334), text_color)
    add_text(icon_preview_destination_image, "Calculator", 34, (336, 334), text_color)
    add_text(icon_preview_destination_image, "Recorder", 34, (105, 643), text_color)
    add_text(icon_preview_destination_image, "Honor Store", 34, (334, 643), text_color)

    icon_preview_destination_image.save("workfolder/preview/preview_icons_0.jpg")

    # Generate Preview Icons
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

    resize_png("workfolder/icons_preview/com.hihonor.gamecenter.png", 182, 182)
    resize_png("workfolder/icons_preview/com.hihonor.tips.png", 182, 182)
    resize_png("workfolder/icons_preview/com.hihonor.android.remotecontroller.png", 182, 182)
    resize_png("workfolder/icons_preview/com.android.chrome.png", 182, 182)
    resize_png("workfolder/icons_preview/com.android.settings.png", 182, 182)
    resize_png("workfolder/icons_preview/com.hihonor.calculator.png", 182, 182)
    resize_png("workfolder/icons_preview/com.hihonor.soundrecorder.png", 182, 182)
    resize_png("workfolder/icons_preview/com.hihonor.appmarket.png", 182, 182)

    widget_jpeg_path = "workfolder/preview/preview_widget_0.jpg"
    widget_png_paths = [
        "workfolder/icons_preview/com.hihonor.gamecenter.png",
        "workfolder/icons_preview/com.hihonor.tips.png",
        "workfolder/icons_preview/com.hihonor.android.remotecontroller.png",
        "workfolder/icons_preview/com.android.chrome.png"
    ]
    widget_positions = [(322, 1190), (570, 1190), (817, 1500), (574, 1870)]
    insert_png_into_jpeg(widget_jpeg_path, widget_png_paths, widget_positions)

    systemui_jpeg_path = "workfolder/preview/preview_icons_0.jpg"
    systemui_png_paths = [
        "workfolder/icons_preview/com.android.settings.png",
        "workfolder/icons_preview/com.hihonor.calculator.png",
        "workfolder/icons_preview/com.hihonor.soundrecorder.png",
        "workfolder/icons_preview/com.hihonor.appmarket.png"
    ]
    systemui_positions = [(79, 136), (325, 136), (79, 446), (325, 446)]
    insert_png_into_jpeg(systemui_jpeg_path, systemui_png_paths, systemui_positions)

    # Generate Preview System UI
    def crop_and_paste(system_preview_source_image, coordinates, system_preview_destination_image):
        system_preview_cropped_image = system_preview_source_image.crop(coordinates)
        system_preview_destination_image.paste(system_preview_cropped_image, coordinates)

    def add_text(image, text, font_size, coordinates, color):
        font = ImageFont.truetype("assets/Roboto-Regular.ttf", font_size)
        draw = ImageDraw.Draw(image)
        draw.text(coordinates, text, font=font, fill=color)

    system_preview_source_image = Image.open("workfolder/preview/preview_systemui_0.jpg")
    system_preview_crop_coordinates1 = (317, 812, 317 + 213, 812 + 35)
    system_preview_cropped_image1 = system_preview_source_image.crop(system_preview_crop_coordinates1)

    system_preview_destination_image = Image.open("workfolder/preview/preview_systemui_0.jpg")
    system_preview_paste_coordinates1 = (317, 843)
    system_preview_destination_image.paste(system_preview_cropped_image1, system_preview_paste_coordinates1)

    tree = ET.parse(xml_file_system)
    root = tree.getroot()

    color_name_system_text = root.find("color[@name='magic_primary']").text
    color_value_system_text = color_name_system_text[3:]  # Ignore the first three characters "#"

    text_color = tuple(int(color_value_system_text[i:i + 2], 16) for i in (0, 2, 4))

    add_text(system_preview_destination_image, "Honor Share", 38, (319, 839), text_color)

    system_preview_destination_image.save("workfolder/preview/preview_systemui_0.jpg")

    # Delete Temp Files
    folder_to_delete = "workfolder/icons_preview"
    shutil.rmtree(folder_to_delete)

