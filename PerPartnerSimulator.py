import pandas as pd

class PerPartnerSimulator:

    def __init__(self):
        print("PerPartnerSimulatior inited")

    def calculatePerDayProfitGainFactors(self, dataForPartnerInDay: pd.DataFrame, perClickCost):
        clicks = len(dataForPartnerInDay.index)
        sum = 0.0
        salesCol = dataForPartnerInDay[0]
        priceCol = dataForPartnerInDay[1]

        for x in range(clicks):
            if salesCol[x] == 1:
                sum = sum + pd.to_numeric(priceCol[x])

        profitPerDay = 0.22 * sum - perClickCost * clicks
        #print("Clicks: " + str(clicks) + " Profit: " + str(profitPerDay))
        return profitPerDay

    def getPerClickCost(self, wholeDataForPartner: pd.DataFrame):
        clicks = len(wholeDataForPartner.index)
        sum = 0.0
        salesCol = wholeDataForPartner[0]
        priceCol = wholeDataForPartner[1]

        for x in range(clicks):
            if salesCol[x] == 1:
                sum = sum + pd.to_numeric(priceCol[x])

        return 0.12 * sum / clicks

    def getProducts(self, dataForPartnerInDay: pd.DataFrame):
        args = len(dataForPartnerInDay.index)
        productCol = dataForPartnerInDay[19]
        ret = []

        for x in range(args):
            if productCol[x] not in ret:
                ret.append(productCol[x])

        return ret;