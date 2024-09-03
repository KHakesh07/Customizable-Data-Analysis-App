import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Customizable Data analysis Dashboard")

uploaded_file = st.file_uploader("Upload your csv file", type=["CSV"])

if uploaded_file is not None:
   data = pd.read_csv(uploaded_file)
   st.write("Data Preview:",data.head())
   st.write("Data Insights:", data.describe())
   

   st.subheader("Data Cleaning Options")
   remove_na = st.checkbox("Remove rows with missing values")
   if remove_na:
      data = data.dropna()
      st.write("Data after removing NA values:", data.head())
      st.write("Insights:", data.describe())
  
   st.subheader("Data Filters")
   columns = data.columns.tolist()
   selected_column = st.selectbox("Selected column to filter", columns)
   unique_values = data[selected_column].unique()
   selected_values = st.selectbox("Select values:", unique_values)

   filtered_Data = data[data[selected_column] == selected_values]
   st.write("filtered Data:", filtered_Data)
   st.write("Count:", filtered_Data[selected_column].count())

   st.subheader("Data Visualization")
   plot_type = st.selectbox("select the plot type", ["Scatter", "Bar", "Line"])
   x_axis = st.selectbox("Select X-axis", columns)
   y_axis = st.selectbox("select y-axis", columns)

   if plot_type == "Scatter":
      fig = px.scatter(filtered_Data, x=x_axis, y=y_axis)
   elif plot_type == "Bar":
      fig = px.bar(filtered_Data, x=x_axis, y=y_axis) 
   else:
      fig = px.line(filtered_Data, x=x_axis, y=y_axis)
   st.plotly_chart(fig)

   st.subheader("Data Analysis")
   group_by_column = st.selectbox("Select a column to group by", columns)
   agg_function = st.selectbox("select aggregation function", ["mean", "sum", "count"])
   if agg_function == "mean":
      agg_data = filtered_Data.groupby(group_by_column).mean()
   elif agg_function == "sum":
      agg_data = filtered_Data.groupby(group_by_column).sum()
   else:
      agg_data = filtered_Data.groupby(group_by_column).count()
   st.write("Aggregated Data:", agg_data)












