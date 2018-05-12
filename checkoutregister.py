class CheckoutRegister():
    def __init__(self,checkout_date,checkout_items):
        self.checkout_date = checkout_date
        self.checkout_items = checkout_items

    def add_item_to_cart(self,p):
        self.checkout_items.append(p)
        

    def display_checkout_items(self):
        print("Checkout Items")
        print(self.checkout_items)


    def calculate_payment_due(self):
        cart_items = self.checkout_items
        cart_totals = 0

        for index, product in enumerate(self.checkout_items):
            cart_totals += product['price']
        self.due = cart_totals
        return cart_totals

    def pay_money(self,total):
        amount_to_pay = total
        print("\nPayment due: $"+str(amount_to_pay))
        #self.accept_payment(amount_to_pay)        
        #amount_to_pay = input("Please enter an amount to pay: ")
        change = self.accept_payment(amount_to_pay)
        return change
        

    def accept_payment(self, amount_to_pay):
        #print("accept payment")
        paid = float(0.0)
        customer_pay = float(0.0)
        due = float(0.0)
        total = amount_to_pay
        due = True
        
        while due == True:
            try:
                paid = float(input("\nPlease enter an amount to pay: "))
                if(paid < 0.0):
                    print("We don't accept negative money!\n")
                    continue
                else:
                    customer_pay += paid
                    self.customer_pay = customer_pay
                    if(paid < total):
                        due = total - paid
                        total = due
                        print("Payment due: $"+str(due))
                        due = True
                        continue   
                    else:
                        change = paid - total
                        self.change = change
                        #print("Change: ",change)
                        return change
                    break
                break
                    #due = False
                    #self.print_receipt(change)
                    
            except ValueError:
                print('Please enter a valid floating point value.')
        return change
                        
    def print_receipt(self,change):
        print("\n----- Final Receipt -----\n")

        for index, item in enumerate(self.checkout_items):
            print(item['name'],'     $'+str(item['price']))

        print("\n")
        print("Total amount due:",'     $'+str(self.due))
        print("Amount Received",'       $'+str(self.customer_pay))
        print("Change Given",'          $'+str(self.change),'\n')


    
        
        
        
        
        
                        
                        
                

        
            
            
        
        
   
