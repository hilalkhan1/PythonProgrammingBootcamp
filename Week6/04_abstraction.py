"""
Week 6: Abstraction Examples
Topics: Abstract Base Classes (ABC)
"""

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def refund_payment(self, amount):
        """Must be implemented by subclasses"""
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
    
    def refund_payment(self, amount):
        return f"Refunding ${amount} to Credit Card"


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"
    
    def refund_payment(self, amount):
        return f"Refunding ${amount} to PayPal"


print("=== Abstraction ===")
cc = CreditCardProcessor()
paypal = PayPalProcessor()

print(cc.process_payment(100))
print(paypal.process_payment(50))
