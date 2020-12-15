from PartnerDataReader import PartnerDataReader
from PerPartnerSimulator import PerPartnerSimulator
import matplotlib.pyplot as plt


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

        for x in range(self.allDays):
            data = partnerDataReader.getDay(self.currentDay)
            profit = perPartnerSimulator.calculatePerDayProfitGainFactors(data, perClickCost)
            accumulatedProfit = accumulatedProfit + profit

            print("Day " + str(x) + ": " + str(profit) + " Accumulated: " + str(accumulatedProfit))

            accumulatedProfits.append(accumulatedProfit)
            days.append(self.currentDay)
            self.currentDay = self.currentDay + 1;

        plt.plot(days, accumulatedProfits)
        plt.show()


