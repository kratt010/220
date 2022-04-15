"""
Stores the definition for the SalesPerson class.
"""
class SalesPerson:
    """Object that stores an integer employee id, a string name, and a numerical list of sales."""
    def __init__(self, employee_id, name):
        """Initializes employee id and name as input. Initializes sales as an empty list."""
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def __str__(self):
        """Returns a formatted string of the SalesPerson object's data."""
        return str(self.employee_id) + "-" + self.name + ":" + str(sum(self.sales))

    def get_id(self):
        """Returns employee id stored in the SalesPerson object."""
        return self.employee_id

    def get_name(self):
        """Returns name stored in the SalesPerson object."""
        return self.name

    def set_name(self, name):
        """Redefines name in SalesPerson object to input."""
        self.name = name

    def enter_sale(self, sale):
        """Redefines name in SalesPerson object to input."""
        self.sales.append(sale)

    def total_sales(self):
        """Returns the sum of sales in the SalesPerson object."""
        return sum(self.sales)

    def get_sales(self):
        """Returns the list of sales in the SalesPerson object."""
        return self.sales

    def met_quota(self, quota):
        """Returns True if total sales exceeds the specified quota, else returns False."""
        if sum(self.sales) >= quota:
            return True
        return False

    def compare_to(self, other):
        """Compares sales of a specified SalesPerson object to another."""
        my_sales = sum(self.sales)
        other_sales = sum(other.get_sales())
        if my_sales > other_sales:
            return 1
        if my_sales < other_sales :
            return -1
        return 0
