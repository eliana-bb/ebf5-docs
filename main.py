import re
import data
import datetime
import json

NOW = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S%f")[:17]

stats = ("HP", "attack", "defence", "magicAttack", "magicDefence", "accuracy", "evade")
for equip in data.equips.values():
    equip_name = data.equip_names[equip["SID"]][0]
    has_status = "statusEffect" in equip and equip["statusEffect"] not in (None, "Status.NONE")
    has_buff = "buffEffect" in equip and equip["buffEffect"] not in (None, "Stats.NONE")
    has_specials = "specials" in equip and equip["specials"] not in ([], [None])
    if not has_specials:
        print(equip_name)
