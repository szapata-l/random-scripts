import json

class BudgetCalculator:

    def __init__(self):
        
        category = input("Paycheck, Deposit, or Withdrawl: ")
        
        self.savings_rate = .5
        self.investment_rate = .3
        self.spending_rate = .2
        
        with open('totalBudget.json') as budgetFile:
            budget = json.load(budgetFile)
        
        self.totalSavings = budget['Savings Total']
        self.totalSpending = budget['Spending Total']
        self.totalInvestings = budget['Investing Total']
        
        if category == "Paycheck":
            
            amount =int(input("Enter Amount: "))
            
            new_budget = self.calculateBudget(amount)
        
            self.totalSavings += new_budget[0]
            self.totalInvestings += new_budget[1]
            self.totalSpending += new_budget[2]
            
            budget['Savings Total'] = round(self.totalSavings,2)
            budget['Spending Total'] = round(self.totalSpending, 2)
            budget['Investing Total'] = round(self.totalInvestings,2)

            with open('totalBudget.json', 'w') as budgetFile1:
                json.dump(budget, budgetFile1)
        
            self.printTotals()
        
        elif category == "Deposit":
            
            cat2 = input("Category (savings, investments, or spending): ")
            amount = int(input("Enter Amount: "))
            
            self.deposit(cat2, amount)
            
            budget['Savings Total'] = round(self.totalSavings,2)
            budget['Spending Total'] = round(self.totalSpending, 2)
            budget['Investing Total'] = round(self.totalInvestings,2)

            with open('totalBudget.json', 'w') as budgetFile1:
                json.dump(budget, budgetFile1)
        
        elif category == "Withdrawl":
            cat3 = input("Category (savings, investments, or spending: ")
            amount = int(input("Enter Amount: "))
            
            self.withdrawl(cat3, amount)
            
            budget['Savings Total'] = round(self.totalSavings,2)
            budget['Spending Total'] = round(self.totalSpending, 2)
            budget['Investing Total'] = round(self.totalInvestings,2)

            with open('totalBudget.json', 'w') as budgetFile1:
                json.dump(budget, budgetFile1)
                
            
        else:
            print("INVALID INPUT: Input Paycheck, Deposit, or Withdrawl")
        
    def calculateBudget(self, paycheck):
        
        savings = paycheck * self.savings_rate
        investment = paycheck * self.investment_rate
        spending = paycheck * self.spending_rate

        return (savings, investment, spending)

    def withdrawl(self, category, amount):
        
        if category == "savings":
            print(f'Previous Total Savings Amount: {self.totalSavings}')
            self.totalSavings -= amount
            print(f'Total Savings Amount: {self.totalSavings}')
        
        elif category == "investments":
            print(f'Previous Total Investments Amount: {self.totalInvestings}')
            self.totalInvestings -= amount
            print(f'Total Investments Amount: {self.totalInvestings}')
        
        elif category == "spendings":
            print(f'Previous Total Spendings Amount: {self.totalSpending}')
            self.totalSpending -= amount
            print(f'Total Spending Amount: {self.totalSpending}')
        else:
            print("Incorrect category: input savings, investments, or spendings")
        
        
    def deposit(self, category, amount):

        if category == "savings":
            print(f'Previous Total Savings Amount: {self.totalSavings}')
            self.totalSavings += amount
            print(f'Total Savings Amount: {self.totalSavings}')
        
        elif category == "investments":
            print(f'Previous Total Investments Amount: {self.totalInvestings}')
            self.totalInvestings += amount
            print(f'Total Investments Amount: {self.totalInvestings}')
        
        elif category == "spendings":
            print(f'Previous Total Spendings Amount: {self.totalSpending}')
            self.totalSpending += amount
            print(f'Total Spending Amount: {self.totalSpending}')
           
        else:
            print("Incorrect category: input savings, investments, or spending")
        
    def printTotals(self):
        
        print("Savings Total: " + str(round(self.totalSavings,2)))
        print("Investing Total: " + str(round(self.totalInvestings,2)))
        print("Spending Total: " + str(round(self.totalSpending,2)))    

if __name__ =="__main__":

    BUDGET = BudgetCalculator()

    
