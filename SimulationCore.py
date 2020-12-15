from datetime import datetime

from Optimizer import Optimizer
from PartnerDataReader import PartnerDataReader
from PerPartnerSimulator import PerPartnerSimulator
import matplotlib.pyplot as plt
import json


class SimulationCore:

    currentDay = 0;
    allDays = 33;
    partnerId = -1;

    def __init__(self, partnerId):
        self.partnerId = partnerId
        self.execute()

    def execute(self):
        partnerDataReader = PartnerDataReader(self.partnerId)
        perPartnerSimulator = PerPartnerSimulator()

        self.currentDay = 0;
        perClickCost = perPartnerSimulator.getPerClickCost(partnerDataReader.getDay(-1))
        print("PerClickCost: " + str(perClickCost))
        accumulatedProfits = []
        days = []
        accumulatedProfit = 0.00
        allProducts = []

        jsonLog = {}
        jsonLog['days'] = []

        for x in range(self.allDays
                 ):
            data = partnerDataReader.getDay(self.currentDay)
            profit = perPartnerSimulator.calculatePerDayProfitGainFactors(data, perClickCost)
            accumulatedProfit = accumulatedProfit + profit
            timeCol = data[3]
            print("Day " + str(x) + ": " + str(profit) + " Accumulated: " + str(accumulatedProfit))
            accumulatedProfits.append(accumulatedProfit)
            days.append(self.currentDay)

            products = perPartnerSimulator.getProducts(data)


            for y in range(len(products)):
                if products[y] not in allProducts:
                    allProducts.append(products[y])
                    print(datetime.utcfromtimestamp(timeCol[y]))

            optimizer = Optimizer(allProducts)
            excluded = optimizer.getExcludedProductsPseudoradnomly()
            excluded.sort()

            print("Excluded: " + str(len(excluded)))
            for y in range(len(excluded)):
                print(excluded[y])

            jsonLog['days'].append({
                'day': str(datetime.utcfromtimestamp(timeCol[0]).year) + "-" +
                       str(datetime.utcfromtimestamp(timeCol[0]).month) + "-" +
                       str(datetime.utcfromtimestamp(timeCol[0]).day),
                'excluded': excluded,
            })

            self.currentDay = self.currentDay + 1;

        with open('log.json', 'w') as outfile:
            json.dump(jsonLog, outfile)

        print('JSON saved')
        #plt.plot(days, accumulatedProfits)
        #plt.show()


