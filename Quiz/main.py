


def new_Game():
    users = []
    benar = 0
    qn = 1

    for key in q:
      print(20*"-")
      print(key)
      for i in o[qn-1]:
        print(i)
      
      user = input("Enter (A,B,C,D) : ")
      user = user.upper()
      users.append(user)

      benar += ceck_Answer(q.get(key) , user)
      qn += 1

    display_score(benar , users)      
        
def ceck_Answer(answer , user):
    
    if answer == user:
        print("Correct!")
        return 1
    else:
      print('wrong')
      return 0     


def display_score(benar , users):
    print(20*"-")
    print("Hasil")
    print(20*"-")
    print("Answer : ",end="")
    for i in q:
        print(q.get(i) , end="")
    print()    

    print("User : ",end="")
    for i in users:
        print(i , end="")
    print()    

    score = int((benar/len(q))*100)
    print("Your Score is " + str(score) + "%")

def play_again():
    

    response = input("do you want to play again? yes/no : ")
    response = response.upper()

    if response == "YES":
      return True
    else:
        return False  


q = {
"1 + 1 = ": "A",
'2 + 2 = ': "B",
"1 * 2 = ": "C",
"2 / 1 = ": "A"
}

o = [
    ["A) 2", "B) 3","C) 1","D) 0"],
    ['A) 2', 'B) 4','C) 5','D) 3'],
    ['A) 33','B) 4','C) 2','D) 3'],
    ['A) 2','B) 4','C) 5','D) 3']]

new_Game()    

while play_again():
    new_Game()

print("See ya!")    