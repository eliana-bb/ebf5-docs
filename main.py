import re
import json
import pprint
import io
with open("data/Equips.as") as infile:
    infile_content = infile.read()

equip_list = re.findall(r"public static var (\w+):Equip = new Equip\((\{[^;]+})\);", infile_content)

for equip_id, equip_text in equip_list:
    if equip_id in ("template", "empty"):
        continue
    equip_text = re.sub(r"\"(?:icon|skin|map)\":[^\n]+\n", "", equip_text)
    equip_text = re.sub(r"(?:Equips\.)?((?:long|short|down)\d{2,3})", r'"\g<1>"', equip_text)
    equip_text = re.sub(r"(?:Equips?|Element|Statu?s|Spells|Items|Foe|Summons)\.\w+", r'"\g<0>"', equip_text)
    equip_text = re.sub(r"[ \n]+", " ", equip_text)
    equip = json.loads(equip_text)
    equip["type"] = equip["type"][6:]
    num_levels = 3 if equip["type"] == "FLAIR" else 5
    for stat in ("HP", "attack", "defence", "magicAttack", "magicDefence", "accuracy", "evade"):
        if stat not in equip:
            equip[stat] = [0]
        while len(equip[stat]) < num_levels:
            equip[stat].append(equip[stat][-1])
    print(f'"{equip_id}":', json.dumps(equip, indent=4).replace("null", "None"), ",")