"""
{
	expenseid: "1"
	itemId: "Item1"
	expensetype: "Food"
	amountInUsd : "250"
	sellerType : "restaurant"
	SellerName "ABC restaurant"

}

- Total expense should not be > 175
- Seller type restaurant should not have expense more that 45
- Entertainment expense type should not be charged

evaluateRule(List<rule> , List<expense>)
"""
from abc import ABC, abstractmethod
from typing import List

class Expense:
    
    def __init__(self, expense_id: str, item_id: str, expense_type: str, amount_in_usd: float, seller_type: str, seller_name: str):
        self.expenseid = expense_id
        self.itemId = item_id
        self.expenseType = expense_type
        self.amountInUsd = amount_in_usd
        self.sellerType = seller_type
        self.SellerName = seller_name

class Rule(ABC):
    @abstractmethod
    def evaluate(self, expenses: List[Expense]) -> bool:
        pass
    

class MaxTotalExpenseRule(Rule):
    def __init__(self, max_total):
        self.max_total = max_total

    def evaluate(self, expenses: List[Expense]) -> bool:
        total = sum(e.amountInUsd for e in expenses)
        return total <= self.max_total
    
    
class MaxSellerTypeExpenseRule(Rule):
    def __init__(self, seller_type, max_amount):
        self.sellerType = seller_type
        self.max_amount = max_amount
        
    def evaluate(self, expenses):
        total = sum(e.amountInUsd for e in expenses if e.sellerType.lower() == self.sellerType.lower())
        return total <= self.max_amount
    

class DisallowExpenseTypeRule(Rule):
    def __init__(self, expense_type):
        self.disallowedType = expense_type
        
    def evaluate(self, expenses):
        return all(e.expenseType.lower() != self.disallowedType.lower() for e in expenses)
    
def evaluateRule(rules, expenses):
    return all(rule.evaluate(expenses) for rule in rules)

expenses = [
    Expense("1", "Item1", "Food", 250, "restaurant", "ABC restaurant"),
    Expense("2", "Item2", "Entertainment", 20, "bar", "XYZ bar")
]

# Create rules
rules = [
    MaxTotalExpenseRule(175),
    MaxSellerTypeExpenseRule("restaurant", 45),
    DisallowExpenseTypeRule("Entertainment")
]

# Evaluate
result = evaluateRule(rules, expenses)
print("Passes all rules?", result)  # ➜ False