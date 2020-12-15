import datetime

import pandas as pd


class SRService:

    @staticmethod
    def getHeaders():
        return [
            "sale",
            "salesAmountInEuro",
            "timeDelayForConversion",
            "clickTimestamp",
            "nbClicks1Week",
            "productPrice",
            "productAgeGroup",
            "deviceType",
            "audienceId",
            "productGender",
            "productBrand",
            "productCategory1",
            "productCategory2",
            "productCategory3",
            "productCategory4",
            "productCategory5",
            "productCategory6",
            "productCategory7",
            "productCountry",
            "productId",
            "productTitle",
            "partnerId",
            "userId"
        ]


