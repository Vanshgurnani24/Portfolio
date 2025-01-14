import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


#Setting up title and description
st.title("Vendor Management Portal")
st.markdown("Enter the Details of the new Vendor Below")


#Establishing Gsheets connection 
conn=st.connection("gsheets",type=GSheetsConnection)

#Fetch exisiting vendors data
existing_data=conn.read(worksheet="Vendors",usecols=list(range(6)),ttl=5)


#dropna is pandas operation which will remova rows containing NaN(Not a number) values. also the how="all" means that all rows with NaN values will be dropped.
#in short. This will remove any NaN values and make sure that no rows are empty in the google sheet
existing_data=existing_data.dropna(how='all')

#LIST OF BUSINESS TYPES AND PRODUCTS
BUSINESS_TYPES=["ManuFacturer",
                "Distributor",
                "Wholesaler",
                "Retailer",
                "Service Provider"
                ]

PRODUCTS=[
  "Electronics",
  "Apparel",
  "Groceries",
  "Software",
  "Other"
]


#Creating the new Vendor Form
with st.form(key='vendor_form'):
  company_name=st.text_input(label="Company Name",placeholder="Name of the company")
  business_type=st.selectbox(label="Business Type",options=BUSINESS_TYPES,index=None)
  products=st.multiselect(label="Products Offered",options=PRODUCTS)
  years_in_business=st.slider(label="Years in business",min_value=0,max_value=50,step=5)
  onboarding_date=st.date_input(label="Onboarding Date")
  additional_info=st.text_area(label="Additional Information")


  #mark mandatory fields
  st.markdown("**required*")

  submit_button=st.form_submit_button(label="Submit Vendor Details")
  if submit_button:
    
    #check if all mandatory fields are filled

    if not company_name and not business_type:
      st.warning("Ensure all mandatory fields are filled")
      st.stop()
    #also makesure no existing company is re-entered
    elif existing_data["CompanyName"].str.contains(company_name).any():
      st.warning("Company Name already exists in the system. Please enter a unique name.")
      st.stop()
    else:
      vendor_data=pd.DataFrame(
        [
          {
            "CompanyName":company_name,
            "BusinessType":business_type,
            "Products":", ".join(products), #convert the list into string and seperate multiple entried with comma
            "YearsInBusiness":years_in_business,
            "OnboardingDate":onboarding_date.strftime("%Y-%m-%d"), #format the date according to the spreadsheet
            "AdditionalInfo":additional_info
          }
        ]
      )
      # Add the new vendor data to the existing data
      updated_df=pd.concat([existing_data,vendor_data],ignore_index=True)

      # Update Google sheets with the new vendor Data
      conn.update(worksheet='Vendors',data=updated_df)

      st.success("Vendor Details Successfully Submitted")
    