import requests
from pathlib import Path
import os
from threading import Thread


def get_url(year, y, x):
    return fr"https://geacron.b-cdn.net/tiles/area_{year}_Z2_{y}_{x}.png?v=20"


def save_year(year):
    try:
        os.mkdir(Path("public", "maps", str(year)))
    except FileExistsError:
        return
    for y in range(3):
        for x in range(4):
            url = get_url(year, y, x)
            response = requests.get(url)
            if response.status_code == 200:
                file_name = f"{year}_{y}_{x}.png"
                with open(Path("public", "maps", str(year), file_name), "wb") as f:
                    f.write(response.content)
                    print(f"Written {file_name}")


for year in range(0, 2100):
    if year % 100 == 0:
        Thread(target=save_year, args=[year]).start()