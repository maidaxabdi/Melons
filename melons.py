#Jacky, Molly, Maida

"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit"""

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "Christmas melons":
            base_price = 7.5
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
        
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""    
    def __init__(self, species, qty):
        #"""Initialize melon order attributes."""
       super().__init__(species, qty, "domestic", 0.08)
    

class InternationalMelonOrder(AbstractMelonOrder):
       # """An international (non-US) melon order."""
    
    
    def __init__(self, species, qty, country_code):
       # """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code
     
    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total = total + 3
            
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order within the USA for US Government."""    
    def __init__(self, species, qty):
        #"""Initialize melon order attributes."""
        super().__init__(species, qty, "government", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True

