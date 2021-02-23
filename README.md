# ConsumerStore
Build a system that based on some given purchasing rules that provides the final total checkout cost.

Approach

Build a classe with four methods. The class will emulate a the billing system of a physical consumer store and each object of this class will represent a unique customer.

1. __init__() acts like a constructor. This method reads the master table containing items, item codes, price and converts it into a dictionary.

2. scan() - Method used to read the scanned items and record the count in the dictionary created in the __init__

3. item_scanned() - Method used to display the total scanned items w.r.t to the MRP before appplying purchasing discount.

4. checkout() - Used to incorporate all the purchase rules and display the net amount to be paid by the customer
