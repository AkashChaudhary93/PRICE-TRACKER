# import streamlit as st
# import os
# from dotenv import load_dotenv
# from utils.web_search import search_product_prices
# from utils.database_manager import DatabaseManager
# from utils.email_sender import EmailSender

# # Load environment variables FIRST
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# SENDER_EMAIL = os.getenv("SENDER_EMAIL")
# SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
# RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")


# # Move these checks AFTER loading .env
# if not GEMINI_API_KEY:
#     st.warning("Please set your Gemini API key in the .env file.")
#     st.stop()

# # Initialize database and email sender AFTER environment check
# db_manager = DatabaseManager("product_prices.db")
# email_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)

# st.title("Product Price Tracker Chatbot")

# st.sidebar.title("Configuration")
# recipient_email = st.sidebar.text_input("Your Email for Notifications", RECIPIENT_EMAIL)

# if not GEMINI_API_KEY:
#     st.warning("Please set your Gemini API key in the .env file.")
#     st.stop()

# if not recipient_email:
#     st.warning("Please provide your email address in the sidebar for notifications.")
#     st.stop()

# # Add instructions for better search results
# st.markdown("""
# ### How to get the best results:
# 1. Be specific with your product search (include brand, model number, etc.)
# 2. For electronics, include specifications like storage capacity or color
# 3. For clothing, mention size, color, and brand
# """)

# product_query = st.text_input("Enter the product you want to search for:", 
#                              placeholder="e.g., iPhone 15 Pro Max 256GB Black")

# if st.button("Search Prices"):
#     if not product_query:
#         st.warning("Please enter a product to search for.")
#     else:
#         with st.spinner(f"Searching the web for prices of {product_query}..."):
#             st.subheader(f"Searching for: {product_query}")

#             if GEMINI_API_KEY:
#                 results = search_product_prices(product_query, GEMINI_API_KEY)

#                 if results:
#                     st.success(f"Found {len(results)} price listings!")
#                     st.subheader("Price Comparison Results:")
#                     st.table(results)

#                     # Store results in session state
#                     st.session_state.email_results = results
#                     st.session_state.email_query = product_query

#                     # Show email section after storing results
#                     st.markdown("---")
#                     st.subheader("Email Options")

# # Add email section outside the search button context
# if 'email_results' in st.session_state:
#     with st.form(key="email_form"):
#         st.write("Send latest search results to your email:")
#         if st.form_submit_button("📨 Send Price Information"):
#             email_body = "Current Price Information:\n\n"
            
#             for item in st.session_state.email_results:
#                 product = item.get("Product", st.session_state.email_query)
#                 platform = item.get("Platform", "N/A")
#                 price = item.get("Price", "N/A")
#                 email_body += f"Product: {product}\nPlatform: {platform}\nPrice: {price}\n\n"
            
#             try:
#                 # Reinitialize email sender with current credentials
#                 current_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)
#                 current_sender.send_email(
#                     recipient_email,
#                     f"Current Prices for {st.session_state.email_query}",
#                     email_body
#                 )
#                 st.success("Email sent successfully! Check your inbox.")
#             except Exception as e:
#                 st.error(f"Email failed: {str(e)}")
#                 st.info("Use the test app (app2.py) to verify your email settings")
                
#                 # Store in database and check for price differences
#                 for item in results:
#                     product_name = item.get("Product", product_query)
#                     platform = item.get("Platform", "N/A")
#                     price_str = item.get("Price", "N/A").replace(",", "").replace("₹", "").strip()
#                     try:
#                         price = float(price_str)
#                     except ValueError:
#                         price = None

#                     if price is not None:
#                         stored_price = db_manager.get_price(product_name, platform)
#                         if stored_price is not None and abs(price - stored_price) > 0.01:  # Check for significant difference
#                             subject = f"Price Alert for {product_name} on {platform}"
#                             body = f"The price of {product_name} on {platform} has changed from ₹{stored_price:.2f} to ₹{price:.2f}."
#                             email_sender.send_email(recipient_email, subject, body)
#                         db_manager.insert_price(product_name, platform, price)
#                 else:
#                     st.error("No price information found for the product.")
#                     st.info("""
#                     Try these tips:
#                     - Be more specific with your search query
#                     - Include brand name and model number
#                     - Check if the product is available in India
#                     - Try a different product
#                     """)
#             else:
#                 st.warning("Gemini API key not configured.")
import streamlit as st
import os
from dotenv import load_dotenv
from utils.web_search import search_product_prices
from utils.database_manager import DatabaseManager
from utils.email_sender import EmailSender

# Load environment variables FIRST
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Move these checks AFTER loading .env
if not GEMINI_API_KEY:
    st.warning("Please set your Gemini API key in the .env file.")
    st.stop()

# Initialize database and email sender AFTER environment check
db_manager = DatabaseManager("product_prices.db")
email_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)

# 🎯 Title & Intro
st.title("🔍 Product Price Tracker Chatbot")
st.write("Get real-time product prices and alerts from across the web! 🚀")

# 📌 Sidebar Configuration
st.sidebar.markdown("## ⚙️ Configuration")
recipient_email = st.sidebar.text_input("📧 **Your Email for Notifications**", RECIPIENT_EMAIL)

# 📝 New Sidebar Description Section
st.sidebar.markdown("---")
st.sidebar.markdown("## ℹ️ Description")
st.sidebar.markdown("""
This chatbot helps you track and compare prices from different e-commerce platforms.  

🔍 **Key Features:**  
- 🛒 Real-time product price tracking  
- 📩 Email notifications for price drops  
- 📊 Smart price comparisons  

Enter a product name to get the best prices available online! 🚀  
""")
st.sidebar.markdown("---")

# Check for required inputs
if not recipient_email:
    st.warning("Please provide your email address in the sidebar for notifications.")
    st.stop()

# 📌 About Section
with st.expander("ℹ️ About This App", expanded=True):
    st.markdown("""
    **Welcome to the Product Price Tracker Chatbot!**  
    This tool helps you:
    - 🛍️ **Find the best product prices online**
    - 📊 **Compare price listings from different websites**
    - 📩 **Receive email alerts for price drops**
    - 🛠️ **Track your favorite products automatically**
    
    **Built with** Streamlit + Gemini API.
    """)

# 🔹 Best Practices Section
st.markdown("## 🏆 How to Get the Best Results:")
st.markdown("""
1. **Be Specific** - Mention brand, model, and variant (e.g., _iPhone 15 Pro Max 256GB Black_).
2. **Include Technical Details** - For electronics, add RAM, storage, etc.
3. **For Clothing** - Specify size, color, and brand.
""")

# 🛍️ Product Search Input
product_query = st.text_input("Enter the product you want to search for:", 
                             placeholder="e.g., iPhone 15 Pro Max 256GB Black")

# ❌ Prevent Random Queries (Non-Product)
def is_valid_product_query(query):
    keywords = ["buy", "price", "cost", "discount", "offer", "sale"]
    return any(word in query.lower() for word in keywords)

# 🔍 Search Prices Button
if st.button("🔎 Search Prices"):
    if not product_query:
        st.warning("Please enter a product to search for.")
    elif not is_valid_product_query(product_query):
        st.error("I am only a price-tracking chatbot. Please enter a product name.")
    else:
        with st.spinner(f"Searching the web for prices of {product_query}..."):
            st.subheader(f"🔍 Searching for: {product_query}")

            if GEMINI_API_KEY:
                results = search_product_prices(product_query, GEMINI_API_KEY)

                if results:
                    st.success(f"✅ Found {len(results)} price listings!")
                    st.subheader("💰 Price Comparison Results:")
                    st.table(results)

                    # Store results in session state
                    st.session_state.email_results = results
                    st.session_state.email_query = product_query

                    # Show email section after storing results
                    st.markdown("---")
                    st.subheader("📨 Email Options")

# 📧 Email Results Section
if 'email_results' in st.session_state:
    with st.form(key="email_form"):
        st.write("📩 Send latest search results to your email:")
        if st.form_submit_button("📨 Send Price Information"):
            email_body = "📊 **Current Price Information:**\n\n"
            
            for item in st.session_state.email_results:
                product = item.get("Product", st.session_state.email_query)
                platform = item.get("Platform", "N/A")
                price = item.get("Price", "N/A")
                email_body += f"**Product:** {product}\n**Platform:** {platform}\n**Price:** {price}\n\n"
            
            try:
                # Reinitialize email sender with current credentials
                current_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)
                current_sender.send_email(
                    recipient_email,
                    f"🔔 Current Prices for {st.session_state.email_query}",
                    email_body
                )
                st.success("✅ Email sent successfully! Check your inbox.")
            except Exception as e:
                st.error(f"❌ Email failed: {str(e)}")
                st.info("💡 Use the test app (`app2.py`) to verify your email settings.")
                
                # Store in database and check for price differences
                for item in results:
                    product_name = item.get("Product", product_query)
                    platform = item.get("Platform", "N/A")
                    price_str = item.get("Price", "N/A").replace(",", "").replace("₹", "").strip()
                    try:
                        price = float(price_str)
                    except ValueError:
                        price = None

                    if price is not None:
                        stored_price = db_manager.get_price(product_name, platform)
                        if stored_price is not None and abs(price - stored_price) > 0.01:  # Check for significant difference
                            subject = f"⚠️ Price Alert for {product_name} on {platform}"
                            body = f"The price of {product_name} on {platform} has changed from ₹{stored_price:.2f} to ₹{price:.2f}."
                            email_sender.send_email(recipient_email, subject, body)
                        db_manager.insert_price(product_name, platform, price)
                else:
                    st.error("❌ No price information found for the product.")
                    st.info("""
                    **Try these tips:**
                    - Be more specific with your search query
                    - Include brand name and model number
                    - Check if the product is available in India
                    - Try a different product
                    """)
            else:
                st.warning("⚠️ Gemini API key not configured.")

