class Payment:

    def __init__(self,wallet_balance,order_id,status,customer_id):
        self.wallet_balance=wallet_balance
        self.order_id=order_id
        self.status=status
        self.customer_id=customer_id


    def details(self):
        print("Hello Details Method in Parent class.....")
        print(f"""Wallet Balance : {self.wallet_balance} , order Id {self.order_id} , 
               status = {self.status} and customer Id. {self.customer_id} """)


class UPI(Payment):

    def details(self):
        print("Hello UPI Details.......")
        super().details()

    def pay(self):
        print("Pay Here ........")

payment=UPI("100000","#123","Order Placed","1234567")
payment.details()