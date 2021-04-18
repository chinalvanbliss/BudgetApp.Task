# BUDGET APP TASK
# This task will be decomposed into five steps/stages for better handling as follows:

# STEP ONE
# Create a Budget class that can instantiate objects based on different budget categories like: Food,
# Clothing and Entertainment.
class Budget:

    def __init__(self, category):
        self.category = category
        self.balance = 0

    # STEP TWO
    # These objects (Food, Clothing, and Entertainment) should allow for: 1. Depositing funds to each of the categories.

    def deposit(self, amount):
        self.balance = amount
        return f"Your current balance is NGN {self.balance} in {self.category} budget"

    # STEP THREE These objects (Food, Clothing, and Entertainment) should allow for: 2. Withdrawing funds from each
    # of the categories.

    def withdraw(self, amount):

        if self.balance < amount:
            return "Insufficient Fund"

        else:
            self.balance = self.balance - amount
            feedback = f"Your current balance is NGN {self.balance} in {self.category} budget"
            return feedback

    # STEP FOUR
    # These objects (Food, Clothing, and Entertainment) should allow for: 3. Computing category balances.

    def get_balance(self):
        feedback = f"The balance for {self.category} is NGN {self.balance} budget"
        return feedback

    # STEP FIVE These objects (Food, Clothing, and Entertainment) should allow for: 5. Transferring balance amounts
    # between categories.

    def transfer(self, amount, category_name):
        if self.category == category_name.category:
            feedback = "You cannot transfer within the same budget category"
            feedback += "\nYou can only transfer amongst budget categories: Food, Clothing and Entertainment"
            return feedback

        if self.balance < amount:
            return "Insufficient Fund"

        else:
            self.balance -= amount
            category_name.balance += amount

            feedback = "Successful Transaction \n"
            feedback += f"The balance for {self.category} is NGN {self.balance} \n"
            feedback += f"The balance for {category_name.category} is NGN {category_name.balance}"
            return feedback


# Instantiation of objects (Food, Clothing, and Entertainment).
food = Budget("Food")
clothing = Budget("Clothing")
entertainment = Budget("Entertainment")

print("*************** Categories ************** \n")
print(food.category)
print(clothing.category)
print(entertainment.category)
print("==========================================\n")

print("***************** Deposit ******************")
print(food.deposit(50000))
print(clothing.deposit(20000))
print(entertainment.deposit(20000))
print("==========================================\n")

print("***************** Withdraw *****************")
print(food.withdraw(30000))
print(clothing.withdraw(10000))
print(entertainment.withdraw(12000))
print("==========================================\n")

print("***************** Balance ******************")
print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())
print("==========================================\n")

print("**************** Transfer *****************")
print(food.transfer(7000, clothing))
print(clothing.transfer(9000, entertainment))
print(entertainment.transfer(11000, food))
print("==========================================\n")
