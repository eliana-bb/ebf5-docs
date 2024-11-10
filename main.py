import re
import data
import datetime
import json

NOW = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S%f")[:17]

stats = ("HP", "attack", "defence", "magicAttack", "magicDefence", "accuracy", "evade")
for stat in stats:
    print("\n\n")
    for equip in data.equips.values():
        equip_name = data.equip_names[equip["SID"]][0]
        print(equip_name, end=":")
        for k, v in enumerate(equip[stat]):
            print(v, end="")
            if k != len(equip[stat])-1:
                print(",", end="")
            else:
                print()
