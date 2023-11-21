import random
import ui

maps = [
    {
        "name": "Mario Kart Stadium",
        "cup": "Mushroom Cup",
        "tip": "Bullet extension: Just before mid ramp"
    },
    {
        "name": "Water Park",
        "cup": "Mushroom Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Sweet Sweet Canyon",
        "cup": "Mushroom Cup",
        "tip": "Bullet extension: Just before donut"
    },
    {
        "name": "Thwomp Ruins",
        "cup": "Mushroom Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Mario Circuit",
        "cup": "Flower Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Toad Harbor",
        "cup": "Flower Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Twisted Mansion",
        "cup": "Flower Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Shy Guy Falls",
        "cup": "Flower Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Sunshine Airport",
        "cup": "Star Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Dolphin Shoals",
        "cup": "Star Cup",
        "tip": "Bullet extension: Right at finish line, mid section of eel"
    },
    {
        "name": "Electrodrome",
        "cup": "Star Cup",
        "tip": "Bullet extension: Offroad before finish line"
    },
    {
        "name": "Mount Wario",
        "cup": "Star Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Cloudtop Cruise",
        "cup": "Special Cup",
        "tip": "Bullet extension: End of glider going back to ground"
    },
    {
        "name": "Bone-Dry Dunes",
        "cup": "Special Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Bowser's Castle",
        "cup": "Special Cup",
        "tip": "Bullet Extension: Slightly before finish line"
    },
    {
        "name": "Rainbow Road",
        "cup": "Special Cup",
        "tip": "Bullet Extension: first twist section on bottom"
    },
    {
        "name": "Moo Moo Meadows",
        "cup": "Shell Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Mario Circuit",
        "cup": "Shell Cup",
        "tip": "Bullet extension: Left of shortcut tires after finish line"
    },
    {
        "name": "Cheep Cheep Beach",
        "cup": "Shell Cup",
        "tip": "Bullet extension: Start of curve on pier section"
    },
    {
        "name": "Toad's Turnpike",
        "cup": "Shell Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Dry Dry Desert",
        "cup": "Banana Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Donut Plains 3",
        "cup": "Banana Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Royal Raceway",
        "cup": "Banana Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "DK Jungle",
        "cup": "Banana Cup",
        "tip": "Bullet extension: After hitting ground from second flower jump, shortcut platform before finish line"
    },
    {
        "name": "Wario Stadium",
        "cup": "Leaf Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Sherbet Land",
        "cup": "Leaf Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Music Park",
        "cup": "Leaf Cup",
        "tip": "Bullet extension: Midway through piano"
    },
    {
        "name": "Yoshi Valley",
        "cup": "Leaf Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Tick-Tock Clock",
        "cup": "Lightning Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Piranha Plant Slide",
        "cup": "Lightning Cup",
        "tip": "Bullet extension: Right before first underwater ramp"
    },
    {
        "name": "Grumble Volcano",
        "cup": "Lightning Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Rainbow Road",
        "cup": "Lightning Cup",
        "tip": "Bullet extension: Start of \"8\" loop (look at mini map)"
    },
    {
        "name": "Yoshi Circuit",
        "cup": "Egg Cup",
        "tip": "Bullet extension: After trick under waterfall"
    },
    {
        "name": "Excitebike Arena",
        "cup": "Egg Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Dragon Driftway",
        "cup": "Egg Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Mute City",
        "cup": "Crossing Cup",
        "tip": "Bullet extension: Start of loop at top of minimap"
    },
    {
        "name": "Wario's Goldmine",
        "cup": "Triforce Cup",
        "tip": "Bullet extension: Final trickable ramp into the goldmine"
    },
    {
        "name": "SNES Rainbow Road",
        "cup": "Triforce Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Ice Ice Outpost",
        "cup": "Triforce Cup",
        "tip": "Bullet extension: End of difficult 2nd shortcut in cave"
    },
    {
        "name": "Hyrule Circuit",
        "cup": "Triforce Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Neo Bowser City",
        "cup": "Bell Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Ribbon Road",
        "cup": "Bell Cup",
        "tip": "Bullet extension: Right before boost ramp that goes to wavy section, after wavy section in shortcut "
               "under arch"
    },
    {
        "name": "Super Bell Subway",
        "cup": "Bell Cup",
        "tip": "Bullet extension: By curve after first item set after finish line "
    },
    {
        "name": "Big Blue",
        "cup": "Bell Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Baby Park",
        "cup": "Crossing Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Cheese Land",
        "cup": "Crossing Cup",
        "tip": "Welcome to the hype zone\nBullet extension: Left most offroad after finish line right of pile of cheese"
    },
    {
        "name": "Wild Woods",
        "cup": "Crossing Cup",
        "tip": "No bullet extensions"
    },
    {
        "name": "Animal Crossing",
        "cup": "Crossing Cup",
        "tip": "Bullet extension: Landing after glider before beach"
    },
    {
        "name": "Paris Promenade",
        "cup": "Golden Dash Cup",
        "tip": "Bullet extension: Right after coin circle on glider (final lap)"
    },
    {
        "name": "Toad Circuit",
        "cup": "Golden Dash Cup",
        "tip": "No bullet extension"
    },
    {
        "name": "Choco Mountain",
        "cup": "Golden Dash Cup",
        "tip": "Bullet extension: Right after first crack in bolder section"
    },
    {
        "name": "Coconut Mall",
        "cup": "Golden Dash Cup",
        "tip": "Store shortcut at beginning"
    },
    {
        "name": "Tokyo Blur",
        "cup": "Lucky Cat Cup",
        "tip": "No bullet extension"
    },
    {
        "name": "Shroom Ridge",
        "cup": "Lucky Cat Cup",
        "tip": "No bullet extension"
    },
    {
        "name": "Sky Garden",
        "cup": "Lucky Cat Cup",
        "tip": "Bullet extension: Right before finish line after glider"
    },
    {
        "name": "Ninja Hideaway",
        "cup": "Lucky Cat Cup",
        "tip": "Bullet extension: Right after stairs on bottom floor"
    },
    {
        "name": "New York Minute",
        "cup": "Turnip Cup",
        "tip": "Bullet extension: Set right before finish line, right after bridge on offroad on lap 3"
    },
    {
        "name": "Mario Circuit 3",
        "cup": "Turnip Cup",
        "tip": "Bullet extension: Middle of \"M\" shape on top of minimap, middle of \"D\" shape on right of minimap"
    },
    {
        "name": "Kalimari Desert",
        "cup": "Turnip Cup",
        "tip": "Bullet extension: Right of straightaway on rails, mildly before tunnel on lap 3"
    },
    {
        "name": "Waluigi Pinball",
        "cup": "Turnip Cup",
        "tip": "Bullet extension: Right off purple ramp before green section, between two flippers in main section"
    },
    {
        "name": "Sydney Sprint",
        "cup": "Propeller Cup",
        "tip": "Bullet extension: On 6 ramp section use just before 2nd or 5th ramp, after bend after finish line"
    },
    {
        "name": "Snow Land",
        "cup": "Propeller Cup",
        "tip": "Bullet extension: Downhill section before ice"
    },
    {
        "name": "Mushroom Gorge",
        "cup": "Propeller Cup",
        "tip": "Bullet extension: Little after coin circle in cave before bend, grass bend outside cave"
    },
    {
        "name": "Sky-High Sundae",
        "cup": "Propeller Cup",
        "tip": "Bullet extension: Right after landing with the right pink ramp, jumping from orange part of sprinkled "
               "bend activate in mid air"
    },
    {
        "name": "London Loop",
        "cup": "Rock Cup",
        "tip": "Bullet extension: After landing from ramp on lap 1, same bend on lap 2"
    },
    {
        "name": "Boo Lake",
        "cup": "Rock Cup",
        "tip": "Bullet extension: Use after first entering the water"
    },
    {
        "name": "Maple Treeway",
        "cup": "Rock Cup",
        "tip": "Bullet extension: Use before boost entering bend by halfpipe"
    },
    {
        "name": "Rock Rock Mountain",
        "cup": "Rock Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Rainbow Road",
        "cup": "Moon Cup",
        "tip": "Bullet extension: Right before two boost panels previous to the wavy section, mildly before arch on "
               "the moon"
    },
    {
        "name": "Merry Mountain",
        "cup": "Moon Cup",
        "tip": "Bullet extension: Right as you find straightaway before wooden bridge, right before anti grav panel "
               "after bridge"
    },
    {
        "name": "Peach Gardens",
        "cup": "Moon Cup",
        "tip": "Bullet extension: Last grass bend by finish line (lap 1 + 2), around same spot in reverse on lap 3, "
               "just after Peach statue from glider on lap 3"
    },
    {
        "name": "Berlin Byways",
        "cup": "Moon Cup",
        "tip": "Bullet extension: Just after glider, grass bend by berlin wall"
    },
    {
        "name": "Amsterdam Drift",
        "cup": "Fruit Cup",
        "tip": "Bullet extension: Use on grass bend after finish line, grass bend in tulip field"
    },
    {
        "name": "Riverside Park",
        "cup": "Fruit Cup",
        "tip": "Bullet extension: Use mildly before bridge previous to cave"
    },
    {
        "name": "DK Summit",
        "cup": "Fruit Cup",
        "tip": "Bullet extension: In first snow pile downhill after cannon"
    },
    {
        "name": "Yoshi's Island",
        "cup": "Fruit Cup",
        "tip": "Bullet extension: In right offroad after landing from glider, further up if bridge is created, "
               "underwater between crabs"
    },
    {
        "name": "Bangkok Rush",
        "cup": "Boomerang Cup",
        "tip": "Bullet extension: Entering parking structure"
    },
    {
        "name": "Mario Circuit",
        "cup": "Boomerang Cup",
        "tip": "Bullet extension: Left of first rock when entering forest section, turn before the big turn, "
               "right after finish line"
    },
    {
        "name": "Walugi Stadium",
        "cup": "Boomerang Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Singapore Speedway",
        "cup": "Boomerang Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Athens Dash",
        "cup": "Feather Cup",
        "tip": "Bullet extension: Right before end of glider when entering cave"
    },
    {
        "name": "Daisy Cruiser",
        "cup": "Feather Cup",
        "tip": "Bullet extension: Entering pool from right side, end of stairs before finish line"
    },
    {
        "name": "Moonview Highway",
        "cup": "Feather Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Squeaky Clean Sprint",
        "cup": "Feather Cup",
        "tip": "Bullet extension: Mildly before drain in tub, in left soap by fan"
    },
    {
        "name": "Tour Los Angeles Laps",
        "cup": "Cherry Cup",
        "tip": "Bullet extension: After ramp with double items at beach, slightly before lap line before lap 2"
    },
    {
        "name": "Sunset Wilds",
        "cup": "Cherry Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Koopa Cape",
        "cup": "Cherry Cup",
        "tip": "Bullet extension: After ramp to riverslide section, before first ramp in underwater section"
    },
    {
        "name": "Tour Vancouver Velocity",
        "cup": "Cherry Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Tour Rome Avanti",
        "cup": "Acorn Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "DK Mountain",
        "cup": "Acorn Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Daisy Circuit",
        "cup": "Acorn Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Piranha Plant Cove",
        "cup": "Acorn Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Tour Madrid Dive",
        "cup": "Spiny Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Rosalina's Ice World",
        "cup": "Spiny Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Bowser's Castle 3",
        "cup": "Spiny Cup",
        "tip": "Unknown bullet extensions"
    },
    {
        "name": "Rainbow Road",
        "cup": "Spiny Cup",
        "tip": "Unknown bullet extensions"
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
