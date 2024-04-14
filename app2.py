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

# Function to load CSV files from the directory
def load_csv_files(directory):
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    return csv_files

# Function to load the selected CSV file
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
    fig.update_layout(title='Candlestick Chart',
                      xaxis_title='Index Number According to the Table (Newest Date First)',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=False)
    st.plotly_chart(fig)

# Streamlit UI
st.title("Volume Percentage Pie Chart and Candlestick Chart")

# Fetch all CSV files from the current directory
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# Dropdown menu to select a CSV file
selected_csv = st.selectbox("Choose a CSV file", csv_files)

if selected_csv:
    df = load_data(selected_csv)

    # Separate date and time from Timestamp column
    df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
    df['Time'] = pd.to_datetime(df['Timestamp']).dt.time

    # Create a new DataFrame with Date, Time, and other previous columns
    new_df = df[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'VWAP', 'Type', 'Range']]

    # Date and time selection
    selected_date = st.date_input("Select Date", min_value=new_df['Date'].min(), max_value=new_df['Date'].max(), value=new_df['Date'].min())
    selected_time = st.time_input("Select Time", value=new_df['Time'].iloc[0])

    custom_date = pd.to_datetime(f"{selected_date.strftime('%Y-%d-%m')}")

    # Filter data based on selected date and time
    filtered_data = new_df[(new_df['Date'] == custom_date) & (new_df['Time'] == selected_time)]

    st.write("Filtered Data:")
    st.write(filtered_data)

    if not filtered_data.empty:
        # Calculate percentage of buy and sell volumes
        buy_percentage, sell_percentage, total_volume, buy_volume, sell_volume = calculate_percentage(new_df, selected_time, custom_date)

        if total_volume > 0:  # Ensure that total_volume is non-zero
            # Create a pie chart
            labels = ['Buy', 'Sell']
            sizes = [buy_percentage, sell_percentage]
            volumes = [buy_volume, sell_volume]
            colors = ['green', 'red']  # Green for buy, red for sell
            explode = (0.1, 0)

            # Plot pie chart using Streamlit's native function
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops=dict(color="w"), colors=colors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Show pie chart in Streamlit
            st.pyplot(fig1)

            # Create custom tooltip format
            tooltip_text = [
                f"Type: {labels[i]}, Volume: {volumes[i]} ({sizes[i]:.2f}%)"
                for i in range(len(labels))
            ]
            tooltip_text.append(f"Total Volume: {total_volume}")

            # Display tooltip
            st.write("\n".join(tooltip_text))

            # Create candlestick chart
            create_candlestick_chart(new_df)
        else:
            st.write("Total volume is zero. Cannot create pie chart.")
    else:
        st.write("No data available for the selected date and time.")
