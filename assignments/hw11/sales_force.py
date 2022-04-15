"""
Stores the definition for the SalesForce class.
"""
from hw11.sales_person import SalesPerson


class SalesForce:
    """Defines the SalesForce class, containing a list of SalesPerson objects."""
    def __init__(self):
        """Initializes sales_people as an empty list."""
        self.sales_people = []

    def add_data(self, file_name):
        """Imports SalesPerson objects from a specified file to the SalesForce class."""
        file = open(file_name, "r")
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip("\n")
        for i in lines:
            personal_data = i.split(", ")
            my_sales_person = SalesPerson(personal_data[0], personal_data[1])
            personal_sales = personal_data[2].split(" ")
            for count in range(len(personal_sales)):
                personal_sales[count] = float(personal_sales[count])
            for sale in personal_sales:
                my_sales_person.enter_sale(sale)
            self.sales_people.append(my_sales_person)
        file.close()

    def print_all(self):
        """Prints all stored SalesPerson objects on separate lines."""
        for i in self.sales_people:
            print(i)

    def quota_report(self, quota):
        """Returns each stored SalesPerson object as a list and whether each has met a set quota."""
        total_lst = []
        for sales_person in self.sales_people:
            individual_lst = [sales_person.get_id(),
                              sales_person.get_name(),
                              sales_person.total_sales()]
            if individual_lst[2] >= quota:
                individual_lst.append(True)
            else:
                individual_lst.append(False)
            total_lst.append(individual_lst)
        return total_lst

    def top_seller(self):
        """Returns the SalesPerson objects of the top sellers. (max 2)"""
        top_sale = 0
        for sales_person in self.sales_people:
            for sale in sales_person.get_sales():
                if sale > top_sale:
                    top_sale = sale
        lst_sellers = []
        for sales_person in self.sales_people:
            for sale in sales_person.get_sales():
                if sale == top_sale:
                    lst_sellers.append(sales_person)
        return lst_sellers

    def individual_sales(self, employee_id):
        """Returns an individual SalesPerson object specified by employee id."""
        for sales_person in self.sales_people:
            if sales_person.get_id() == employee_id:
                return sales_person
        return None

    def get_sale_frequencies(self):
        """Returns the frequency of certain sales amounts in dictionary format."""
        my_dict = {}
        for sales_person in self.sales_people:
            for sale in sales_person.get_sales():
                my_dict.update({sale: 0})
        for sales_person in self.sales_people:
            for sale in sales_person.get_sales():
                var = my_dict.get(sale) + 1
                my_dict.update({sale: var})
        return my_dict
