import pandas as pd


class item:
    def __init__(self, items_diction, row_index):
        """
        costructor of class item
        items_diction: dictionary of items for a specific admin
        row_index: admin index
        """
        self.row_index = row_index
        self.items_diction = items_diction
    def getlist(self):
        return self.items_diction
    def update_file(self, row_index, item, newvalue):
        """
        used to update csv file after set
        row_index: admin index
        item : item i want to know its counter
        newvalue: the updated value

        """
        df = pd.read_csv("data.csv")

        # updating the column value/data
        df.loc[row_index, item] = newvalue

        df.to_csv("data.csv", index=False)

        print(df)


    def set_(self,element,newValue):
        """
           Set an item in csv file

           :return: none
           """


        if (element in self.items_diction):

            self.items_diction[element] = newValue
            self.update_file(self.row_index, element, newValue)
            print(self.items_diction)
        else:
            print("element is not found ")

    def get(self):
        """
         get the value of an item

         :return: none
       """
        element = input("Please enter the element to get its value")
        print(self.items_diction.get(element))




