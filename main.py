import re
import data
import datetime
import json

NOW = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S%f")[:17]

stats = ("HP", "attack", "defence", "magicAttack", "magicDefence", "accuracy", "evade")
with open("data/local_skills.as") as infile:
    file_content = infile.read()

skill_locals = re.findall(r"public static var ([^:]+):Object = \{[ \n]+\"name\":\"([^\"]+)\"", file_content)

skill_locals.extend(re.findall(r"public static var ([^:]+):String = \"([^\"]+)\"", file_content))

print("{")
for sid, name in skill_locals:
    if re.match(r"[A-Z]", sid):
        continue
    name = name.replace('\\\'', '\'')
    print(f"\t\"{sid}\": \"{name}\",")
print("}")

with open("data/Spells.as") as infile:
    file_content = infile.read()

skill_sids = re.findall(r"public static var ([^:]+):Spell = new Spell\({[\n ]+\"SID\":\"([^\"]+)\"", file_content)

for id, sid in skill_sids:
    print(f"\t\"{id}\": \"{data.skill_sids[sid]}\",")