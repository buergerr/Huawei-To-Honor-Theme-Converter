from PIL import Image, ImageDraw, ImageFont
import os
import xml.etree.ElementTree as ET

def manipulate_home_preview(work_folder):
    # Funktion zum Ausschneiden und Einfügen eines Bildausschnitts
    def crop_and_paste(source_image, coordinates, destination_image):
        cropped_image = source_image.crop(coordinates)
        destination_image.paste(cropped_image, coordinates)

    # Funktion zum Hinzufügen von Text
    def add_text(image, text, font_size, coordinates, color):
        font = ImageFont.truetype("assets/Roboto-Regular.ttf", font_size)
        draw = ImageDraw.Draw(image)
        draw.text(coordinates, text, font=font, fill=color)

    # Bildausschnitt aus "bild_xyz.jpg" ausschneiden
    source_image = Image.open(os.path.join(work_folder, "wallpaper", "home_wallpaper_0.jpg"))
    crop_coordinates1 = (849, 1176, 849 + 483, 1176 + 279)
    cropped_image1 = source_image.crop(crop_coordinates1)

    # Bild "zielbild.jpg" öffnen
    destination_image = Image.open(os.path.join(work_folder, "preview", "preview_widget_0.jpg"))


    # Bildausschnitt in das Zielbild einfügen
    paste_coordinates1 = (308, 1176)
    destination_image.paste(cropped_image1, paste_coordinates1)

    # Zweiten Bildausschnitt ausschneiden
    crop_coordinates2 = (1365, 1692, 1365 + 209, 1692 + 64)
    cropped_image2 = source_image.crop(crop_coordinates2)

    # Zweiten Bildausschnitt in das Zielbild einfügen
    paste_coordinates2 = (825, 1692)
    destination_image.paste(cropped_image2, paste_coordinates2)

    # XML-Datei "theme.xml" öffnen und Farbwerte extrahieren
    tree = ET.parse("theme.xml")
    root = tree.getroot()

    # Farbwerte extrahieren (Beispiel)
    color_name_widget_text = root.find("color[@name='widget_text_color']").text
    color_value_widget_text = color_name_widget_text[2:]  # Ignoriere die ersten beiden Zeichen "#"

    # Hintergrundfarbe für den Text in RGB umwandeln (Beispiel)
    text_color = tuple(int(color_value_widget_text[i:i+2], 16) for i in (0, 2, 4))

    # Text "Game Center" hinzufügen
    add_text(destination_image, "Game Center", 34, (333, 1389), text_color)

    # Text "Tips" hinzufügen
    add_text(destination_image, "Tips", 34, (630, 1389), text_color)

    # Text "Smart Remote" hinzufügen
    add_text(destination_image, "Smart Remote", 34, (811, 1700), text_color)

    # PNG-Dateien einfügen (Beispiel)
    png_image1 = Image.open("workfolder\icon_preview\com.hihonor.gamebox.png").convert("RGBA")
    paste_coordinates3 = (322, 1190)
    destination_image.paste(png_image1, paste_coordinates3, mask=png_image1)

    png_image2 = Image.open("workfolder\icon_preview\com.hihonor.android.tips.png").convert("RGBA")
    paste_coordinates4 = (570,1190)
    destination_image.paste(png_image2, paste_coordinates4, mask=png_image2)

    png_image3 = Image.open("workfolder\icon_preview\com.hihonor.android.remotecontroller.png").convert("RGBA")
    paste_coordinates5 = (817, 1500)
    destination_image.paste(png_image3, paste_coordinates5, mask=png_image3)

    # Zielbild speichern
    destination_image.save(work_folder, "preview_widget_0.jpg")


# Icon Preview Widget 
# /////////////////////
