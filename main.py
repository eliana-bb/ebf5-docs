import re
import data
import datetime
import json

NOW = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S%f")[:17]

stats = ("HP", "attack", "defence", "magicAttack", "magicDefence", "accuracy", "evade")
with open("data/Spells.as") as infile:
    upgrade_chains = re.findall(r" (\w+)\.upgradesInto = (\w+);", infile.read())

upgrade_chains = dict(upgrade_chains)

for skill_id, skill_name in data.skill_names.items():
    print(skill_name, end=":")
    current_skill_id = skill_id
    while current_skill_id in upgrade_chains:
        current_skill_id = upgrade_chains[current_skill_id]
    print(data.skill_names[current_skill_id])