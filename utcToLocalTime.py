from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd

def timeAsia(dataFrame):
    # print(dataFrame)
    timeDate = dataFrame["Time_Frame"].dt.strftime("%Y-%m-%d %X")
    timeList = []
    for dt in timeDate:
        splitTD = dt.split(" ")
        dateSplit = splitTD[0].split("-")
        secondStrip = splitTD[1].replace(".", " ").split(" ")
        timeSplit = secondStrip[0].split(":")
        # print(dateSplit, timeSplit)
        convertedTime = datetime(int(dateSplit[0]), int(dateSplit[1]),int(dateSplit[2]), int(timeSplit[0]), int(timeSplit[1]), int(timeSplit[2]), tzinfo=ZoneInfo('UTC'))
        asianTime = convertedTime.astimezone(ZoneInfo('Asia/kolkata')) 
        # print(asianTime)
        data = str(asianTime)
        timeList.append(data)   
    # print(timeList)

    dataFrame['TimeFrame'] = timeList
    print(dataFrame)
    print(dataFrame.info())


if __name__ == "__main__":
    data = pd.DataFrame("data.csv")
    print(data.info())
    timeAsia(data)