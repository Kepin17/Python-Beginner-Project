import random

def jadwal():
    list_penayangan = ["11.00" , "12.00" , "13.00","14.00" , "16.00" , "19.00" , "21.00"]
    list_studio = ["Studio 1" , "Studio 2" , "Studio 3" , "Studio 4"]
    print(f"\nWaktu penayangan  : {random.choice(list_penayangan)}")
    print(f"Studio penayangan : {random.choice(list_studio)}")



