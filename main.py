import re
import data
import datetime
import json

NOW = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S%f")[:17]

stats = ("HP", "attack", "defence", "magicAttack", "magicDefence", "accuracy", "evade")
for equip_name, equip in data.equips.items():
    if "specials" not in equip:
        continue
    for special in equip["specials"]:
        if special is None:
            continue
        if special[0] == "Equip.CAST":
            print(equip_name, end=":")
            skill_name = data.skill_names[special[1][7:]]
            print(skill_name, end=";")
            print(special[2])
