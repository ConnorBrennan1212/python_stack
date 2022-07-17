class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent)

    
# Create two shoe instances
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)

skater_shoe.on_sale_by_percent(.5)
print(skater_shoe.price)
        
# # The skater shoes go on sale by 20% reduced price:
# skater_shoe.price = skater_shoe.price * (1 - 0.2)
        
# # The dress shoes go on sale by 10% reduction:
# dress_shoe.price = dress_shoe.price * (1 - 0.1)
        
# # The skater shoes go on sale AGAIN by another 10%:
# skater_shoe.price = skater_shoe.price * (1 - 0.1)

