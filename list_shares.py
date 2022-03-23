
class ListShares:

    def __init__(self, shares_list):
        self.shares_list = shares_list

    @staticmethod
    def purchase_shares(purchase_value, share):

        while purchase_value < 500:

            share += 1

        else:

            print("We spent the maximum amount of shares per customers(500 euros)")
        
