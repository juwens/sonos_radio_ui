import soco
from pprint import pprint
import tkinter as tk

def play_station(coordinator, uri, metadata):
    print("play station " + uri)
    coordinator.play_uri(uri, metadata)

def main():
    root = tk.Tk()

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
    stations = coordinator.music_library.get_sonos_favorites()
    i = 0
    for station in stations:
        print("    title:", station.title)
        print("    item_class:", station.item_class)
        print("    item_class:", station.reference.item_class)

        if len(station.resources) == 0: continue

        uri = station.resources[0].uri
        metadata = station.resource_meta_data
        btn = tk.Button(root, text=station.title + "\r\n" + uri, command=lambda uri=uri,metadata=metadata: play_station(coordinator, uri, metadata))
        
        divider = 3
        col = i % divider
        row = int(i/divider)
        btn.grid(row=row, column=col)

        i = i + 1

        for res in station.resources:
            #pprint(vars(res))
            print("    uri:", res.uri)
            print("    proto:", res.protocol_info)
        print("")
    
    root.mainloop()

if __name__ == "__main__":
    main()