import requests
from pathlib import Path
import os
from threading import Thread


def get_img_url(year, y, x):
    return fr"https://geacron.b-cdn.net/tiles/area_{year}_Z2_{y}_{x}.png?v=20"


def year_to_str(year):
    return str(year) if year > 0 else f"B{-year}"


def get_label_url(year):
    return fr"https://geacron.b-cdn.net/txt/labeltxt_en_L{year}_Z3_L{year}en3.txt?v=0"


def save_label(year):
    year = year_to_str(year)
    url = get_label_url(year)
    response = requests.get(url)
    if response.status_code == 200:
        with open(Path("public", "labels", f"{year}.js"), "wb") as f:
            f.write(response.content)
            print("saved", year)
    else:
        print("FAILED", year)


def save_year(year):
    try:
        os.mkdir(Path("public", "maps", str(year)))
    except FileExistsError:
        return
    for y in range(3):
        for x in range(4):
            url = get_img_url(year, y, x)
            response = requests.get(url)
            if response.status_code == 200:
                file_name = f"{year}_{y}_{x}.png"
                with open(Path("public", "maps", str(year), file_name), "wb") as f:
                    f.write(response.content)
                    print(f"Written {file_name}")


for year in range(290, 1005):
    # Thread(target=save_year, args=[year]).start()
    save_label(year)
