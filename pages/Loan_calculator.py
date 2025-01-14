import streamlit as st


class LoanCalculator:
  def __init__(self):
    st.html("<H1 style='text-align: center;'>LOAN CALCULATOR</H1>")
    st.markdown("---")
    col1,col2=st.columns(2)
   
    principal_amt=col1.text_input("Enter the Principal amount",placeholder="Enter the principal amount")
    Annual_interest=col2.number_input("Enter the annual interest",1,20)
    time_period=st.text_input("Enter the time period in years",placeholder="Enter the time period in years")
    calculate_button=st.button("Calculate the Loan", use_container_width=True)
    if calculate_button:
      self.calculate_loan(principal_amt,Annual_interest,time_period)
    st.markdown("---")

  def calculate_loan(self,principal_amt,Annual_interest,time_period):
    if not(principal_amt) or not(Annual_interest) or not(time_period):
      st.error("All fields are required")
      return
    
    principal_amt=float(principal_amt)
    Annual_interest=float(Annual_interest)
    time_period=float(time_period)

    months=time_period*12
    monthly_rate=(Annual_interest/100)/12

    if monthly_rate!=0:
      monthly_payment = (principal_amt * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    else:
      monthly_payment=principal_amt/months

    st.success(f"The monthly payment is: {monthly_payment}")
    


LC=LoanCalculator()
