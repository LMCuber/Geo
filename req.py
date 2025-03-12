import requests
from pathlib import Path
import os


def get_url(year, y, x):
    return rf"https://geacron.b-cdn.net/tiles/area_{year}_Z2_{y}_{x}.png?v=20"


def save_year(year):
    year = str(year) if year > 0 else f"B{-year}"

    try:
        os.mkdir(Path("public", "maps", year))
    except FileExistsError:
        return

    for y in range(3):
        for x in range(4):
            url = get_url(year, y, x)
            response = requests.get(url)
            if response.status_code == 200:
                file_name = f"{year}_{y}_{x}.png"
                with open(Path("public", "maps", year, file_name), "wb") as f:
                    f.write(response.content)
                    print(f"Written {file_name}")
            else:
                print(f"At year {year}, ({x}, {y}): Error", response.status_code)


for year in range(1, 2023):
    save_year(year)
