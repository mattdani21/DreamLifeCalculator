import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from utils import calculate_monthly_income, calculate_annual_income

def calculate_mortgage_payment(P, r, n):
    """
    Calculate the monthly mortgage payment.
    P: loan amount
    r: monthly interest rate (annual rate / 12)
    n: total number of months
    """
    return P * (r * (1 + r)**n) / ((1 + r)**n - 1)

def usa_page():
    st.title("Lifestyle Cost Calculator - USA")
    st.subheader("Determine the income needed for your dream life in the USA")
    
    # Input sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Housing Costs")
        house_cost = st.number_input("Cost of desired house ($)", min_value=0, value=500000, step=10000)
        down_payment_percent = st.slider("Down payment percentage", 0, 100, 20)
        mortgage_years = st.slider("Mortgage term (years)", 5, 30, 30)
        mortgage_rate = st.slider("Mortgage interest rate (%)", 0.0, 10.0, 3.5, 0.1)
        property_tax_rate = st.slider("Annual property tax rate (%)", 0.0, 5.0, 1.2, 0.1)
        house_maintenance = st.number_input("Monthly house maintenance costs ($)", min_value=0, value=300, step=50)
        homeowners_insurance = st.number_input("Monthly homeowners insurance ($)", min_value=0, value=150, step=50)

        st.subheader("Vehicle Expenses")
        vehicle_cost = st.number_input("Total vehicle costs ($)", min_value=0, value=35000, step=5000)
        vehicle_loan_years = st.slider("Vehicle loan term (years)", 1, 7, 5)
        vehicle_loan_rate = st.slider("Vehicle loan interest rate (%)", 0.0, 10.0, 4.5, 0.1)
        vehicle_insurance = st.number_input("Monthly vehicle insurance ($)", min_value=0, value=150, step=50)
        vehicle_maintenance = st.number_input("Monthly vehicle maintenance ($)", min_value=0, value=100, step=50)
        fuel_costs = st.number_input("Monthly fuel costs ($)", min_value=0, value=200, step=50)

    with col2:
        st.subheader("Daily Expenses")
        daily_food = st.number_input("Daily food expenses ($)", min_value=0, value=40, step=5)
        daily_transport = st.number_input("Daily transport expenses ($)", min_value=0, value=10, step=5)
        entertainment = st.number_input("Monthly entertainment expenses ($)", min_value=0, value=300, step=50)
        personal_care = st.number_input("Monthly personal care expenses ($)", min_value=0, value=150, step=50)
        
        st.subheader("Financial Goals")
        savings_goal = st.number_input("Monthly savings goal ($)", min_value=0, value=500, step=100)
        investment_goal = st.number_input("Monthly investment goal ($)", min_value=0, value=500, step=100)
        retirement_savings = st.number_input("Monthly retirement savings ($)", min_value=0, value=500, step=100)
        
        st.subheader("Other Expenses")
        utilities = st.number_input("Monthly utilities ($)", min_value=0, value=250, step=50)
        health_insurance = st.number_input("Monthly health insurance ($)", min_value=0, value=400, step=50)
        life_insurance = st.number_input("Monthly life insurance ($)", min_value=0, value=100, step=50)
        travel_budget = st.number_input("Monthly travel budget ($)", min_value=0, value=300, step=100)
        misc_expenses = st.number_input("Miscellaneous monthly expenses ($)", min_value=0, value=300, step=50)

        st.subheader("Income Tax")
        tax_rate = st.slider("Estimated income tax rate (%)", 0, 50, 25)

    # Calculations
    loan_amount = house_cost * (1 - down_payment_percent / 100)
    monthly_mortgage = calculate_mortgage_payment(loan_amount, mortgage_rate / 100 / 12, mortgage_years * 12)
    monthly_property_tax = house_cost * (property_tax_rate / 100) / 12

    vehicle_loan_amount = vehicle_cost
    monthly_vehicle_payment = calculate_mortgage_payment(vehicle_loan_amount, vehicle_loan_rate / 100 / 12, vehicle_loan_years * 12)

    monthly_expenses = {
        "Mortgage": monthly_mortgage,
        "Property Tax": monthly_property_tax,
        "House Maintenance": house_maintenance,
        "Homeowners Insurance": homeowners_insurance,
        "Vehicle Payment": monthly_vehicle_payment,
        "Vehicle Insurance": vehicle_insurance,
        "Vehicle Maintenance": vehicle_maintenance,
        "Fuel": fuel_costs,
        "Food": daily_food * 30,
        "Transport": daily_transport * 30,
        "Entertainment": entertainment,
        "Personal Care": personal_care,
        "Utilities": utilities,
        "Health Insurance": health_insurance,
        "Life Insurance": life_insurance,
        "Travel": travel_budget,
        "Miscellaneous": misc_expenses,
        "Savings": savings_goal,
        "Investments": investment_goal,
        "Retirement Savings": retirement_savings
    }

    total_monthly_expenses = sum(monthly_expenses.values())
    required_monthly_income = calculate_monthly_income(total_monthly_expenses, tax_rate)
    required_annual_income = calculate_annual_income(required_monthly_income)

    # Results display
    st.header("Results")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Required Income")
        st.metric("Monthly Income Needed", f"${required_monthly_income:,.2f}")
        st.metric("Annual Income Needed", f"${required_annual_income:,.2f}")

        st.subheader("Expense Breakdown")
        expenses_df = pd.DataFrame(list(monthly_expenses.items()), columns=["Category", "Amount"])
        fig = px.pie(expenses_df, values="Amount", names="Category", title="Monthly Expenses")
        st.plotly_chart(fig)

    with col4:
        st.subheader("Monthly Expenses Summary")
        col_left, col_right = st.columns(2)
        expenses_items = list(monthly_expenses.items())
        mid_point = len(expenses_items) // 2

        with col_left:
            for category, amount in expenses_items[:mid_point]:
                st.metric(category, f"${amount:,.2f}")

        with col_right:
            for category, amount in expenses_items[mid_point:]:
                st.metric(category, f"${amount:,.2f}")

        st.subheader("Total Monthly Expenses")
        st.metric("Total", f"${total_monthly_expenses:,.2f}")

    st.info("Adjust the inputs to see real-time updates in the required income and expense breakdown.")

def netherlands_page():
    st.title("Lifestyle Cost Calculator - Netherlands")
    st.subheader("Determine the income needed for your dream life in the Netherlands")
    
    # Input sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Housing Costs")
        house_cost = st.number_input("Cost of desired house (€)", min_value=0, value=400000, step=10000)
        down_payment_percent = st.slider("Down payment percentage", 0, 100, 10)
        mortgage_years = st.slider("Mortgage term (years)", 5, 30, 30)
        mortgage_rate = st.slider("Mortgage interest rate (%)", 0.0, 5.0, 2.0, 0.1)
        property_tax_rate = st.slider("Annual property tax rate (%)", 0.0, 1.0, 0.1, 0.01)
        house_maintenance = st.number_input("Monthly house maintenance costs (€)", min_value=0, value=200, step=50)
        homeowners_insurance = st.number_input("Monthly homeowners insurance (€)", min_value=0, value=50, step=10)

        st.subheader("Vehicle Expenses")
        vehicle_cost = st.number_input("Total vehicle costs (€)", min_value=0, value=25000, step=5000)
        vehicle_loan_years = st.slider("Vehicle loan term (years)", 1, 7, 5)
        vehicle_loan_rate = st.slider("Vehicle loan interest rate (%)", 0.0, 10.0, 3.5, 0.1)
        vehicle_insurance = st.number_input("Monthly vehicle insurance (€)", min_value=0, value=100, step=25)
        vehicle_maintenance = st.number_input("Monthly vehicle maintenance (€)", min_value=0, value=75, step=25)
        fuel_costs = st.number_input("Monthly fuel costs (€)", min_value=0, value=150, step=25)

    with col2:
        st.subheader("Daily Expenses")
        daily_food = st.number_input("Daily food expenses (€)", min_value=0, value=20, step=5)
        daily_transport = st.number_input("Daily transport expenses (€)", min_value=0, value=5, step=1)
        entertainment = st.number_input("Monthly entertainment expenses (€)", min_value=0, value=200, step=50)
        personal_care = st.number_input("Monthly personal care expenses (€)", min_value=0, value=100, step=25)
        
        st.subheader("Financial Goals")
        savings_goal = st.number_input("Monthly savings goal (€)", min_value=0, value=500, step=100)
        investment_goal = st.number_input("Monthly investment goal (€)", min_value=0, value=300, step=100)
        retirement_savings = st.number_input("Monthly retirement savings (€)", min_value=0, value=300, step=100)
        
        st.subheader("Other Expenses")
        utilities = st.number_input("Monthly utilities (€)", min_value=0, value=200, step=50)
        health_insurance = st.number_input("Monthly health insurance (€)", min_value=0, value=120, step=10)
        life_insurance = st.number_input("Monthly life insurance (€)", min_value=0, value=50, step=10)
        travel_budget = st.number_input("Monthly travel budget (€)", min_value=0, value=200, step=50)
        misc_expenses = st.number_input("Miscellaneous monthly expenses (€)", min_value=0, value=200, step=50)

        st.subheader("Income Tax")
        tax_rate = st.slider("Estimated income tax rate (%)", 0, 60, 40)

    # Calculations
    loan_amount = house_cost * (1 - down_payment_percent / 100)
    monthly_mortgage = calculate_mortgage_payment(loan_amount, mortgage_rate / 100 / 12, mortgage_years * 12)
    monthly_property_tax = house_cost * (property_tax_rate / 100) / 12

    vehicle_loan_amount = vehicle_cost
    monthly_vehicle_payment = calculate_mortgage_payment(vehicle_loan_amount, vehicle_loan_rate / 100 / 12, vehicle_loan_years * 12)

    monthly_expenses = {
        "Mortgage": monthly_mortgage,
        "Property Tax": monthly_property_tax,
        "House Maintenance": house_maintenance,
        "Homeowners Insurance": homeowners_insurance,
        "Vehicle Payment": monthly_vehicle_payment,
        "Vehicle Insurance": vehicle_insurance,
        "Vehicle Maintenance": vehicle_maintenance,
        "Fuel": fuel_costs,
        "Food": daily_food * 30,
        "Transport": daily_transport * 30,
        "Entertainment": entertainment,
        "Personal Care": personal_care,
        "Utilities": utilities,
        "Health Insurance": health_insurance,
        "Life Insurance": life_insurance,
        "Travel": travel_budget,
        "Miscellaneous": misc_expenses,
        "Savings": savings_goal,
        "Investments": investment_goal,
        "Retirement Savings": retirement_savings
    }

    total_monthly_expenses = sum(monthly_expenses.values())
    required_monthly_income = calculate_monthly_income(total_monthly_expenses, tax_rate)
    required_annual_income = calculate_annual_income(required_monthly_income)

    # Results display
    st.header("Results")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Required Income")
        st.metric("Monthly Income Needed", f"€{required_monthly_income:,.2f}")
        st.metric("Annual Income Needed", f"€{required_annual_income:,.2f}")

        st.subheader("Expense Breakdown")
        expenses_df = pd.DataFrame(list(monthly_expenses.items()), columns=["Category", "Amount"])
        fig = px.pie(expenses_df, values="Amount", names="Category", title="Monthly Expenses")
        st.plotly_chart(fig)

    with col4:
        st.subheader("Monthly Expenses Summary")
        col_left, col_right = st.columns(2)
        expenses_items = list(monthly_expenses.items())
        mid_point = len(expenses_items) // 2

        with col_left:
            for category, amount in expenses_items[:mid_point]:
                st.metric(category, f"€{amount:,.2f}")

        with col_right:
            for category, amount in expenses_items[mid_point:]:
                st.metric(category, f"€{amount:,.2f}")

        st.subheader("Total Monthly Expenses")
        st.metric("Total", f"€{total_monthly_expenses:,.2f}")

    st.info("Adjust the inputs to see real-time updates in the required income and expense breakdown.")

def south_africa_page():
    st.title("Lifestyle Cost Calculator - South Africa")
    st.subheader("Determine the income needed for your dream life in South Africa")
    
    # Input sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Housing Costs")
        house_cost = st.number_input("Cost of desired house (R)", min_value=0, value=2000000, step=100000)
        down_payment_percent = st.slider("Down payment percentage", 0, 100, 10)
        mortgage_years = st.slider("Mortgage term (years)", 5, 30, 20)
        mortgage_rate = st.slider("Mortgage interest rate (%)", 0.0, 15.0, 7.0, 0.1)
        property_tax_rate = st.slider("Annual property tax rate (%)", 0.0, 3.0, 1.5, 0.1)
        house_maintenance = st.number_input("Monthly house maintenance costs (R)", min_value=0, value=3000, step=500)
        homeowners_insurance = st.number_input("Monthly homeowners insurance (R)", min_value=0, value=1000, step=100)

        st.subheader("Vehicle Expenses")
        vehicle_cost = st.number_input("Total vehicle costs (R)", min_value=0, value=300000, step=50000)
        vehicle_loan_years = st.slider("Vehicle loan term (years)", 1, 7, 5)
        vehicle_loan_rate = st.slider("Vehicle loan interest rate (%)", 0.0, 15.0, 9.0, 0.1)
        vehicle_insurance = st.number_input("Monthly vehicle insurance (R)", min_value=0, value=1500, step=100)
        vehicle_maintenance = st.number_input("Monthly vehicle maintenance (R)", min_value=0, value=1000, step=100)
        fuel_costs = st.number_input("Monthly fuel costs (R)", min_value=0, value=2000, step=100)

    with col2:
        st.subheader("Daily Expenses")
        daily_food = st.number_input("Daily food expenses (R)", min_value=0, value=200, step=10)
        daily_transport = st.number_input("Daily transport expenses (R)", min_value=0, value=50, step=10)
        entertainment = st.number_input("Monthly entertainment expenses (R)", min_value=0, value=2000, step=100)
        personal_care = st.number_input("Monthly personal care expenses (R)", min_value=0, value=1000, step=100)
        
        st.subheader("Financial Goals")
        savings_goal = st.number_input("Monthly savings goal (R)", min_value=0, value=3000, step=500)
        investment_goal = st.number_input("Monthly investment goal (R)", min_value=0, value=2000, step=500)
        retirement_savings = st.number_input("Monthly retirement savings (R)", min_value=0, value=2000, step=500)
        
        st.subheader("Other Expenses")
        utilities = st.number_input("Monthly utilities (R)", min_value=0, value=2000, step=100)
        health_insurance = st.number_input("Monthly health insurance (R)", min_value=0, value=1500, step=100)
        life_insurance = st.number_input("Monthly life insurance (R)", min_value=0, value=500, step=100)
        travel_budget = st.number_input("Monthly travel budget (R)", min_value=0, value=2000, step=500)
        misc_expenses = st.number_input("Miscellaneous monthly expenses (R)", min_value=0, value=1500, step=100)
        
        st.subheader("South Africa Specific Expenses")
        private_security = st.number_input("Monthly private security costs (R)", min_value=0, value=1500, step=100)

        st.subheader("Income Tax")
        tax_rate = st.slider("Estimated income tax rate (%)", 0, 45, 30)

    # Calculations
    loan_amount = house_cost * (1 - down_payment_percent / 100)
    monthly_mortgage = calculate_mortgage_payment(loan_amount, mortgage_rate / 100 / 12, mortgage_years * 12)
    monthly_property_tax = house_cost * (property_tax_rate / 100) / 12

    vehicle_loan_amount = vehicle_cost
    monthly_vehicle_payment = calculate_mortgage_payment(vehicle_loan_amount, vehicle_loan_rate / 100 / 12, vehicle_loan_years * 12)

    monthly_expenses = {
        "Mortgage": monthly_mortgage,
        "Property Tax": monthly_property_tax,
        "House Maintenance": house_maintenance,
        "Homeowners Insurance": homeowners_insurance,
        "Vehicle Payment": monthly_vehicle_payment,
        "Vehicle Insurance": vehicle_insurance,
        "Vehicle Maintenance": vehicle_maintenance,
        "Fuel": fuel_costs,
        "Food": daily_food * 30,
        "Transport": daily_transport * 30,
        "Entertainment": entertainment,
        "Personal Care": personal_care,
        "Utilities": utilities,
        "Health Insurance": health_insurance,
        "Life Insurance": life_insurance,
        "Travel": travel_budget,
        "Miscellaneous": misc_expenses,
        "Private Security": private_security,
        "Savings": savings_goal,
        "Investments": investment_goal,
        "Retirement Savings": retirement_savings
    }

    total_monthly_expenses = sum(monthly_expenses.values())
    required_monthly_income = calculate_monthly_income(total_monthly_expenses, tax_rate)
    required_annual_income = calculate_annual_income(required_monthly_income)

    # Results display
    st.header("Results")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Required Income")
        st.metric("Monthly Income Needed", f"R{required_monthly_income:,.2f}")
        st.metric("Annual Income Needed", f"R{required_annual_income:,.2f}")

        st.subheader("Expense Breakdown")
        expenses_df = pd.DataFrame(list(monthly_expenses.items()), columns=["Category", "Amount"])
        fig = px.pie(expenses_df, values="Amount", names="Category", title="Monthly Expenses")
        st.plotly_chart(fig)

    with col4:
        st.subheader("Monthly Expenses Summary")
        col_left, col_right = st.columns(2)
        expenses_items = list(monthly_expenses.items())
        mid_point = len(expenses_items) // 2

        with col_left:
            for category, amount in expenses_items[:mid_point]:
                st.metric(category, f"R{amount:,.2f}")

        with col_right:
            for category, amount in expenses_items[mid_point:]:
                st.metric(category, f"R{amount:,.2f}")

        st.subheader("Total Monthly Expenses")
        st.metric("Total", f"R{total_monthly_expenses:,.2f}")

    st.info("Adjust the inputs to see real-time updates in the required income and expense breakdown.")

def south_korea_page():
    st.title("Lifestyle Cost Calculator - South Korea")
    st.subheader("Determine the income needed for your dream life in South Korea")
    
    # Input sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Housing Costs")
        house_cost = st.number_input("Cost of desired house (₩)", min_value=0, value=500000000, step=10000000)
        down_payment_percent = st.slider("Down payment percentage", 0, 100, 20)
        mortgage_years = st.slider("Mortgage term (years)", 5, 30, 20)
        mortgage_rate = st.slider("Mortgage interest rate (%)", 0.0, 10.0, 3.0, 0.1)
        property_tax_rate = st.slider("Annual property tax rate (%)", 0.0, 1.0, 0.3, 0.01)
        house_maintenance = st.number_input("Monthly house maintenance costs (₩)", min_value=0, value=300000, step=50000)
        homeowners_insurance = st.number_input("Monthly homeowners insurance (₩)", min_value=0, value=50000, step=10000)

        st.subheader("Vehicle Expenses")
        vehicle_cost = st.number_input("Total vehicle costs (₩)", min_value=0, value=30000000, step=1000000)
        vehicle_loan_years = st.slider("Vehicle loan term (years)", 1, 7, 5)
        vehicle_loan_rate = st.slider("Vehicle loan interest rate (%)", 0.0, 10.0, 4.0, 0.1)
        vehicle_insurance = st.number_input("Monthly vehicle insurance (₩)", min_value=0, value=100000, step=10000)
        vehicle_maintenance = st.number_input("Monthly vehicle maintenance (₩)", min_value=0, value=100000, step=10000)
        fuel_costs = st.number_input("Monthly fuel costs (₩)", min_value=0, value=200000, step=50000)

    with col2:
        st.subheader("Daily Expenses")
        daily_food = st.number_input("Daily food expenses (₩)", min_value=0, value=20000, step=1000)
        daily_transport = st.number_input("Daily transport expenses (₩)", min_value=0, value=3000, step=500)
        entertainment = st.number_input("Monthly entertainment expenses (₩)", min_value=0, value=300000, step=50000)
        personal_care = st.number_input("Monthly personal care expenses (₩)", min_value=0, value=100000, step=10000)
        
        st.subheader("Financial Goals")
        savings_goal = st.number_input("Monthly savings goal (₩)", min_value=0, value=500000, step=100000)
        investment_goal = st.number_input("Monthly investment goal (₩)", min_value=0, value=300000, step=50000)
        retirement_savings = st.number_input("Monthly retirement savings (₩)", min_value=0, value=300000, step=50000)
        
        st.subheader("Other Expenses")
        utilities = st.number_input("Monthly utilities (₩)", min_value=0, value=200000, step=10000)
        health_insurance = st.number_input("Monthly health insurance (₩)", min_value=0, value=100000, step=10000)
        life_insurance = st.number_input("Monthly life insurance (₩)", min_value=0, value=50000, step=10000)
        travel_budget = st.number_input("Monthly travel budget (₩)", min_value=0, value=300000, step=50000)
        misc_expenses = st.number_input("Miscellaneous monthly expenses (₩)", min_value=0, value=200000, step=50000)
        
        st.subheader("South Korea Specific Expenses")
        public_transportation = st.number_input("Monthly public transportation costs (₩)", min_value=0, value=100000, step=10000)

        st.subheader("Income Tax")
        tax_rate = st.slider("Estimated income tax rate (%)", 0, 50, 25)

    # Calculations
    loan_amount = house_cost * (1 - down_payment_percent / 100)
    monthly_mortgage = calculate_mortgage_payment(loan_amount, mortgage_rate / 100 / 12, mortgage_years * 12)
    monthly_property_tax = house_cost * (property_tax_rate / 100) / 12

    vehicle_loan_amount = vehicle_cost
    monthly_vehicle_payment = calculate_mortgage_payment(vehicle_loan_amount, vehicle_loan_rate / 100 / 12, vehicle_loan_years * 12)

    monthly_expenses = {
        "Mortgage": monthly_mortgage,
        "Property Tax": monthly_property_tax,
        "House Maintenance": house_maintenance,
        "Homeowners Insurance": homeowners_insurance,
        "Vehicle Payment": monthly_vehicle_payment,
        "Vehicle Insurance": vehicle_insurance,
        "Vehicle Maintenance": vehicle_maintenance,
        "Fuel": fuel_costs,
        "Food": daily_food * 30,
        "Transport": daily_transport * 30,
        "Entertainment": entertainment,
        "Personal Care": personal_care,
        "Utilities": utilities,
        "Health Insurance": health_insurance,
        "Life Insurance": life_insurance,
        "Travel": travel_budget,
        "Miscellaneous": misc_expenses,
        "Public Transportation": public_transportation,
        "Savings": savings_goal,
        "Investments": investment_goal,
        "Retirement Savings": retirement_savings
    }

    total_monthly_expenses = sum(monthly_expenses.values())
    required_monthly_income = calculate_monthly_income(total_monthly_expenses, tax_rate)
    required_annual_income = calculate_annual_income(required_monthly_income)

    # Results display
    st.header("Results")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Required Income")
        st.metric("Monthly Income Needed", f"₩{required_monthly_income:,.0f}")
        st.metric("Annual Income Needed", f"₩{required_annual_income:,.0f}")

        st.subheader("Expense Breakdown")
        expenses_df = pd.DataFrame(list(monthly_expenses.items()), columns=["Category", "Amount"])
        fig = px.pie(expenses_df, values="Amount", names="Category", title="Monthly Expenses")
        st.plotly_chart(fig)

    with col4:
        st.subheader("Monthly Expenses Summary")
        col_left, col_right = st.columns(2)
        expenses_items = list(monthly_expenses.items())
        mid_point = len(expenses_items) // 2

        with col_left:
            for category, amount in expenses_items[:mid_point]:
                st.metric(category, f"₩{amount:,.0f}")

        with col_right:
            for category, amount in expenses_items[mid_point:]:
                st.metric(category, f"₩{amount:,.0f}")

        st.subheader("Total Monthly Expenses")
        st.metric("Total", f"₩{total_monthly_expenses:,.0f}")

    st.info("Adjust the inputs to see real-time updates in the required income and expense breakdown.")

def main():
    st.set_page_config(page_title="Lifestyle Cost Calculator", page_icon="💰", layout="wide")

    selected_country = option_menu(
        menu_title=None,
        options=["USA", "Netherlands", "South Africa", "South Korea"],
        icons=["flag-fill", "flag-fill", "flag-fill", "flag-fill"],
        default_index=0,
        orientation="horizontal",
    )

    if selected_country == "USA":
        usa_page()
    elif selected_country == "Netherlands":
        netherlands_page()
    elif selected_country == "South Africa":
        south_africa_page()
    elif selected_country == "South Korea":
        south_korea_page()

if __name__ == "__main__":
    main()
