pricePerUnit = 10.768
def getDiscount(itemCount):
    if(itemCount <=20):
        return 0
    elif(itemCount > 20 and itemCount <=50):
        return 10 / 100*itemCount
    elif (itemCount > 20 and itemCount <= 50):
        return 20 / 100 * itemCount
    elif (itemCount > 100):
        return 25 / 100 * itemCount
    else:
        print("Discount calculation failed.")


def totalPrice(itemCount):
    return round(itemCount * pricePerUnit - (getDiscount(itemCount) * pricePerUnit),2)


print(totalPrice(9))


