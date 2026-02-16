import streamlit as st
import pandas as pd
import os

# Set page configuration
st.set_page_config(page_title="Resume Completion Dashboard", layout="wide")

@st.cache_data
def load_excel_data(file_path):
    """
    Loads data from an Excel file.
    """
    if not os.path.exists(file_path):
        return None
    # Using openpyxl engine to read .xlsx files
    return pd.read_excel(file_path, engine='openpyxl')

def main():
    st.title("📊 Resume Completion Dashboard")
    
    # The exact name of your file
    file_name = 'resume_completion_%.xlsx'
    
    try:
        # Load the data
        data = load_excel_data(file_name)
        
        if data is not None:
            st.success(f"Successfully loaded: {file_name}")
            
            # 1. Show a high-level summary
            st.subheader("📈 Data Overview")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Records", len(data))
            
            # If you have a column named 'Completion %', we can show the average
            # (Adjust 'Completion %' to match your actual column name)
            if 'Completion %' in data.columns:
                avg_completion = data['Completion %'].mean()
                col2.metric("Avg. Completion", f"{avg_completion:.1f}%")
            
            # 2. Display the interactive table
            st.subheader("📄 Detailed Data View")
            st.dataframe(data, use_container_width=True)
            
            # 3. Simple Visualization (Example: Bar chart of completion)
            if 'Completion %' in data.columns:
                st.subheader("📊 Completion Distribution")
                st.bar_chart(data['Completion %'])
                
        else:
            st.error(f"File not found: {file_name}. Please ensure the file is in the same folder as this script.")
            
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
        st.info("Tip: Make sure you have installed the required library by running: pip install openpyxl")

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd

st.title("📊 Excel Data Dashboard")

# This adds a "Browse Files" button to your dashboard!
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Load the file the user just uploaded
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    st.dataframe(df) # Show the data
else:
    st.info("Please upload an Excel file to begin.")
