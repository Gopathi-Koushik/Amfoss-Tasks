from collections import Counter
def find_captains_room(k, room_list):
    # Count the occurrences of each room number
    room_count = Counter(room_list)
    
   #find the room number that appears once
    for room, count in room_count.items():
        if count == 1:
            return room

k = int(raw_input())  
room_list = map(int, raw_input().split())  

captains_room = find_captains_room(k, room_list)

print captains_room


