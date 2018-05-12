from product import Product
from checkoutregister import CheckoutRegister
from time import gmtime, strftime
#import sys
import os
import sys
current_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
wishlist = []

def scan_product():
    barcode = input("\nPlease enter the barcode of your item: ")
    p1 = Product("","",barcode)
    search_product = p1.check_product_on_inventory()
    if(search_product == False):
        print("This product does not exist in our inventory.\n")
        scan_another()
    else:        
        wishlist.append(search_product)
        scan_another()
    
def scan_another():
    scan_another = input("Would you like to scan another product? (Y/N)")
    if(scan_another == 'y' or scan_another == 'Y'):
        scan_product()

def main():
    scan_product()
    c1 = CheckoutRegister(current_date_time,wishlist)
    total_payment = c1.calculate_payment_due()
    change = c1.pay_money(total_payment)
    #print("Change:",change)
    c1.print_receipt(change)
    print("\nThank you for shopping at FedUni!")

    next = input("(N)ext customer, or (Q)uit? ")
    if(next == "n" or next == "N"):
        wishlist[:] = []
        main()     
    else:
        #sys.exit(0)
        exit()

print("\n--------Welcome to FedUni checkout!--------\n")

main()


    
