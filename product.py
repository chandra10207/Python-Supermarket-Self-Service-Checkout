class Product():
    product_list = [
            {
                'name': 'Milk 1 litres',
                'price': 10,
                'bar_code': '111'                  
                },
            {
                'name': 'Bread',
                'price': 1,
                'bar_code': '222'
                },
            {
                'name': 'Coke',
                'price':2,
                'bar_code':'333'
                }
        ]   
        
    def __init__(self,name,price,bar_code):
        self.name = name
        self.price = price
        self.bar_code = bar_code

    def display_product(self):
        print(self)
        #print 'Human readable: ', str(self)
        #print repr(self)       

    def display_product_list(self):
        print("Our inventory")

    def check_product_on_inventory(self):
        found = False       
        for index, product in enumerate(self.product_list):
            #print(product)
                        
            if self.bar_code == product['bar_code']:                
                product_found = {'name': product['name'],'price': product['price'],'bar_code': product['bar_code']}
                found = True
                print(product['name']," -  $"+str(product['price']),'\n' )
                
                
        if found == True :            
            return product_found
        else:
            return False
         

    def set_bar_code(self,bar_code):
        
        self.bar_code = bar_code

    def set_price(self,price):
        self.price = price    

   
        
        
