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
    polygon?
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
def get_json_data(filename):
    with open(filename) as fn:
        return json.load(fn)
        

if __name__ == "__main__":
    data = get_json_data('data.json')


    for room in data['rooms']:
        if not room:
            # the first room value is always null
            continue
        
        if room['shape'] not in ['square', 'polygon']:
            print(room['shape'], room['id'])