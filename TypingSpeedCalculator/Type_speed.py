from time import *
import random as r
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
         error = error + 1
    return  error

def speed_time(time_s,time_e,userinput):
        time_delay = time_e - time_s
        time_R = round(time_delay,2)
        speed = len(userinput)/time_R
        return  round(speed) #give us rounded off value


#
# while True:
#   ck = input("Ready to test : yes / no :")
#   if ck ==  "yes":
test = ["A paragraph is a self-contained unit of units",
        "My name is ChVivek","Welcom to chtech vuyyuru"]

test1 = r.choice(test)
print("*********Typing Speed  Calculator*******")

print(test1)

time1 = time()
testinput = input("Enter :")
time2 = time()


print('Speed : ',speed_time(time1,time2,testinput),"w/second")
print("Error : ",mistake(test1,testinput))

 # elif ck == 'no':
 #     print("thank you")
 # else:
 #      print("Wrong input")
