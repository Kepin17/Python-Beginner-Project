

import random
print("Gacha status Test 1")

user = ["Kepin","Makcang","Mepuru","Arikata","Dio","William","Bambang","Peter","Charles","Lugh","Rafael","Michael","George"]
jobs = ["Student","Gay","Mafia","Married","Teacher","Worker","Programer","President","Business Man"]
hobby = ["Making Tiktok Videos","Playing Basketball","Playing Football","Draw","Sleep","Diving","Waching anime","Waching Movie","Singing","Editing","Acting","Camping"]
region = ["AFG","AL","AR","AW","AU","AT","AZ","BD","BT","BO","BR","VG","BN","BG","ID","US","JP","DK","IND"]
grub = ["Manime_Sekai Grup Admin","Tutha De Group","Shigatsu Group"]
media = ["WhatsApp","FaceBook","Telegram"]
status = ["Married","Single","Gay","Lesbian"]

target_name = random.choice(user)
target_job = random.choice(jobs)
target_hobby = random.choice(hobby)
target_media = random.choice(media)
target_region = random.choice(region)
target_group = random.choice(grub)
target_status = random.choice(status)

email = target_name + "@isekai.com"

print(f" name : {target_name}\n Job : {target_job}\n Hobby :{target_hobby}\n Status : {target_status}\n Grup : {target_group}\n media : {target_media}\n region : {target_region}\n Email : {email}")




