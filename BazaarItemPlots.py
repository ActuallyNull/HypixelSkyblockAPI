import matplotlib.pyplot as plt
import requests
from datetime import datetime

# method for asking which item using ID and take the data (buy and sell)

def askItemID():
    itemID = input("Input Bazaar Item ID: ")
    dateNow = datetime.date()
    itemGet = requests.get(f"https://sky.coflnet.com/api/bazaar/{itemID}/history?start=2023-03-01&end=2023-04-01")
    itemDataJSON = itemGet.json()
    buyPriceArray = []
    sellPriceArray = []
    dateArray = []
    for item in itemDataJSON:
        date_str = item["timestamp"]
        try:
            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        except:
            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        day_month_str = f'{date.day:02d}-{date.month}'
        buyPriceArray.append(round(item["buy"], -1))
        sellPriceArray.append(round(item["sell"], -1))
        dateArray.append(day_month_str)
    fig, ax = plt.subplots()
    ax.plot(dateArray, buyPriceArray, label = "Buy Price")
    ax.plot(dateArray, sellPriceArray, label = "Sell Price")
    plt.xlabel("Date DD-MM")
    plt.ylabel("Price in coins")
    plt.legend()
    plt.show()
    print(len(buyPriceArray))
    print(len(sellPriceArray))
    print(dateArray)

askItemID()