import streamlit as st
from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Supabase
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Test page
st.title("🚀 Auth Dashboard")
st.write("Setup successful!")
st.success("✅ Connected to Supabase!")
