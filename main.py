import random
import ui

maps = [
    {
        "name": "Mario Circuit",
        "cup": "Mushroom Cup",
        "weight": 1
    },
    {
        "name": "Toad Harbor",
        "cup": "Mushroom Cup",
        "weight": 1
    },
    {
        "name": "Twisted Mansion",
        "cup": "Mushroom Cup",
        "weight": 1
    },
    {
        "name": "Shy Guy Falls",
        "cup": "Mushroom Cup",
        "weight": 1
    },
    {
        "name": "Sunshine Airport",
        "cup": "Flower Cup",
        "weight": 1
    },
    {
        "name": "Dolphin Shoals",
        "cup": "Flower Cup",
        "weight": 1
    },
    {
        "name": "Electrodrome",
        "cup": "Flower Cup",
        "weight": 1
    },
    {
        "name": "Mount Wario",
        "cup": "Flower Cup",
        "weight": 1
    },
    {
        "name": "Cloudtop Cruise",
        "cup": "Star Cup",
        "weight": 1
    },
    {
        "name": "Bone-Dry Dunes",
        "cup": "Star Cup",
        "weight": 1
    },
    {
        "name": "Bowser's Castle",
        "cup": "Star Cup",
        "weight": 1
    },
    {
        "name": "Rainbow Road",
        "cup": "Star Cup",
        "weight": 1
    },
    {
        "name": "Mario Kart Stadium",
        "cup": "Special Cup",
        "weight": 1
    },
    {
        "name": "Water Park",
        "cup": "Special Cup",
        "weight": 1
    },
    {
        "name": "Sweet Sweet Canyon",
        "cup": "Special Cup",
        "weight": 1
    },
    {
        "name": "Thwomp Ruins",
        "cup": "Special Cup",
        "weight": 1
    },
    {
        "name": "Mario Circuit",
        "cup": "Egg Cup",
        "weight": 1
    },
    {
        "name": "Yoshi Circuit",
        "cup": "Egg Cup",
        "weight": 1
    },
    {
        "name": "Excitebike Arena",
        "cup": "Egg Cup",
        "weight": 1
    },
    {
        "name": "Dragon Driftway",
        "cup": "Egg Cup",
        "weight": 1
    },
    {
        "name": "Mute City",
        "cup": "Crossing Cup",
        "weight": 1
    },
    {
        "name": "Baby Park",
        "cup": "Crossing Cup",
        "weight": 1
    },
    {
        "name": "Cheese Land",
        "cup": "Crossing Cup",
        "weight": 1
    },
    {
        "name": "Wild Woods",
        "cup": "Crossing Cup",
        "weight": 1
    },
    {
        "name": "Neo Bowser City",
        "cup": "Shell Cup",
        "weight": 1
    },
    {
        "name": "Ribbon Road",
        "cup": "Shell Cup",
        "weight": 1
    },
    {
        "name": "Super Bell Subway",
        "cup": "Shell Cup",
        "weight": 1
    },
    {
        "name": "Big Blue",
        "cup": "Shell Cup",
        "weight": 1
    },
    {
        "name": "Animal Crossing",
        "cup": "Banana Cup",
        "weight": 1
    },
    {
        "name": "Cheep Cheep Beach",
        "cup": "Banana Cup",
        "weight": 1
    },
    {
        "name": "Donut Plains 3",
        "cup": "Banana Cup",
        "weight": 1
    },
    {
        "name": "Toad's Turnpike",
        "cup": "Banana Cup",
        "weight": 1
    },
    {
        "name": "Wario Stadium",
        "cup": "Leaf Cup",
        "weight": 1
    },
    {
        "name": "Sherbet Land",
        "cup": "Leaf Cup",
        "weight": 1
    },
    {
        "name": "Music Park",
        "cup": "Leaf Cup",
        "weight": 1
    },
    {
        "name": "Yoshi Valley",
        "cup": "Leaf Cup",
        "weight": 1
    },
    {
        "name": "Tick-Tock Clock",
        "cup": "Lightning Cup",
        "weight": 1
    },
    {
        "name": "Piranha Plant Slide",
        "cup": "Lightning Cup",
        "weight": 1
    },
    {
        "name": "Grumble Volcano",
        "cup": "Lightning Cup",
        "weight": 1
    },
    {
        "name": "Rainbow Road",
        "cup": "Lightning Cup",
        "weight": 1
    },
    {
        "name": "Wario Stadium",
        "cup": "Triforce Cup",
        "weight": 1
    },
    {
        "name": "GCN Rainbow Road",
        "cup": "Triforce Cup",
        "weight": 1
    },
    {
        "name": "Ice Ice Outpost",
        "cup": "Triforce Cup",
        "weight": 1
    },
    {
        "name": "Hyrule Circuit",
        "cup": "Triforce Cup",
        "weight": 1
    },
    {
        "name": "Dragon Driftway",
        "cup": "Bell Cup",
        "weight": 1
    },
    {
        "name": "Mute City",
        "cup": "Bell Cup",
        "weight": 1
    },
    {
        "name": "Wario Stadium",
        "cup": "Bell Cup",
        "weight": 1
    },
    {
        "name": "Animal Crossing",
        "cup": "Bell Cup",
        "weight": 1
    },
    {
        "name": "Baby Park",
        "cup": "Golden Dash Cup",
        "weight": 1
    },
    {
        "name": "Cheese Land",
        "cup": "Golden Dash Cup",
        "weight": 1
    },
    {
        "name": "Wild Woods",
        "cup": "Golden Dash Cup",
        "weight": 1
    },
    {
        "name": "Animal Crossing",
        "cup": "Golden Dash Cup",
        "weight": 1
    },
    {
        "name": "Neo Bowser City",
        "cup": "Lucky Cat Cup",
        "weight": 1
    },
    {
        "name": "Ribbon Road",
        "cup": "Lucky Cat Cup",
        "weight": 1
    },
    {
        "name": "Super Bell Subway",
        "cup": "Lucky Cat Cup",
        "weight": 1
    },
    {
        "name": "Big Blue",
        "cup": "Lucky Cat Cup",
        "weight": 1
    },
    {
        "name": "Toad Circuit",
        "cup": "Turnip Cup",
        "weight": 1
    },
    {
        "name": "Mario Circuit",
        "cup": "Turnip Cup",
        "weight": 1
    },
    {
        "name": "Rock Rock Mountain",
        "cup": "Turnip Cup",
        "weight": 1
    },
    {
        "name": "Piranha Plant Pipeway",
        "cup": "Turnip Cup",
        "weight": 1
    },
    {
        "name": "Airship Fortress",
        "cup": "Propeller Cup",
        "weight": 1
    },
    {
        "name": "Water Park",
        "cup": "Propeller Cup",
        "weight": 1
    },
    {
        "name": "Sweet Sweet Canyon",
        "cup": "Propeller Cup",
        "weight": 1
    },
    {
        "name": "Thwomp Ruins",
        "cup": "Propeller Cup",
        "weight": 1
    },
    {
        "name": "Mario Circuit",
        "cup": "Rock Cup",
        "weight": 1
    },
    {
        "name": "Cheep Cheep Beach",
        "cup": "Rock Cup",
        "weight": 1
    },
    {
        "name": "Toad Harbor",
        "cup": "Rock Cup",
        "weight": 1
    },
    {
        "name": "Twisted Mansion",
        "cup": "Rock Cup",
        "weight": 1
    },
    {
        "name": "Sunshine Airport",
        "cup": "Moon Cup",
        "weight": 1
    },
    {
        "name": "Electrodrome",
        "cup": "Moon Cup",
        "weight": 1
    },
    {
        "name": "Mount Wario",
        "cup": "Moon Cup",
        "weight": 1
    },
    {
        "name": "Cloudtop Cruise",
        "cup": "Moon Cup",
        "weight": 1
    },
    {
        "name": "Wii Moo Moo Meadows",
        "cup": "Fruit Cup",
        "weight": 1
    },
    {
        "name": "GBA Mario Circuit",
        "cup": "Fruit Cup",
        "weight": 1
    },
    {
        "name": "DS Cheep Cheep Beach",
        "cup": "Fruit Cup",
        "weight": 1
    },
    {
        "name": "N64 Toad's Turnpike",
        "cup": "Fruit Cup",
        "weight": 1
    },
    {
        "name": "DS Tick-Tock Clock",
        "cup": "Boomerang Cup",
        "weight": 1
    },
    {
        "name": "3DS Piranha Plant Slide",
        "cup": "Boomerang Cup",
        "weight": 1
    },
    {
        "name": "Wii Grumble Volcano",
        "cup": "Boomerang Cup",
        "weight": 1
    },
    {
        "name": "N64 Rainbow Road",
        "cup": "Boomerang Cup",
        "weight": 1
    },
    {
        "name": "Daisy Cruiser",
        "cup": "Feather Cup",
        "weight": 1
    },
    {
        "name": "Moonview Highway",
        "cup": "Feather Cup",
        "weight": 1
    },
    {
        "name": "Squeaky Clean Sprint",
        "cup": "Feather Cup",
        "weight": 1
    },
    {
        "name": "Tour Los Angeles Laps",
        "cup": "Cherry Cup",
        "weight": 1
    },
    {
        "name": "Sunset Wilds",
        "cup": "Cherry Cup",
        "weight": 1
    },
    {
        "name": "Koopa Cape",
        "cup": "Cherry Cup",
        "weight": 1
    },
    {
        "name": "Tour Vancouver Velocity",
        "cup": "Cherry Cup",
        "weight": 1
    },
    {
        "name": "Tour Rome Avanti",
        "cup": "Acorn Cup",
        "weight": 1
    },
    {
        "name": "DK Mountain",
        "cup": "Acorn Cup",
        "weight": 1
    },
    {
        "name": "Daisy Circuit",
        "cup": "Acorn Cup",
        "weight": 1
    },
    {
        "name": "Piranha Plant Cove",
        "cup": "Acorn Cup",
        "weight": 1
    },
    {
        "name": "Tour Madrid Dive",
        "cup": "Spiny Cup",
        "weight": 1
    },
    {
        "name": "Rosalina's Ice World",
        "cup": "Spiny Cup",
        "weight": 1
    },
    {
        "name": "Bowser's Castle 3",
        "cup": "Spiny Cup",
        "weight": 1
    },
    {
        "name": "Rainbow Road",
        "cup": "Spiny Cup",
        "weight": 1
    }
]
cup_colors = {
    "Mushroom Cup": "#ffffff",
    "Flower Cup": "#ff8c00",
    "Star Cup": "#ffff00",
    "Special Cup": "#ffc800",
    "Egg Cup": "#27c924",
    "Crossing Cup": "#27c924",
    "Shell Cup": "#27c924",
    "Banana Cup": "#eaff00",
    "Leaf Cup": "#8b4513",
    "Lightning Cup": "#ffff00",
    "Triforce Cup": "#ffff00",
    "Bell Cup": "#ffff00",
    "Golden Dash Cup": "#ffff00",
    "Lucky Cat Cup": "#b2460f",
    "Turnip Cup": "#ffffff",
    "Propeller Cup": "#FF5733",
    "Rock Cup": "#7f7f7f",
    "Moon Cup": "#ffff00",
    "Fruit Cup": "#ff8c00",
    "Boomerang Cup": "#0c63f0",
    "Feather Cup": "#e85709",
    "Cherry Cup": "#ff002f",
    "Acorn Cup": "#ff5500",
    "Spiny Cup": "#3477eb"
}

randomMaps = random.sample(maps, 8)
data = [randomMaps.index(item) + 1 for item in randomMaps]

# Ui stuff
view = ui.load_view("UI.pyui")
table = view["Map_Table"]
table.data_source = ui.ListDataSource(data)
view.present("sheet")
