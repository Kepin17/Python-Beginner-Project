def newGame():
    users = []
    correct = 0
    quizNum = 1

    for key in soal:
        print(40*"=")
        print(key)
        for i in answer[quizNum - 1]:
          print(i)

        user = input("Please enter A,B,C or D : ")
        user = user.upper()
        users.append(user) 

        correct += CeckAnswer(soal.get(key) , user)
        quizNum += 1 

        DisplayScore(correct , users)

def CeckAnswer(answer , user):
    
    if answer == user:
        print('Correct!')
        return 1
    else:
        print("Wrong!")
        return 0    

def DisplayScore(correct , users):
    
    print(20*"=")
    print("Result")
    print(20*"=")
    
    print("user answer : \n" , end="")
    for i in users:
        print(i ,end="")
    print()
        
    score = int((correct/len(soal))*100) 
    print(20*"=")
    print("Your score is : " + str(score) + "%")    
    print(20*"=")

def PlayAgain():
    

    response = input("\nDo you want to play again? y / n : ")
    response = response.upper()

    if response =="y":
        return True
    else:
        return False    


soal = {
  "Siapakah presiden pertama Indoensia?":'A',
  "Tanggal kemerdekaan Indonesia adalah:":"C",
  "Permasalah dari 8^4 = ..... + 2080 adalah":"A",
  "Diketahui harga 1 kg beras adalah Rp. 20,000,00.Jika ibu membeli 5 Kg beras,maka harga yang harus di bayar Ibu adalah":"B",
  "jawaban dari 2^0 + 1 adalah":"D" ,
  "Rani berumur 20 tahun ,adiknya bermur 10 tahun.Saat ini Rani berumur 50 tahun dan adiknya umur?":"C" ,
  'Menampilkan output Hello World! pada python dengan cara':"B",
  'Warna bendera Indonesia':"B",
  'Luas segitiga dengan alas 4 cm dan tinggi 20 cm adalah':"D",
  'Saat lampu merah kita harus ':"A"
  
}

answer = [
  ["A. Soekarno" , "B. MOh.Hatta" , "C. Kevien Ollyvie Jolanda" , "D. Soeharto" ],
  ["A. 14 Agustus 1945" , "B. 16 Agustus 1945" , "C. 17 Agustus 1945" , "D. 18 Agustus 1945 " ],
  ["A. 2016" , "B. 2309" , "C. 1220" , "D. 2015" ],
  ["A. Rp. 110,000" , "B. Rp. 100,000" , "C. Rp. 90,000" , "D. Rp. 80,000" ],
  ["A. 3" , "B. 4" , "C. 1" , "D. 2" ],
  ["A. 20 th" , "B. 30 th" , "C. 40 th" , "D. 50 th" ],
  ["A. <h1>Hello World!<h1>" , "B. print('Hello World!')" , "C. x = Hello World!" , "D. Output = str('Hello World!)" ],
  ["A. Merah , Putih , Biru" , "B. Merah , Putih" , "C. Merah , Putih , Hijau" , "D. Putih ,Merah" ],
  ["A. 85 cm" , "B. 70 cm" , "C. 60 cm" , "D. 80 cm" ],
  ["A. Berhenti" , "B. Jalan" , "C. Tiktokan" , "D. Gas terus!" ]
]  