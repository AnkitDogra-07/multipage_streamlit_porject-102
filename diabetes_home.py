#  Show complete dataset and summary in 'diabetes_home.py'
# Import the streamlit modules.
import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(diabetes_df):
    # Set the title to the home page contents.
    st.title("Early Diabetes Prediciton Web App")
    # Provide a brief description for the web app.
    st.markdown('''<p style = "Color:red">Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.

There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.

This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.
''', unsafe_allow_html = True)

    # Add the 'beta_expander' to view full dataset 
    st.header("View Data")
    with st.expander("View Full DataSet"):
     st.table(diabetes_df)
     
    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
    with st.subheader("Column's Descrption"):
     col1, col2, col3 = st.columns(3)

    with col1 :
      if st.checkbox("Show all column names"):
        st.table(list(diabetes_df.columns))
    # Add a checkbox in the second column. Display the column data-types of 'diabetes_df' on the click of checkbox.
    with col2:
      if st.checkbox("View Columns Data-Type"):
        st.table(diabetes_df.dtypes)
    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with col3 :
      if st.checkbox("View column data"):
        column_data = st.selectbox("Select_columns" , tuple(diabetes_df.columns))
        if column_data == "Pregnancies":
          st.write(diabetes_df["Pregnancies"]) 

        elif column_data == "Glucose":
          st.write(diabetes_df["Glucose"])

        elif column_data == "Blood_Pressure":
          st.write(diabetes_df["Blood_Pressure"])

        elif column_data == "Skin_Thickness":
          st.write(diabetes_df["Skin_Thickness"])

        elif column_data == "Insulin":
          st.write(diabetes_df["Insulin"])

        elif column_data == "BMI":
          st.write(diabetes_df["BMI"])

        elif column_data == "Pedigree_Function":
          st.write(diabetes_df["Pedigree_Function"])

        elif column_data == "Age":
          st.write(diabetes_df["Age"])

        else:
          st.write(diabetes_df['Outcome'])