from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_gps(image_path: str):
    try:
        image = Image.open(image_path)
        exif = image._getexif()
        if not exif:
            return None

        gps_info = {}
        for tag, value in exif.items():
            decoded = TAGS.get(tag)
            if decoded == "GPSInfo":
                for t in value:
                    sub_decoded = GPSTAGS.get(t)
                    gps_info[sub_decoded] = value[t]

        if "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
            return gps_info

        return None
    except Exception:
        return None
