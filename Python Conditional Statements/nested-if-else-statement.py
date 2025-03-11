age=int(input("Enter your age:"))
if(age>=18):
    print("you can vote.")
    print("you can drive.")
    if(age>=20):
        print("you can drink.")
    else:
        print("you can't drink.")
else:
    print("you are smaller then 18 so you can't vote.")