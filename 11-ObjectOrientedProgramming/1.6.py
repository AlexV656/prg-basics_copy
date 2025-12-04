class Phone():
    def __init__(self,model,size,price):
        self.model = model
        self.price = price
        self.size = size 
        
    def display_model(self):
        print(self.model)
    
    def display_price(self):
        print(self.price)
    
    def display_size(self):
        print(self.size)
    