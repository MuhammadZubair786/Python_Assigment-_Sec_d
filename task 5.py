name = input("Enter Student Name :")
a1 = int(input("Enter Math Marks :"))
a2 = int(input("Enter Urdu Marks :"))
a3 = int(input("Enter Computer Marks :"))
a4 = int(input("Enter Python Marks :"))
a5 = int(input("Enter English Marks :"))
tmark = 500
tsum = a1+a2+a3+a4+a5
per = (tsum*100/tmark)

print(f"\n********************Marksheet of {name}********************\n")
print(f"\t\tMath Mark :{a1}\n\t\tUrdu Mark :{a2}\n\t\tComputer Mark :{a3}\n\t\tPython Mark :{a4}\n\t\tEnglish Mark :{a5}")
print("\t\tTotal Marks :  500")
print(f"\t\tObtainted Marks : {tsum}")
print(f"\t\tPercentage : {per}")

if(per>80):
    print("\t\t PASS ")
    print("\t\tGrade :A +")

elif(per<80 and per >70):
    print("\t\t PASS ")
    print("\t\tGrade :A ")

elif(per<70 and per >60):
    print("\t\t PASS ")
    print("\t\tGrade :B+ ")

elif(per<70 and per >60):
    print("\t\t PASS ")
    print("\t\tGrade :B ")

elif(per<60 and per >50):
    print("\t\t PASS ")
    print("\t\tGrade :C ")

elif(per<50 and per >40):
    print("\t\t PASS ")
    print("\t\tGrade :D")

else:
    print("\t\t FAIL ")
