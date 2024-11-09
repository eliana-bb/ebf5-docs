import re
import data
import datetime
import json

NOW = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S%f")[:17]

for equip in data.equips.values():
    equip_title = data.equip_names[equip['SID']][0]
    equip_desc = data.equip_names[equip['SID']][1]
    tiddler = {"title": equip_title, "created": NOW, "modified": NOW, "tags": "Equips TODO",
               "text": "<$transclude $tiddler=\"Equip Descriptions\" $index=<<currentTiddler>>/>\n\n{{Equip Icon}}"}
    with open("eq_" + equip["SID"] + ".json", "w") as outfile:
        json.dump(tiddler, outfile)