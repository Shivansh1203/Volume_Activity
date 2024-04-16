# import streamlit as st
# import pandas as pd
# import os

# # Function to load CSV files from the directory
# def load_csv_files(directory):
#     csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
#     return csv_files

# # Function to load the selected CSV file
# @st.cache_data
# def load_data(selected_csv):
#     df = pd.read_csv(selected_csv)
#     st.write(df)
#     return df

# # Streamlit UI
# st.title("Custom Date and Time Selection")

# # Fetch all CSV files from the current directory
# csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# # Dropdown menu to select a CSV file
# selected_csv = st.selectbox("Choose a CSV file", csv_files)

# if selected_csv:
#     df = load_data(selected_csv)

#     # Splitting the Timestamp column into Date and Time columns
#     df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
#     df['Time'] = pd.to_datetime(df['Timestamp']).dt.time

#     # Create a new DataFrame with Date, Time, and other previous columns
#     new_df = df[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'VWAP', 'Type', 'Range']]

#     st.write("New DataFrame with Date, Time, and other previous columns:")
#     st.write(new_df)

#     # Date and time selection
#     selected_date = st.date_input("Select Date", min_value=new_df['Date'].min(), max_value=new_df['Date'].max(), value=new_df['Date'].min())
#     selected_time = st.time_input("Select Time", value=new_df['Time'].iloc[0])

#     # Convert custom date and time to match the format of the 'Timestamp' column in the new DataFrame
#     custom_date = pd.to_datetime(f"{selected_date.strftime('%Y-%d-%m')}")

#     st.write("Selected Date and Time:", custom_date)

#     # print(selected_date)
#     # print(custom_date)
#     # print(selected_time)

#     # Filter data based on selected date and time
#     filtered_data = new_df[(new_df['Date'] == custom_date) & (new_df['Time'] == selected_time)]

#     st.write("Filtered Data:")
#     st.write(filtered_data)

#     if not filtered_data.empty:
#         # Display volume and type
#         st.subheader("Selected Data:")
#         st.write(filtered_data[['Volume', 'Type']])
#     else:
#         st.write("No data available for the selected date and time.")

# import streamlit as st
# import pandas as pd
# import os
# import matplotlib.pyplot as plt

# # Function to load CSV files from the directory
# def load_csv_files(directory):
#     csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
#     return csv_files

# # Function to load the selected CSV file
# @st.cache_data
# def load_data(selected_csv):
#     df = pd.read_csv(selected_csv)
#     st.write(df)
#     return df

# # Function to calculate percentage of buy and sell volumes
# def calculate_percentage(new_df, selected_time, custom_date):
#     filtered_df = new_df[(new_df['Time'] == selected_time) & (new_df['Date'] <= custom_date)]
#     total_volume = filtered_df['Volume'].sum()
#     buy_volume = filtered_df[filtered_df['Type'] == 'Buy']['Volume'].sum()
#     sell_volume = filtered_df[filtered_df['Type'] == 'Sell']['Volume'].sum()
#     total_count = len(filtered_df)
#     buy_count = len(filtered_df[filtered_df['Type'] == 'Buy'])
#     sell_count = len(filtered_df[filtered_df['Type'] == 'Sell'])
#     buy_percentage = (buy_count / total_count) * 100 if total_volume > 0 else 0
#     sell_percentage = (sell_count / total_count) * 100 if total_volume > 0 else 0
#     return buy_percentage, sell_percentage, total_volume, buy_volume, sell_volume

# # Streamlit UI
# st.title("Volume Percentage Pie Chart")

# # Fetch all CSV files from the current directory
# csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# # Dropdown menu to select a CSV file
# selected_csv = st.selectbox("Choose a CSV file", csv_files)

# if selected_csv:
#     df = load_data(selected_csv)

#     # Separate date and time from Timestamp column
#     df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
#     df['Time'] = pd.to_datetime(df['Timestamp']).dt.time

#     # Create a new DataFrame with Date, Time, and other previous columns
#     new_df = df[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'VWAP', 'Type', 'Range']]

#     # Date and time selection
#     selected_date = st.date_input("Select Date", min_value=new_df['Date'].min(), max_value=new_df['Date'].max(), value=new_df['Date'].min())
#     selected_time = st.time_input("Select Time", value=new_df['Time'].iloc[0])

#     custom_date = pd.to_datetime(f"{selected_date.strftime('%Y-%d-%m')}")

#     # Filter data based on selected date and time
#     filtered_data = new_df[(new_df['Date'] == custom_date) & (new_df['Time'] == selected_time)]

#     st.write("Filtered Data:")
#     st.write(filtered_data)

#     if not filtered_data.empty:
#         # Display volume and type
#         st.subheader("Selected Data:")
#         st.write(filtered_data[['Volume', 'Type']])

#         # Calculate percentage of buy and sell volumes
#         buy_percentage, sell_percentage, total_volume, buy_volume, sell_volume = calculate_percentage(new_df, selected_time, custom_date)

#         # Create a pie chart
#         labels = ['Buy', 'Sell']
#         sizes = [buy_percentage, sell_percentage]
#         volumes = [buy_volume, sell_volume]
#         explode = (0.1, 0)
#         fig1, ax1 = plt.subplots()
#         wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops=dict(color="w"))

#         # Create custom tooltip format
#         tooltip_text = [
#             f"Type: {labels[i]}, Volume: {volumes[i]} ({sizes[i]:.2f}%)"
#             for i in range(len(labels))
#         ]
#         tooltip_text.append(f"Total Volume: {total_volume}")

#         # Update tooltips
#         tooltip = st.pyplot(fig1)
#         tooltip.write("\n".join(tooltip_text))
#     else:
#         st.write("No data available for the selected date and time.")

# import streamlit as st
# import pandas as pd
# import os
# import matplotlib.pyplot as plt

# # Function to load CSV files from the directory
# def load_csv_files(directory):
#     csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
#     return csv_files

# # Function to load the selected CSV file
# @st.cache_data
# def load_data(selected_csv):
#     df = pd.read_csv(selected_csv)
#     st.write(df)
#     return df

# # Function to calculate percentage of buy and sell volumes
# def calculate_percentage(new_df, selected_time, custom_date):
#     filtered_df = new_df[(new_df['Time'] == selected_time) & (new_df['Date'] <= custom_date)]
#     total_volume = filtered_df['Volume'].sum()
#     buy_volume = filtered_df[filtered_df['Type'] == 'Buy']['Volume'].sum()
#     sell_volume = filtered_df[filtered_df['Type'] == 'Sell']['Volume'].sum()
#     total_count = len(filtered_df)
#     buy_count = len(filtered_df[filtered_df['Type'] == 'Buy'])
#     sell_count = len(filtered_df[filtered_df['Type'] == 'Sell'])
#     buy_percentage = (buy_count / total_count) * 100 if total_volume > 0 else 0
#     sell_percentage = (sell_count / total_count) * 100 if total_volume > 0 else 0
#     return buy_percentage, sell_percentage, total_volume, buy_volume, sell_volume

# # Streamlit UI
# st.title("Volume Percentage Pie Chart")

# # Fetch all CSV files from the current directory
# csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# # Dropdown menu to select a CSV file
# selected_csv = st.selectbox("Choose a CSV file", csv_files)

# if selected_csv:
#     df = load_data(selected_csv)

#     # Separate date and time from Timestamp column
#     df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
#     df['Time'] = pd.to_datetime(df['Timestamp']).dt.time

#     # Create a new DataFrame with Date, Time, and other previous columns
#     new_df = df[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'VWAP', 'Type', 'Range']]

#     # Date and time selection
#     selected_date = st.date_input("Select Date", min_value=new_df['Date'].min(), max_value=new_df['Date'].max(), value=new_df['Date'].min())
#     selected_time = st.time_input("Select Time", value=new_df['Time'].iloc[0])

#     custom_date = pd.to_datetime(f"{selected_date.strftime('%Y-%d-%m')}")

#     # Filter data based on selected date and time
#     filtered_data = new_df[(new_df['Date'] == custom_date) & (new_df['Time'] == selected_time)]

#     st.write("Filtered Data:")
#     st.write(filtered_data)

#     if not filtered_data.empty:
#         # Calculate percentage of buy and sell volumes
#         buy_percentage, sell_percentage, total_volume, buy_volume, sell_volume = calculate_percentage(new_df, selected_time, custom_date)

#         if total_volume > 0:  # Ensure that total_volume is non-zero
#             # Create a pie chart
#             labels = ['Buy', 'Sell']
#             sizes = [buy_percentage, sell_percentage]
#             volumes = [buy_volume, sell_volume]
#             colors = ['green', 'red']  # Green for buy, red for sell
#             explode = (0.1, 0)

#             # Plot pie chart using Streamlit's native function
#             fig1, ax1 = plt.subplots()
#             ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops=dict(color="w"), colors=colors)
#             ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#             # Show pie chart in Streamlit
#             st.pyplot(fig1)

#             # Create custom tooltip format
#             tooltip_text = [
#                 f"Type: {labels[i]}, Volume: {volumes[i]} ({sizes[i]:.2f}%)"
#                 for i in range(len(labels))
#             ]
#             tooltip_text.append(f"Total Volume: {total_volume}")

#             # Display tooltip
#             st.write("\n".join(tooltip_text))
#         else:
#             st.write("Total volume is zero. Cannot create pie chart.")
#     else:
#         st.write("No data available for the selected date and time.")


import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from PIL import Image
import requests
import smtplib



st.set_page_config(page_title="MQH-Volume_Activity", page_icon=":tada:", layout="wide")
# ---- HEADER SECTION ----
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.title("MQH")
        st.write(
            "Stay Ahead of the Game with MQH."
        )
        st.write("MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision.")
    with c2:
          
            image = Image.open('images/mqh_logo.jpeg')

            resized_image = image.resize((300, 300))

            st.image(resized_image)
            






st.sidebar.header('MQH (Volume Based Activity)')
st.sidebar.header("Select The Parameters:")

def load_csv_files(directory):
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    return csv_files


@st.cache_data
def load_data(selected_csv):
    df = pd.read_csv(selected_csv)
    st.write(df)
    return df

# Function to calculate percentage of buy and sell volumes
def calculate_percentage(new_df, selected_time, custom_date):
    filtered_df = new_df[(new_df['Time'] == selected_time) & (new_df['Date'] <= custom_date)]
    total_volume = filtered_df['Volume'].sum()
    buy_volume = filtered_df[filtered_df['Type'] == 'Buy']['Volume'].sum()
    sell_volume = filtered_df[filtered_df['Type'] == 'Sell']['Volume'].sum()
    total_count = len(filtered_df)
    buy_count = len(filtered_df[filtered_df['Type'] == 'Buy'])
    sell_count = len(filtered_df[filtered_df['Type'] == 'Sell'])
    buy_percentage = (buy_count / total_count) * 100 if total_volume > 0 else 0
    sell_percentage = (sell_count / total_count) * 100 if total_volume > 0 else 0
    return buy_percentage, sell_percentage, total_volume, buy_volume, sell_volume

# Function to create candlestick chart
def create_candlestick_chart(filtered_df):
    # Filter the data where the date is less than or equal to the selected date
    filtered_df = new_df[(new_df['Date'] <= custom_date)]

    fig = go.Figure(data=[go.Candlestick(x=filtered_df.index,
                                         open=filtered_df['Open'],
                                         high=filtered_df['High'],
                                         low=filtered_df['Low'],
                                         close=filtered_df['Close'])])
    st.subheader("Candlestick Chart (Note-> Newest Date First in the Chart)")
    fig.update_layout(title='Candlestick Chart',
                      xaxis_title='Index Number According to the Table (Newest Date First)',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=False)
    st.plotly_chart(fig)


st.title("Dataset Viewer")


csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]


selected_csv = st.sidebar.selectbox("Choose a CSV file:", csv_files)

if selected_csv:
    df = load_data(selected_csv)

 
    df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
    df['Time'] = pd.to_datetime(df['Timestamp']).dt.time


    new_df = df[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'VWAP', 'Type', 'Range']]

 
    selected_date = st.sidebar.date_input("Select Date:", min_value=new_df['Date'].min(), max_value=new_df['Date'].max(), value=new_df['Date'].min())
    selected_time = st.sidebar.time_input("Select Time:", value=new_df['Time'].iloc[0])

    custom_date = pd.to_datetime(f"{selected_date.strftime('%Y-%d-%m')}")

  
    filtered_data = new_df[(new_df['Date'] == custom_date) & (new_df['Time'] == selected_time)]

    st.subheader("Filtered Data:")
    st.write(filtered_data)

    if not filtered_data.empty:
       
        buy_percentage, sell_percentage, total_volume, buy_volume, sell_volume = calculate_percentage(new_df, selected_time, custom_date)

        if total_volume > 0:  
           
            labels = ['Buy', 'Sell']
            sizes = [buy_percentage, sell_percentage]
            volumes = [buy_volume, sell_volume]
            colors = ['green', 'red']  # Green for buy, red for sell
            explode = (0.1, 0)

            # Plot pie chart using Streamlit's native function
            fig1, ax1 = plt.subplots(figsize=(3, 3))

            # fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops=dict(color="w"), colors=colors)
            ax1.axis('equal')  
            
            st.subheader("Buy/Sell Type Volume Share Pie Chart")
            st.pyplot(fig1)

            st.subheader("The Required Buy/Sell Volume Percentage upto the selected date for a particular timespan")
            # tooltip_text = [
            #     f"Type: {labels[i]}, Volume: {volumes[i]} ({sizes[i]:.2f}%)"
            #     for i in range(len(labels))
            # ]
            # tooltip_text.append(f"Total Volume: {total_volume}")

          
            # st.write("\n".join(tooltip_text))
            tooltip_text = [
                f"<b>Type:</b> {labels[i]}, <b>Volume:</b> {volumes[i]} ({sizes[i]:.2f}%)"
                for i in range(len(labels))
            ]
            tooltip_text.append(f"<b>Total Volume:</b> {total_volume}")

            # Display tooltip
            st.write("\n".join(tooltip_text), unsafe_allow_html=True)

         
            create_candlestick_chart(new_df)
        else:
            st.write("Total volume is zero. Cannot create pie chart.")
    else:
        st.write("No data available for the selected date and time.")


st.sidebar.markdown('''
---
Created with ❤️ by [Shivansh](https://github.com/Shivansh1203/Volume_Activity).
''')


with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.write("##")

 
    def send_email(name, email, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("epicstruchain@gmail.com", "imttyfmbkriojftd")
        msg = f"Subject: New message from {name}\n\n{name} ({email}) sent the following message:\n\n{message}"
        server.sendmail("epicstruchain@gmail.com", "epicstruchain@gmail.com", msg)
        st.success("Thank you for contacting us.")
        
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        send_email(name, email, message)

    
    st.markdown(
    """
    <style>
       
         /* Adjust the width of the form elements */
        .stTextInput {
            width: 50%;
        }
        
        .stTextArea {
            width: 20%;
        }
        /* Style the submit button */
        .stButton button {
            background-color: #45a049;
            color: #FFFFFF;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            width: 10%;
        }
        /* Style the success message */
        .stSuccess {
            color: #0072C6;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

