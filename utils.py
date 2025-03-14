def calculate_monthly_income(total_expenses, tax_rate):
    """
    Calculate the required monthly income based on expenses and tax rate.
    """
    return total_expenses / (1 - tax_rate / 100)

def calculate_annual_income(monthly_income):
    """
    Calculate the annual income based on monthly income.
    """
    return monthly_income * 12
