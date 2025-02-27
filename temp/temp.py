#Using data file sample-data.json, create output that resembles the 
#following by parsing the included JSON file.

import json

f = open(r"C:\Users\user\Desktop\Python\lab4\temp\sample-data.json")

data = json.load(f)

print("Interface Status")
print("=" * 87)
print(f"{'DN':<50} {'Description':<21} {'Speed':<8} {'MTU':<5}")
print(f"{'-' * 50:<50} {'-'*21:<21} {'-'*8:<8} {'-'*5:<5}")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50} {descr:<21} {speed:<8} {mtu:<5}")