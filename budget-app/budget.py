class Category:

  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.ledger = []
    self.withdrawals = 0
    self.deposits = 0

  def deposit(self, amount, description=''):
    # Error check amount?
    # add entry to ledger, update balance and total deposits amount
    self.ledger.append({'amount': amount, 'description': description})
    self.balance += amount
    self.deposits += amount
    return None

  def withdraw(self, amount, description=''):
    # Error check amount?
    # if insufficient funds, do nothing
    if not self.check_funds(amount):
      return False
    # if sufficient funds
    else:
      # add entry to ledger, update balance and total withrawals amount
      self.ledger.append({'amount': -amount, 'description': description})
      self.balance -= amount
      self.withdrawals += amount
      return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, otherCategory):
    # if insufficient funds, do nothing
    if not self.check_funds(amount):
      return False
    else:
      # withdraw from this category, deposit to the other category
      self.withdraw(amount, 'Transfer to {}'.format(otherCategory.name))
      otherCategory.deposit(amount, 'Transfer from {}'.format(self.name))
      return True

  def check_funds(self, amount):
    # use get_balance() instead of direct?
    return True if self.balance >= amount else False

  def __str__(self):
    # category title
    title = self.name.center(30, '*') + '\n'
    items = ''
    # list ledger items line by line for the category
    for item in self.ledger:
      desc = item['description']
      amt = format(item['amount'], '.2f')
      items += f'{desc[0:23] : <23}' + f'{amt[0:7] : >7}' + '\n'
    # total balance for the category
    bal = 'Total: ' + format(self.balance, '.2f')
    return title + items + bal


def create_spend_chart(categories):
  # graph title
  title = 'Percentage spent by category\n'
  spendingPercentages = []
  spendingTotal = 0
  
  # get total spending for all categories
  for cat in categories:
    spendingTotal += cat.withdrawals
  
    # get percentages by category. round down to 10s.
  # i = 0
  for cat in categories:
    spendingPercentages.append(round(cat.withdrawals / spendingTotal * 100 - 5, -1))
    # print('cat:', cat.name, '\t| perc:', spendingPercentages[i])
    # i += 1
  
  # create body of graph
  graphBodyStr = ''
  
  # y-axis and ticks (percentage markers) and data bars
  for i in range(10,-1,-1):
    perc = i*10
    tempStr = f"{str(perc)+'|':>4}" + ' '
    catIndex = 0
    # add 'bars' for each category equaling or greater than the percentage
    for cat in categories:
      tempStr += 'o  ' if spendingPercentages[catIndex] >= perc else '   '
      catIndex += 1
    tempStr += '\n' 
    graphBodyStr += tempStr
  
  # x-axis and ticks (categories)
  xAxis = ' '*4 + '-' + '---'*len(categories) + '\n'
  catTickMarks = ''
  longestCatNameLength = max(len(cat.name) for cat in categories)
  for i in range(longestCatNameLength):
    tempStr = '     '
    for cat in categories:
      # tempStr += ' ' if i < len(cat.name) else cat.name[i]
      # is there a better way to do this other than try-except?
      try:
        tempStr += cat.name[i]
      except:
        tempStr += ' '
      tempStr += '  '
    tempStr += '\n' if i < longestCatNameLength-1 else ''
    catTickMarks += tempStr
    
  graphStr = title + graphBodyStr + xAxis + catTickMarks
  return graphStr