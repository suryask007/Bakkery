today_special={"chips":{"Banana chips":50,"potato chips":30,"tomato chips":40},
               "Biscuit":{"Parle-g":20,"Mari gold":25,"Good day":30},
               "Pups":{"Egg":15,"veg":15,"Kalan":20,"Chicken":25}}
print("=============== Today special ============")
for i in today_special.keys():
    print(i)
print("===============What you want sir...=========")
item=[]
for i in range(0,3):
    user=input("Enter your choice:")
#items 1
    if user=="chips":
        for chips,rate in today_special["chips"].items():
            print(chips,":",rate)
        #chose which item you want
        user1=input("enter which chips you want:")
        if user1=="Banana chips":
            print(today_special["chips"]["Banana chips"])
            item.append(today_special["chips"]["Banana chips"])
        elif user1=="potato chips":
            print(today_special["chips"]["potato chips"])
            item.append(today_special["chips"]["potato chips"])
        elif user1=="tomato chips":
            print(today_special["chips"]["tomato chips"])
            item.append(today_special["chips"]["tomato chips"])
        else:
            print("enter correctly")
#items 2            
    elif user=="Biscuit":
        for Biscuit,rate in today_special["Biscuit"].items():
            print(Biscuit,":",rate)
    #chose which item you want
        user2=input("Enter Whih Biscuit you want:")
        if user2=="Parle-g":
            item.append(today_special["Biscuit"]["Parle-g"])
            print(today_special["Biscuit"]["Parle-g"])
        elif user2=="Mari gold":
            item.append(today_special["Biscuit"]["Mari gold"])
            print(today_special["Biscuit"]["Mari gold"])
        elif user2=="Good day":
            item.append(today_special["Biscuit"]["Good day"])
            print(today_special["Biscuit"]["Good day"])
        else:
            print("Enter correctly...")
#items 3
    elif user=="Pups":
        for Pups,rate in today_special["Pups"].items():
            print(Pups,":",rate)
        #chose which item you want
        user3=input("Enter Whih Pups you want:")
        if user3=="Egg":
            item.append(today_special["Pups"]["Egg"])
            print(today_special["Pups"]["Egg"])
        elif user3=="veg":
            item.append(today_special["Pups"]["veg"])
            print(today_special["Pups"]["veg"])
        elif user3=="Kalan":
            item.append(today_special["Pups"]["Kalan"])
            print(today_special["Pups"]["Kalan"])
        elif user3=="Chicken":
            item.append(today_special["pups"]["Chicken"])
            print(today_special["pups"]["Chicken"])
        else:
            print("Enter correctly...")
    else:
        print("we have above 3 items only")
print("you purchesed:")
for i in item:
    print(i)
print("=========")
#Sum the total items
total=sum(item)
print("your bill is:",total)
print("=================")
#calculate the customer given amount
user_amount=int(input("enter the customer given amount:"))
Balance=user_amount-total
print("please return the balance amount to customer:",Balance)


