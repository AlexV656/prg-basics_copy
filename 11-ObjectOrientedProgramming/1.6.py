class Phone():
    def __init__(self,model,size,price):
        self.model = model
        self.price = price
        self.size = size 
        
    def display_model(self):
        print(self.model,'model of the phone')
    
    def display_price(self):
        print(self.price,'price of the phone')
    
    def display_size(self):
        print(self.size,'size of the phone')
    