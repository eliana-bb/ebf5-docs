import re
import json

with open("data/Equips.as") as infile:
    content = infile.read()

equip_list = re.findall(r"public static var (\w+):Equip = new Equip\(([^;]+)\);", content, re.MULTILINE)

