from tkinter import *
import os

UID="Candidate"
PWD="jeemain"
def delete6():
  screen.destroy()

def delete5():
  screen_1.destroy()
 
def delete2():
  screen_3.destroy()
 
def delete3():
  screen_4.destroy()
 
def delete4():
  screen_5.destroy()
   
def login_sucess():
  global screen_3
  screen_3 = Toplevel(screen)
  screen_3.title("Successful")
  screen_3.geometry("800x600")
  Label(screen_3, text = "Login Sucessful").pack()
  Button(screen_3, text = "OK", command = lambda:[delete2(),delete6(),questions()]).pack()
  
 
def password_not_recognised():
  global screen_4
  screen_4 = Toplevel(screen)
  screen_4.title("Successful")
  screen_4.geometry("800x600")
  Label(screen_4, text = "Password Error").pack()
  Button(screen_4, text = "OK", command =delete3).pack()
 
def user_not_found():
  global screen_5
  screen_5 = Toplevel(screen)
  screen_5.title("Successful")
  screen_5.geometry("800x600")
  Label(screen_5, text = "Users Not Found").pack()
  Button(screen_5, text = "OK", command =delete4).pack()
 
   
def register_user():
  print("working")
   
  username_info = username.get()
  password_info = password.get()
 
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)
 
  Label(screen_1, text = "!! REGISTRATION SUCCESSFUL !!", fg = "green" ,font = ("calibri", 17)).pack()
  Button(screen_1, text = "ok", command = delete5).pack() 
def login_verify():
   
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
 
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
 
  else:
        user_not_found()
   
 
 
def register():
  global screen_1
  screen_1 = Toplevel(screen)
  screen_1.title("Register")
  screen_1.geometry("800x600")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(screen_1, text = "Please Enter the Information Carefully" , width = 30, height = 2 , font = ("calibri", 25) , fg = "green").pack()
  Label(screen_1, text = "").pack()
  Label(screen_1, text = "* Username * " , width = 30, height = 2 , font = ("calibri", 18)).pack()
  
  username_entry = Entry(screen_1, textvariable = username)
  username_entry.pack()
  Label(screen_1, text = "* Password * " , width = 30, height = 2 , font = ("calibri", 18)).pack()
  password_entry =  Entry(screen_1, textvariable = password)
  password_entry.pack()
  Label(screen_1, text = "" , width = 30, height = 3).pack()
  Button(screen_1, text = "Register", width = 30, height = 3, command = register_user , font = ("calibri", 18)).pack()
 
def login():
  global screen_2
  screen_2 = Toplevel(screen)
  screen_2.title("Login")
  screen_2.geometry("800x600")
  Label(screen_2, text = "Please enter details below to login" , width = 30, height = 2 , font = ("calibri", 25) , fg = "green").pack()
  Label(screen_2, text = "").pack()
 
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(screen_2, text = "Username * " , width = 30, height = 2 , font = ("calibri", 18)).pack()
  username_entry1 = Entry(screen_2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen_2, text = "").pack()
  Label(screen_2, text = "Password * " , width = 30, height = 2 , font = ("calibri", 18)).pack()
  password_entry1 = Entry(screen_2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen_2, text = "" ,  width = 30, height = 3).pack()
  Button(screen_2, text = "Login", width = 10, height = 1, command = lambda:[login_verify(),screen_2.destroy()] , font = ("calibri", 18)).pack()
   
   
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("800x600")
  screen.title("JEE MAIN Registration")
  Label(text = "JEE MAIN Registration", bg = "blue", width = "400", height = "5", font = ("Calibri", 24)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "3", width = "50", font = ("Calibri", 18) , command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "3", width = "50", font = ("Calibri", 18) , command = register).pack()

 
  screen.mainloop()
 
main_screen()

def questions():
  
  print("Welcome to the test!")
  score = 0
  # QUESTION 1
  Answer1 = input("Q1. If three successive terms of a G.P with common ratio r (r > 1)form the sides of a triangle ABC and [r] denotes greatest integer function, then [r] + [−r] is \n A.0 \n B.1 \n C.-1 \n D.None of these \n Answer: ")
  if Answer1 == "C":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer C")
      print("Score: ",score)
      print("\n")


  # QUESTION 2
  Answer2 = input("Q2. Root mean square velocity of a gas is x/ms at a pressure p atm and temperature T K. If pressure is made 2p under isothermal condition root mean square speed becomes \n A.2x \n B.4x \n C.x/2 \n D.x \n Answer: ")
  if Answer2 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")

  # QUESTION 3
  Answer3 = input("Q3. The rms velocity of molecules of a gas of density 4 kg m-3 and pressure 1.2 × 105 Nm-2 is \n A.900m/s \n B.120m/s \n C.600m/s \n D.300m/s \n Answer: ")
  if Answer3 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")

  # QUESTION 4
  Answer4 = input("Q4. Two numbers are chosen from 1, 3, 5, 7,… 147, 149 and 151 and multiplied together in all possible ways. The number of ways which will give us the product a multiple of 5, is \n A.1020 \n B.1030 \n C.95 \n D.75 \n Answer: ")
  if Answer4 == "A":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer A")
      print("Score: ",score)
      print("\n")

  # QUESTION 5
  Answer5 = input("Q5. The image of an object, formed by a plano-convex lens at a distance of 8m behind the lens, is real and is one third the size of the object. The wavelength of light inside the lens is 2/3 times the wavelength in free space. The radius of the curved surface of the lens is \n A.1m \n B.6m \n C.5m \n D.3m \n Answer: ")
  if Answer5 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")

  # QUESTION 6
  Answer6 = input("Q6. The resistance of a wire at room temperature 20°C is found to be 20W. Now to increase the resistance by 20%, the temperature of the wire must be [The temperature coefficient of resistance of the material of the wire is 0.002 per °C]. \n A.142 \n B.124 \n C.150 \n D.122 \n Answer: ")
  if Answer6 == "B":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer B")
      print("Score: ",score)
      print("\n")

  # QUESTION 7
  Answer7 = input("Q7. A spring of force constant k is cut into two pieces such that one piece is double the length of the other.Then the long piece will have a force constant of \n A.(2/3)k \n B.(3/2)k \n C.3k \n D.6k \n Answer: ")
  if Answer7 == "B":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer B")
      print("Score: ",score)
      print("\n")

  # QUESTION 8
  Answer8 = input("Q8. A circular disc rolls down an inclined plane. The ratio of the total kinetic energy to the rotational kinetic energy is \n A.1:3 \n B.3:2 \n C.2:3 \n D.3:1 \n Answer: ")
  if Answer8 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")

  # QUESTION 9
  Answer9 = input("Q9. A satellite is moving with a constant speed 'V’ in a circular orbit about the earth. An object of mass  ‘m’ is ejected from the satellite such that it just escapes from the gravitational pull of the earth. At   the time of its ejection, the kinetic energy of the object is \n A.5GMm/6R \n B.2GMm/3R \n C.GMm/2R \n D.GMm/3R \n Answer: ")
  if Answer9 == "A":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer A")
      print("Score: ",score)
      print("\n")

  # QUESTION 10
  Answer10 = input("Q10. What is the minimum energy required to launch a satellite of mass m from the surface of a planet of mass M and radius R in a circular orbit at an altitude of 2R? \n A.1/2mVV \n B.mVV \n C.3/2mVV \n D.2mVV \n Answer: ")
  if Answer10 == "B":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer B")
      print("Score: ",score)
      print("\n")

  # QUESTION 11
  Answer11 = input("Q.11The equation of the plane passing through the points (2, -1, 0), (3, -4, 5) and parallel  to the line 2x = 3y = 4z is:\nA.125x - 90y - 79z = 340 \n B.32x - 21y - 36z = 85\n C.73x + 61y - 22z = 85 \n D.29x - 27y - 22z = 85\n Answer: ")
  if Answer11 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 12
  Answer12 = input(" Q.12        Let A = {x1, x2, x3, x4, x5}; B = {y1, y2, y3, y4, y5} then the number of one-one mapping from A to B such that  f (x) != y ,i= 1, 2, … 5 is\nA.40\nB.44\nC.6\nD.24\n Answer: ")
  if Answer12 == "B":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer B")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 13
  Answer10 = input("Q.13	Iso-electric point of alanine is (pH = 6). At which pH, maximum concentration of zwitter ion of alanine will be present?\nA.pH > 6\nB.pH < 6\nC.pH = 6\nD. pH = 7\n Answer: ")
  if Answer10 == "C":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer C")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 14
  Answer10 = input("Q.14 The value of (1 – cot 3º)(1 – cot 7º)(1 – cot 11º)(1 – cot 34º)(1 – cot 38º)(1 – cot 42º) is equal to \nA.3\nB.2\nC.27\nD.8\n Answer: ")
  if Answer10 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")
      
  # QUESTION 15
  Answer10 = input("Q.15 If a, b, c are number of elements in sets A, B and C respectively and sum of number of all  subsets of A, B and C is 28, then maximum number of ordered triplets (a, b, c) is\nA.1\nB.2\nC.4\nD.6\n Answer: ")
  if Answer10 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 16
  Answer10 = input(" Q.16	What is the molarity of HCl in a solution prepared by dissolving 5.5 g HCl in 200 g ethanol if the density of the solution is 0.79 g/ml?\nA.2.1 M\nB.0.93 M\nC. 1.7 M\nD.0.58 M\n Answer: ")
  if Answer10 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 17
  Answer10 = input("Q.17	Ratio of sigma and pie bonds is maximum in \nA.	Naphthalene\nB.Tetra Cyanomethane\nC.Enolic form of urea\nD.Equal in all\n Answer: ")
  if Answer10 == "C":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer C")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 18
  Answer10 = input("Q.18.A listener is at rest with respect to the source of sound. A wind starts blowing along the lime joining the source and the observer. Which of the following quantities do not change?\nA.Wavelength\nB.Frequency\nC.Time Period\nD.Velocity of Sound \n Answer: ")
  if Answer10 == "B":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer B")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 19
  Answer10 = input(" Q.19 The YDSE is made in a liquid. The 10th bright fringe in the liquid lies where the 6th dark fringe lies in vacuum. The refractive index of the liquid is approximately.\nA.1.81\nB.1.54\nC.1.67\nD.1.20\n Answer: ")
  if Answer10 == "A":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer A")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 20
  Answer10 = input("Q.20 A cube of wood supporting 200 gm mass just floats in water (density = 1g/cc). When the mass is removed, the cube rises by 2 cm. The volume of cube is \nA.1000 cc\nB.800 cc\nC.500 cc\nD.none of these \n Answer: ")
  if Answer10 == "A":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer A")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 21
  Answer10 = input(" Q.21. For 1st law of thermodynamics, select the correct option:\nA.The energy of a closed system is constant.\nB. 1st law is commonly started as the law of conservation of energy i.e., energy canneither be created nor be destroyed.\nC.It is applicable only for reversible process.\nD.Both A & B\n Answer: ")
  if Answer10 == "B":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer B")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 22
  Answer10 = input(" Q.22Select the correct option :\nA. Gold sol is negatively charged\nB.Peptization is method of purification of sols.\nC.Persistent dialysis is method of coagulation.\nD.Both A and C\n Answer: ")
  if Answer10 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 23
  Answer10 = input("Q.23 Select the incorrect option :\nA.Each species appearing in balanced chemical equation must appear in kinetic rate law.\nB.Bimolecular elementary reaction is always second order.\nC.Hydrolysis of ester in alkaline medium is bimolecular second order reaction.\nD.Order and molecularity may be same for a chemical reaction.\n Answer: ")
  if Answer10 == "A":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer A")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 24
  Answer10 = input("Q.24The distance between two adjuscent carbon atoms is maximum in :\nA.Diamond\nB.Graphite\nC.Benzene\nD.Ethene\n Answer: ")
  if Answer10 == "A":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer A")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 25
  Answer10 = input("Q.25The reaction of white phosphorus with sodium hydroxide solution gives : \nA. Phosphine and sodium salt of a dibasic acid\nB.Phosphine and sodium salt of a monobasic acid\nC.Phosphine and sodium salt of a tribasic acid\nD.None of these\n Answer: ")
  if Answer10 == "B":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer B")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 26
  Answer10 = input("Q.26ABCD is a rhombus. The circumradii of triangle ABD and triangle ACD are 25/2 and 25. Then the area of rhombus is: \nA.400 sq.unit\nB.600 sq. unit\nC.200 sq. unit\nD. 800 sq. unit\n Answer: ")
  if Answer10 == "A":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer A")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 27
  Answer10 = input("Q.27 The equation of the plane through the intersection of the planes x + 2y + z - 1 = 0 and 2x + y + 3z - 2 = 0 and perpendicular to the plane x+y+z-1=0 and x + ky + 3z - 1 = 0. Then the value of k is: \nA.-5/2\nB.-3/2\nC.5/2\nD.3/2\n Answer: ")
  if Answer10 == "C":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer C")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 28
  Answer10 = input("Q.28The average marks of 10 students in a class was 60 with a standard deviation 4, while the average marks of other ten students was 40 with a standard deviation 6. If all the 20 students are taken together, their standard deviation will be\nA.5\nB.7.5\nC.9.8\nD.11.2 \n Answer: ")
  if Answer10 == "D":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer D")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 29
  Answer10 = input("Q.29 By passing vapours of phenol over heated zinc dust will produce :\nA.Benzoic Acid \nB.Quinone\nC.Benzene\nD.Malic Acid\n Answer: ")
  if Answer10 == "C":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer C")
      print("Score: ",score)
      print("\n")
    
  # QUESTION 30
  Answer10 = input("Q.30Which of the following pyrimidine base present in RNA ?\nA.Ademine\nB.Guanine\nC.Uracil\nD.All of these \n Answer: ")
  if Answer10 == "C":
      score = score + 4 
      print("Correct!!")
      print("Score: ",score)
      print("\n")
  else:
      score = score - 1
      print("Incorrect The answer C")
      print("Score: ",score)
      print("\n")

      #Total Marks
  print("Total Marks:")
  print("Score: ",score)
  print("\n")

  #Average Marks
  average = (score) / 30
  print ("Average Score: ",average)
  #!/usr/bin/python

questions()



  





