import pandas as pd

class PartnerDataReader:

    partnerId = 0

    def __init__(self, partnerId):
        self.partnerId = partnerId

    def getDay(self, day):
        path = "C:/SR/" + self.partnerId
        if (day != -1):
            path = path + ("_" + str(day))
        path = path + ".csv"

        data = pd.read_csv(path, header=None, parse_dates=True, sep="\t")
        return data