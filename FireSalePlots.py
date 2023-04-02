import requests
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

#fill this and put it in a for loop ok cool thanks
def arrayOfIDs(filename):
    
    df = pd.read_csv(filename)
    item_IDS = []

    for item in df['Unnamed: 6']:
        item_IDS.append(item)

    for i in range(4):
        item_IDS.remove(item_IDS[0])
        print(item_IDS)
    
    for item in item_IDS: 
        getDataForItem(skyblock_id=item)



def getDataForItem(skyblock_id):
    data = requests.get(f"https://sky.coflnet.com/api/item/price/{skyblock_id}/history/month")
    resp = data.json()
    
    avg_array = []
    min_array = []
    max_array = []
    date_array = []
    for d in resp:
        date_str = d["time"]
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        day_month_str = f'{date.day:02d}-{date.month}'
        avg_rounded = round(d["avg"], 0)
        min_rounded = round(d["min"], 0)
        max_rounded = round(d["max"], 0)
        max_array.append(max_rounded)
        min_array.append(min_rounded)
        avg_array.append(avg_rounded)
        date_array.append(day_month_str)

    avg_in_millions = [val / 1000000 for val in avg_array]
    min_in_millions = [val / 1000000 for val in min_array]
    max_in_millions = [val / 1000000 for val in max_array]
    fig, ax = plt.subplots()
    ax.plot(date_array, avg_in_millions, label='Average')
    ax.plot(date_array, min_in_millions, color='r', label='Minimum')
    ax.plot(date_array, max_in_millions, color='g', label='Maximum')
    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.state('zoomed')
    plt.xlabel('Date (in DD-MM)')
    plt.ylabel('Price (in millions)')
    plt.title('Price History for Skyblock Item ID: {}'.format(skyblock_id))
    ax.legend()
    figure = plt.gcf()
    figure.set_size_inches(13.66, 7.28)
    plt.savefig('SkinPlots/' + '2023/' + skyblock_id + '.png', dpi=100, bbox_inches='tight')
    print(skyblock_id)
    plt.close()
    
def ask():
    skyblock_id = input("INPUT SKYBLOCK ID: ")
    getDataForItem(skyblock_id)

def test():
    arrayOfIDs(input("file name with .csv at the end"))

test()