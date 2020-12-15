import random
import pandas as pd


class Optimizer:

    howManyRatio = 20
    randomSeed = 12
    products = []

    def __init__(self, productsForPartnerInDay):
        print("Optimizer inited")
        self.products = productsForPartnerInDay

    def nextDay(self):
        return []

    def getProductsSeenToday(self):
        args = len(self.data.index)
        producktsCol = self.data[19]
        ret = []

        for x in range(args):
            ret.append(producktsCol[x])

        return ret

    def getExcludedProducts(self):
        return []

    def getExcludedProductsPseudoradnomly(self):
        dummy_list_of_potentially_excluded_products = self.products
        dummy_list_of_potentially_excluded_products = list(dummy_list_of_potentially_excluded_products)
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / self.howManyRatio)
        random.seed(self.randomSeed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products,
                                          dummy_how_many_products)

        return excluded_products

