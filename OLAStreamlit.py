# Traffic Streamlit USER Interface

#--------------------------------- Import Liabraries-------------------------------------------
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import mysql.connector
from tabulate import tabulate
import streamlit as st



#------------------------------- Adding Gradient Background--------------------------------

gradient_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(90deg, #f8ff00 0%, #3ad59f 100%);
    background-size: cover;
}
</style>
"""

st.markdown(gradient_css, unsafe_allow_html=True)

sidebar_gradient_css = """
<style>
[data-testid="stSidebar"] {
    background-image: linear-gradient(90deg, #f8ff00 0%, #3ad59f 100%);
    background-size: cover;
}
"""
st.markdown(sidebar_gradient_css, unsafe_allow_html=True)

#------------------------------------Connecting to Database----------------------------------

DB_PASSWORD = "MySQL@1234"

conn = mysql.connector.connect(host="localhost",user="root",password=DB_PASSWORD,database="Oladb")

# Function to connect to MySql database
def get_data(query, params=None):
    
    if params:
        df = pd.read_sql_query(query, conn, params=params)
    else:
        df = pd.read_sql_query(query, conn)
    conn.close()
    return df



#----------------------------------- Streamlit Layout-----------------------------------------

# Streamlit App Title
st.set_page_config(page_title="Ola Ride Insights", layout="wide")
st.image("D:/Shruti/Guvi/OLA Project/Data/Ola-banner.jpg")
st.sidebar.image("D:/Shruti/Guvi/OLA Project/Data/ola.png")
st.sidebar.title("Navigation : ")
page = st.sidebar.radio("Go To", ["Project Introduction", "Ratings", "Bookings","Ride Status",
                                   "Creator Information"])
st.header ("Ola Ride Insights")
col1,col2,col3 = st.columns(3,gap='small')
container = st.container

#----------------------------------- Project Introduction Page-----------------------------------------

if page == "Project Introduction":
    st.title("Project Introduction")
    
    st.subheader("📊 Welcome to the Ola Ride Analytics & Insight Platform")
    st.write("""The rise of ride-sharing platforms has transformed urban mobility, 
             offering convenience and affordability to millions of users. 
             OLA, a leading ride-hailing service, generates vast amounts of data related
            to ride bookings, driver availability, fare calculations, and customer 
             preferences. However, deriving actionable insights from this data remains a 
             challenge. To enhance operational efficiency, improve customer satisfaction, 
             and optimize business strategies, this project focuses on analyzing OLA’s
              ride-sharing data. By leveraging data analytics, visualization techniques, 
             and interactive applications, the goal is to extract meaningful insights that 
             can drive data-informed decisions. The project will involve cleaning and 
             processing raw ride data, performing exploratory data analysis (EDA), 
             developing a dynamic Power BI dashboard, and creating a Streamlit-based web
              application to present key findings in an interactive and user-friendly manner.""")




#----------------------------------- Ratings Page-----------------------------------------

elif page == "Ratings":
    st.title("Ratings")
    ride_status = ["Driver ratings for Prime Sedan bookings","Average customer rating per vehicle type"]
    selected_status = st.radio("**Ratings**",ride_status)

    if selected_status == "Driver ratings for Prime Sedan bookings":
        query = "SELECT Vehicle_Type, MAX(Driver_Ratings) AS MAX_Rating, MIN(Driver_Ratings) AS MIN_Rating FROM olarides WHERE Vehicle_Type = 'Prime Sedan';"
        query_result = get_data(query)
    
    elif selected_status == "Average customer rating per vehicle type":
        query = "SELECT Vehicle_Type,AVG(Customer_Rating) AS AVG_Customer_Rating FROM olarides GROUP BY Vehicle_Type;"
        query_result = get_data(query)
    st.write("### Query Result:")
    st.dataframe(query_result,hide_index=True,)


#----------------------------------- Ride Status Page-----------------------------------------

elif page == "Ride Status":
    st.title("Ride Status")
    booking = ["Successful bookings","Incomplete rides along with the reason","Average ride distance for each vehicle type","Total number of cancelled rides by customers","Number of rides cancelled by drivers due to personal and car-related issues"]
    booking_query = st.selectbox("**Choose a Query**",booking)

    if booking_query == "Successful bookings":
        query = "SELECT * FROM olarides where Booking_Status = 'Success';"
        query_result = get_data(query)
        
    elif booking_query == "Incomplete rides along with the reason":
        query = "SELECT 'Date',Booking_ID,Booking_Status,Customer_ID,Vehicle_Type,Incomplete_Rides,Incomplete_Rides_Reason FROM olarides WHERE Incomplete_Rides='Yes';"
        query_result = get_data(query)

    elif booking_query == "Average ride distance for each vehicle type":
        query = "SELECT Vehicle_Type,AVG(Ride_Distance) FROM olarides GROUP BY Vehicle_Type ;"
        query_result = get_data(query)

    elif booking_query == "Total number of cancelled rides by customers":
        query = "SELECT COUNT(*) AS Rides_Cancelled_By_Customer FROM olarides where Booking_Status = 'Canceled by Customer';"
        query_result = get_data(query)
    
    elif booking_query == "Number of rides cancelled by drivers due to personal and car-related issues":
        query = "SELECT Booking_Status,Canceled_Rides_by_Driver,COUNT(*) AS Rides_Cancelled FROM olarides where Booking_Status = 'Canceled by Driver' and Canceled_Rides_by_Driver = 'Personal & Car related issue';"
        query_result = get_data(query)

    st.write("### Query Result:")
    st.dataframe(query_result,hide_index=True,)


#----------------------------------- Bookings  Page-----------------------------------------

elif page == "Bookings":
    st.title("Bookings")
    booking = ["Top 5 customers","Payment made using UPI","Total booking value of rides completed successfully"]
    booking_query = st.selectbox("**Choose a Query**",booking)

    if booking_query == "Top 5 customers":
        query = "SELECT Customer_ID, COUNT(*) AS Highest_NUMBER_OF_RIDES FROM olarides GROUP BY Customer_ID ORDER BY Highest_NUMBER_OF_RIDES DESC LIMIT 5;"
        query_result = get_data(query)
        
    elif booking_query == "Payment made using UPI":
        query = "SELECT * FROM olarides WHERE Payment_Method = 'UPI';"
        query_result = get_data(query)

    elif booking_query == "Total booking value of rides completed successfully":
        query = "SELECT Booking_Status,SUM(Booking_Value) AS Total_Booking_Value FROM olarides WHERE Booking_Status = 'success';"
        query_result = get_data(query)
    st.write("### Query Result:")
    st.dataframe(query_result,hide_index=True,)

#----------------------------------- Creator InformATION Page-----------------------------------------

elif page == "Creator Information":
    st.title("Creator Information")
    st.subheader("Name : Shruti Kinalekar")
    st.write("""Software Engineer with total 8 years of experience in Software Testing.
             \nCurrently working on Data Science Projects.
             \nTools : Python, MySQl, Streamlit,vc++,Oracle""")

        
