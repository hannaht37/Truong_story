# write a program that will ask the user what their age is and then determine if they are old enough to vote and respond appropriately

age = int(input("How old are you? "))
if(age == 18):
    print("Hey, you're just old enough to vote!")
if(age < 18):
    print("You're not old enough, but you are almost there! You just need to be " + str(18 - age) + " years older!")
if(age > 18):
    print("You have been voting for " + str(age - 18) + " years now! Who are you planning on voting for in the next election?")