
class ListShares:

    def __init__(self, shares_list):
        self.shares_list = shares_list

    @staticmethod
    def purchase_shares(purchase_value, share):

        # Add shares to the list until the total shares value reach 500 euros
        while purchase_value < 500:

            share += 1

        else:

            print("We spent the maximum amount of shares per customers(500 euros)")

    def prevent_duplicated_share(self, share_index, purchase_value):

        if self.shares_list[share_index] in self.shares_list:

            pass

        else:

            self.purchase_shares(purchase_value, self.shares_list[share_index])
        
