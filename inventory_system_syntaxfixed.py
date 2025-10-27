import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename="inventory.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=[]):
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning("%s not found" % item)

def getQty(item):
    return stock_data.get(item, 0)

def printData():
    for i, qty in stock_data.items():
        print(f"{i}: {qty}")

def main():
    addItem("apple", 10)
    addItem("banana", 2)
    addItem("orange", 1)
    removeItem("apple", 3)
    print("Apple stock:", getQty("apple"))
    printData()

if __name__ == "__main__":
    main()
