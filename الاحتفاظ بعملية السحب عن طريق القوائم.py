class ATM :
  def __init__(self,balance,bank_name):
        self.balance=balance
        self.bank_name=bank_name
        self.withdrawals_list = []
  def widthraw(self,request):
        print(self.bank_name,'current balance=',str(self.balance),'$')
        if request > self.balance:
           print('the mony in the ATM not enough ')
        elif request < 0:
            print('please enter the mony you need')
        else:
          self.balance -= request
          self.withdrawals_list.append(request)

          notes = [100, 50, 10, 5]
          for note in notes:
                while request >= note:
                    request -= note
                    print("give " + str(note))
          if request % 5 != 0 :
              print('give ' + str(request) + ' pieces')
              request = 0
              
        print('Remaining Mony In The ATM', self.balance)      
        print('')
        return self.balance
        
  def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print('Withdrawaled Mony =',withdrawal)            

                   
balance1=500
balance2=1000

atm1 = ATM(balance1,"Smart_bank")   
atm2 = ATM(balance2,"Taslef_bank")  

atm1.widthraw(100)
atm1.widthraw(300)

atm2.widthraw(100)
atm2.widthraw(800)

atm1.show_withdrawals()
atm2.show_withdrawals()
