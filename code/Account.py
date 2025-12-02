from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def permissions(self):
        pass

class ManagerAccount(Account):
    def permissions(self):
        return "Manage stock, purchases, orders, view incomes"

class SellerAccount(Account):
    def permissions(self):
        return "Sell products, make orders"

class VisitorAccount(Account):
    def permissions(self):
        return "View stock, make purchases"

class AccountFactory:
    @staticmethod
    def createAccount(type):
        type = type.lower()
        if type == "manager":
            return ManagerAccount()
        elif type == "seller":
            return SellerAccount()
        elif type == "visitor":
            return VisitorAccount()
        else:
            raise ValueError("Unknown account type")
