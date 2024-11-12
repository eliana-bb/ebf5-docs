import re
import data
import datetime
import json

NOW = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S%f")[:17]

stats = ("HP", "attack", "defence", "magicAttack", "magicDefence", "accuracy", "evade")

for equip_name, equip in data.equips.items():
    if "specials" not in equip:
        continue
    if equip["specials"] is None:
        continue
    for lv, special in enumerate(equip["specials"]):
        if special is None:
            continue
        if special[0] == "Equip.STATUS":
            print(equip_name, end=":")
            print(special[1][7:].replace("_", " ").title().replace("Autolife", "Auto-Revive"), end=";")
            print(special[2], end=";")
            print(special[3], end=";")
            print(lv+1)