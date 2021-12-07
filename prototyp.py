import soco
from pprint import pprint
import tkinter as tk

print("zones:")

for zone in soco.discover():
    print("   ", zone.player_name, "--", zone.ip_address)
    if zone.is_coordinator: 
        coordinator = zone
print("")

print("coordinator:")
#pprint(vars(coordinator))
print("    ", coordinator.ip_address)
print("")

print("favorite stations")
stations = coordinator.music_library.get_favorite_radio_stations()
for station in stations:
    print("    title:", station.title)
    for res in station.resources:
        #pprint(vars(res))
        print("    uri:", res.uri)
        print("    proto:", res.protocol_info)
    print("")