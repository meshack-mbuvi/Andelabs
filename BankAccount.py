class BankAccount(object):
  '''
  This is the parent class from which other class inherit
  '''
  def withdraw(self):
    '''
    This method will be overriden by child class
    '''
    pass
  def deposit(self):
    pass
  
class SavingsAccount(BankAccount):
  '''
    This class Class inherits from BankAccount class
        
    '''
  def __init__(self):
    self.__balance=500
  @property
  def balance(self):
    return self.__balance
  def deposit(self,deposit):
    if deposit<0:
      return 'Invalid deposit amount'
    else:
      self.__balance+=deposit
      return self.__balance
  def withdraw(self,amount):
    if amount<0:
      return 'Invalid withdraw amount'
    elif amount>self.__balance:
      return 'Cannot withdraw beyond the current account balance'
    if (self.__balance-amount)<500:
      return 'Cannot withdraw beyond the minimum account balance'
    self.__balance-=amount
    return self.__balance
  
class CurrentAccount(BankAccount):
  '''
    This class Class inherits from BankAccount class
        
    '''
  def __init__(self):
    self.__balance=0
  @property
  def balance(self):
    return self.__balance
  def deposit(self,amount):
    if amount<0:
      return 'Invalid deposit amount'
    self.__balance+=amount
    return self.__balance
  def withdraw(self,amount):
    if amount<0:
      return 'Invalid withdraw amount'
    if amount>=self.__balance:
      return 'Cannot withdraw beyond the current account balance'
    self.__balance-=amount
    return self.__balance
def test():
    mbuvi = SavingsAccount()
    print(mbuvi.deposit(1000))
    print(mbuvi.withdraw(1500))
    print(mbuvi.balance)

    mbuvi_current_account = CurrentAccount()
    print(mbuvi_current_account.deposit(1500))
    print(mbuvi_current_account.withdraw(5600))
    print(mbuvi_current_account.balance)

    

if __name__ == '__main__':
  test()
