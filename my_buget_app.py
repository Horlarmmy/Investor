print("Welcome to the Budget app !!! \n\n")

class myBudget:
	def __init__(self, **budgets):
		self.budgets = budgets
		print(self.budgets)
	def deposit(self, budget, amount):
		self.budgets[budget] = self.budgets[budget] + amount
		print('You deposited $' + str(amount) + ' in ' + budget)
		
	def withdraw(self,budget,amount):
		print('Processing your withdrawal...')
		if amount > self.budgets[budget]:
		  print('Insufficient Balance \n Unable to withdraw')
		else:
			self.budgets[budget] = self.budgets[budget] - amount
			print('You withdrawal of $' + str(amount) +  ' from ' + budget + ' was successful' )
			
	def transfer(self,debit,credit,amount):
		print('Transfer ongoing...')
		if amount > self.budgets[debit]:
			print('Insufficient Balance \n Transfer failed !')
		else:
			self.budgets[debit] = self.budgets[debit] - amount
			self.budgets[credit] = self.budgets[credit] + amount
			print('Your transfer was successful!')
	def checkBalance(self,budget):
		print('Your ' + budget + ' balance is $' + str(self.budgets[budget]))
		
mybudget = myBudget(Food = 700, Clothing =1000, Rent = 2000, Entertainment = 200)

while True:
	print("\n What do you want...?\n 1. Deposit \n 2. Withdraw \n 3. Transfer \n 4. Check balance \n 5. Quit\n")
	opt = int(input('Enter an option...  '))
	if opt == 1:
		i = int(input('Enter deposit amount '))
		j = str(input('Enter category '))
		mybudget.deposit(str(j), i)
	elif opt == 2:
		k= int(input('Enter withdraw amount '))
		l= str(input('Enter category '))
		mybudget.withdraw(str(l), k)
	elif opt == 3:
		m= int(input('Enter amount '))
		n= str(input('Enter category to be debited '))
		o = str(input('Enter category to be credited '))
		mybudget.transfer(str(n),str(o), m)
	elif opt == 4:
		balance =str(input('What balance do you want to check '))
		mybudget.checkBalance(str(balance))
	elif opt == 5:
		break
	else:
		print('\nEnter a valid option')
