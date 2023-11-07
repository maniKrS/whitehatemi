import streamlit as st

def calculate_emi(p, n, r):
    emi = p * r/100 * (1 + r/100)**n / ((1 + r/100)**n - 1)
    return emi

def calculate_outstanding_balance(p, n, r, months_paid):
    emi = calculate_emi(p, n, r)
    remaining_balance = p * ((1 + r/100)**n - (1 + r/100)**months_paid) / ((1 + r/100)**n - 1)
    return remaining_balance

st.title('Loan Calculator')

principal = st.number_input('Principal loan amount')
loan_tenure_in_months = st.number_input('Loan tenure (in months)')
interest_rate = st.number_input('Interest rate (%)')
months_paid = st.number_input('Months paid')

if st.button('Calculate EMI'):
    emi_result = calculate_emi(principal, loan_tenure_in_months, interest_rate)
    st.write(f'Your EMI is: {emi_result:.2f}')

if st.button('Calculate Outstanding Balance'):
    outstanding_balance = calculate_outstanding_balance(principal, loan_tenure_in_months, interest_rate, months_paid)
    st.write(f'Your outstanding loan balance is: {outstanding_balance:.2f}')
