import soco
from pprint import pprint
import tkinter as tk
from functools import partial

def play_station(coordinator, uri, metadata):
    print("play station " + uri)
    coordinator.play_uri(uri, metadata)

def main():
    root = tk.Tk()

    coordinator = next(zone for zone in soco.discover() if zone.is_coordinator)

    for i in range(0, 7):
        btn = tk.Button(root,
        text=f'{10*i}', 
        width=4,
        command=lambda i=i: setattr(coordinator.group, "volume", i*10))
        btn.grid(column=0, row=i, padx=5)


    def partyMode():
        activeSpeaker =soco.discovery.by_name("Wohnzimmer") 
        activeSpeaker.partymode()
        # for speaker in soco.discover():
        #     if not (speaker in activeSpeaker.group.members):
        #         activeSpeaker.group.members.add(speaker)

    btnPartyMode = tk.Button(root, 
        text="party mode",
        command=partyMode
    )
    btnPartyMode.grid(column=0, row=7)
        

    print("zones:")

    for zone in soco.discover():
        print("   ", zone.player_name, "--", zone.ip_address)
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
        btn = tk.Button(root, 
            text=station.title, 
            width=30,
            command=lambda uri=uri,metadata=metadata: play_station(coordinator, uri, metadata))
        
        divider = 3
        col = (i % divider) + 1
        row = int(i/divider)
        btn.grid(row=row, column=col, padx=5, pady=2)

        i = i + 1

        for res in station.resources:
            #pprint(vars(res))
            print("    uri:", res.uri)
            print("    proto:", res.protocol_info)
        print("")
    
    root.mainloop()

if __name__ == "__main__":
    main()