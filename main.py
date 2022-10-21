import json
'''
corridor_features{}
    a-z{}
        detail
        key
        summary
details{}
    floor
    illumination
    special
    temperature
    walls
rooms[]
    id
    width
    height
    area
    shape
    north
    south
    east
    west
    contents{}
        detail{}
            room_features?
            hidden_treature?
            trap?
            inhabited?
            monster[]?
                X monsters
                --
                treasure
    doors{}
        north|south|east|west[]
            desc
            out_id
            type
stairs[]
    col
    dir
    key
    row
wandering_monsters{}
    1
    2
    3
    4
    5
    6



'''
with open('data.json') as fn:
    data = json.load(fn)

print(data)