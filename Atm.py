class Atm:
   def __init__(self,CardNo,Pin):
      self.CardNo = CardNo
      self.Pin = Pin
   def BalanceEnquiry(self):
      print("Your Card Balance is:- 1,000,450,000")
   def CashWithdrawl(self,amount):
      new_amount=1000450000-amount
      print("Your Card Balance is "+str(new_amount))

      
      
def main():
   Card_No = input("insert your card number:- ")
   Pin_No = input("insert your Pin :- ")
   
   user1= Atm(Card_No,Pin_No)
   user1.BalanceEnquiry()
   amount = int(input("enter the amount:- "))
   user1.CashWithdrawl(amount)
   

main()

