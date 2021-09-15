import cv2
class numbers():
    a=int(input("Guess a number\n"))
    number=15
    if(a<number):
        print("Your guess is too low, Try a higher number")
    if(a>number):
        print("Your guess is too high, Try a lower number")
    if (a==number):
        print("Congratulation! Your guess is correct")
numbers()