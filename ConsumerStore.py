import numpy as np
import pandas as pd

class ConsumerStore():
    
    '''
    This method is used to connect the object with the Cunsomer Store class. 
    Function reads the Master Table(Excel file) and converts it in to dictionary.
    Dictionary contains two elements. Item and Price. Later's we'll add a thrid element Count.
    Going forward this dictionary will be used to which keeps track of count of each item scanned and also update the Price based on rules.  
    '''
    def __init__(self):
        print('New Customer')
        self.df = pd.read_excel('Master Table.xlsx')
        item_dict = {}
        for i in self.df['item_code']:
            item_dict[i] = [self.df[self.df['item_code']==i].price.values[0],self.df[self.df['item_code']==i].item_list.values[0],0]
        
        self.item_dict = item_dict
        
    
    
    '''
    This method is used to record the added items and keeps a track of it.
    '''
    def scan(self,item):
        self.item = item
        print('{} has been added in the cart'.format(item))
        for i in self.item_dict.keys():
            if i == item :
                self.item_dict[i][2] = self.item_dict[i][2] + 1 
                
                
                    
    '''
    This method is used to view the total item scanned and will display the total amount before applying discount.
    This method should be executed just before checkout.    
    '''
    def item_scanned(self):
        
        sum_tot = 0
        for key,value in self.item_dict.items():
            print(value[2],' ',value[1],' MRP ',value[0],' : ',value[0]*value[2])
            sum_tot = sum_tot + value[0]*value[2]
            
        print('\n Total Amount with out discount rules : ',sum_tot)
        
    
    
    '''
    This method is used to apply the all the purchasing discount rules.
    In future if rules are to modified and removed then this function needs to be edited.
    '''
    
    def checkout(self):
        
        #Rule 1
        non_chargeable_nsh = int(np.floor(self.item_dict["nsh"][2]/3))
        self.item_dict["nsh"][2] = self.item_dict["nsh"][2] - non_chargeable_nsh

        #Rule 2
        if self.item_dict["stv"][2] > 4:
            self.item_dict["stv"][0] = 499.99

        
        sum_tot = 0
        for key,value in self.item_dict.items():
            print(value[2],' ',value[1],' billed @ ',value[0],' : ',value[0]*value[2])
            sum_tot = sum_tot + value[0]*value[2]
    
    
        print('\n Net Amount to be paid : ',sum_tot)
        
        #Rule 3    
        if self.item_dict["cac"][2]>0:
            print('\n {} Chargers have been offered for free with purchase Central AC '.format(self.item_dict["cac"][2]))
        
        #Print statement to display the discounted NIKE SHOE
        if non_chargeable_nsh > 0:
            print('\n {} Nike Shoe have been offered for free '.format(non_chargeable_nsh))
