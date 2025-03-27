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

# # 🎯 Title & Intro
# st.title("🔍 Product Price Tracker Chatbot")
# st.write("Get real-time product prices and alerts from across the web! 🚀")

# # 📌 Sidebar Configuration
# st.sidebar.markdown("## ⚙️ Configuration")
# recipient_email = st.sidebar.text_input("📧 **Your Email for Notifications**", RECIPIENT_EMAIL)

# # 📝 New Sidebar Description Section
# st.sidebar.markdown("---")
# st.sidebar.markdown("## ℹ️ Description")
# st.sidebar.markdown("""
# This chatbot helps you track and compare prices from different e-commerce platforms.  

# 🔍 **Key Features:**  
# - 🛒 Real-time product price tracking  
# - 📩 Email notifications for price drops  
# - 📊 Smart price comparisons  

# Enter a product name to get the best prices available online! 🚀  
# """)
# st.sidebar.markdown("---")

# # Check for required inputs
# if not recipient_email:
#     st.warning("Please provide your email address in the sidebar for notifications.")
#     st.stop()

# # 📌 About Section
# with st.expander("ℹ️ About This App", expanded=True):
#     st.markdown("""
#     **Welcome to the Product Price Tracker Chatbot!**  
#     This tool helps you:
#     - 🛍️ **Find the best product prices online**
#     - 📊 **Compare price listings from different websites**
#     - 📩 **Receive email alerts for price drops**
#     - 🛠️ **Track your favorite products automatically**
    
#     **Built with** Streamlit + Gemini API.
#     """)

# # 🔹 Best Practices Section
# st.markdown("## 🏆 How to Get the Best Results:")
# st.markdown("""
# 1. **Be Specific** - Mention brand, model, and variant (e.g., _iPhone 15 Pro Max 256GB Black_).
# 2. **Include Technical Details** - For electronics, add RAM, storage, etc.
# 3. **For Clothing** - Specify size, color, and brand.
# """)

# # 🛍️ Product Search Input
# product_query = st.text_input("Enter the product you want to search for:", 
#                              placeholder="e.g., iPhone 15 Pro Max 256GB Black")

# # ❌ Prevent Random Queries (Non-Product)
# def is_valid_product_query(query):
#     keywords = ["buy", "price", "cost", "discount", "offer", "sale"]
#     return any(word in query.lower() for word in keywords)

# # 🔍 Search Prices Button
# if st.button("🔎 Search Prices"):
#     if not product_query:
#         st.warning("Please enter a product to search for.")
#     elif not is_valid_product_query(product_query):
#         st.error("I am only a price-tracking chatbot. Please enter a product name.")
#     else:
#         with st.spinner(f"Searching the web for prices of {product_query}..."):
#             st.subheader(f"🔍 Searching for: {product_query}")

#             if GEMINI_API_KEY:
#                 results = search_product_prices(product_query, GEMINI_API_KEY)

#                 if results:
#                     st.success(f"✅ Found {len(results)} price listings!")
#                     st.subheader("💰 Price Comparison Results:")
#                     st.table(results)

#                     # Store results in session state
#                     st.session_state.email_results = results
#                     st.session_state.email_query = product_query

#                     # Show email section after storing results
#                     st.markdown("---")
#                     st.subheader("📨 Email Options")

# # 📧 Email Results Section
# if 'email_results' in st.session_state:
#     with st.form(key="email_form"):
#         st.write("📩 Send latest search results to your email:")
#         if st.form_submit_button("📨 Send Price Information"):
#             email_body = "📊 **Current Price Information:**\n\n"
            
#             for item in st.session_state.email_results:
#                 product = item.get("Product", st.session_state.email_query)
#                 platform = item.get("Platform", "N/A")
#                 price = item.get("Price", "N/A")
#                 email_body += f"**Product:** {product}\n**Platform:** {platform}\n**Price:** {price}\n\n"
            
#             try:
#                 # Reinitialize email sender with current credentials
#                 current_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)
#                 current_sender.send_email(
#                     recipient_email,
#                     f"🔔 Current Prices for {st.session_state.email_query}",
#                     email_body
#                 )
#                 st.success("✅ Email sent successfully! Check your inbox.")
#             except Exception as e:
#                 st.error(f"❌ Email failed: {str(e)}")
#                 st.info("💡 Use the test app (`app2.py`) to verify your email settings.")
                
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
#                             subject = f"⚠️ Price Alert for {product_name} on {platform}"
#                             body = f"The price of {product_name} on {platform} has changed from ₹{stored_price:.2f} to ₹{price:.2f}."
#                             email_sender.send_email(recipient_email, subject, body)
#                         db_manager.insert_price(product_name, platform, price)
#                 else:
#                     st.error("❌ No price information found for the product.")
#                     st.info("""
#                     **Try these tips:**
#                     - Be more specific with your search query
#                     - Include brand name and model number
#                     - Check if the product is available in India
#                     - Try a different product
#                     """)
#             else:
#                 st.warning("⚠️ Gemini API key not configured.")




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
                
#                 # Validation to ensure meaningful product search results
#                 if not results or all(item.get("Price") in [None, "N/A", "₹ Not Found"] for item in results):
#                     st.error("I am a price tracking chatbot. Please provide a valid product name for price tracking.")
#                 elif any(keyword in product_query.lower() for keyword in ["capital", "weather", "who is", "define", "explain","yuabdyububduyasbdyu","qiwibdbubduabdua"]):
#                     st.error("I am a price tracking chatbot. Please provide a valid product name for price tracking.")
#                 else:
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

# # Set UI theme
# st.set_page_config(page_title="Price Tracker Bot", page_icon="💰", layout="wide")

# # Sidebar Configuration
# st.sidebar.title("⚙️ Configuration")
# st.sidebar.info("🔔 Get notified when the price drops!")
# recipient_email = st.sidebar.text_input("📩 Your Email for Notifications", RECIPIENT_EMAIL)

# if not GEMINI_API_KEY:
#     st.warning("Please set your Gemini API key in the .env file.")
#     st.stop()

# if not recipient_email:
#     st.warning("Please provide your email address in the sidebar for notifications.")
#     st.stop()

# # Main Title
# st.title("💰 Product Price Tracker Chatbot")

# # User Guide
# st.markdown("""
# ### 🛒 How to Get the Best Results:
# ✅ Be **specific** with your product search (include brand, model number, etc.)  
# ✅ For **electronics**, mention storage, color, and model  
# ✅ For **clothing**, mention size, color, and brand  
# """)

# # Search Input
# product_query = st.text_input("🔍 Enter the product you want to search for:", 
#                              placeholder="e.g., iPhone 15 Pro Max 256GB Black")

# # Price Search Button
# if st.button("🔍 Search Prices"):
#     if not product_query:
#         st.warning("⚠️ Please enter a product to search for.")
#     else:
#         with st.spinner(f"Searching the web for prices of **{product_query}**..."):
#             st.subheader(f"🔎 Searching for: {product_query}")

#             if GEMINI_API_KEY:
#                 results = search_product_prices(product_query, GEMINI_API_KEY)

#                 # Handle invalid queries
#                 if not results or all(item.get("Price") in ["₹ Not Found", "N/A"] for item in results):
#                     st.error("🚫 Invalid search query! I am a price-tracking chatbot, please provide a valid product.")
#                 else:
#                     st.success(f"✅ Found {len(results)} price listings!")
#                     st.balloons()  # 🎈 Confetti effect when successful

#                     # Display Results
#                     st.subheader("📊 Price Comparison Results")
#                     st.table(results)

#                     # Store results in session state
#                     st.session_state.email_results = results
#                     st.session_state.email_query = product_query

#                     # Show email section
#                     st.markdown("---")
#                     st.subheader("📩 Email Options")

# # Email Section
# if 'email_results' in st.session_state:
#     with st.form(key="email_form"):
#         st.write("📨 Send latest search results to your email:")
#         if st.form_submit_button("📩 Send Price Information"):
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
#                     f"📊 Current Prices for {st.session_state.email_query}",
#                     email_body
#                 )
#                 st.success("✅ Email sent successfully! Check your inbox. 📬")
#             except Exception as e:
#                 st.error(f"🚫 Email failed: {str(e)}")
#                 st.info("🔧 Use the test app (app2.py) to verify your email settings")
                
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
#                             subject = f"📢 Price Alert for {product_name} on {platform}"
#                             body = f"⚠️ The price of {product_name} on {platform} has changed from ₹{stored_price:.2f} to ₹{price:.2f}."
#                             email_sender.send_email(recipient_email, subject, body)
#                         db_manager.insert_price(product_name, platform, price)
#                 else:
#                     st.error("🚫 No price information found for the product.")
#                     st.info("""
#                     Try these tips:
#                     - Be more specific with your search query  
#                     - Include brand name and model number  
#                     - Check if the product is available in India  
#                     - Try a different product  
#                     """)
#             else:
#                 st.warning("⚠️ Gemini API key not configured.")


# import streamlit as st
# import os
# from dotenv import load_dotenv
# from utils.web_search import search_product_prices
# from utils.database_manager import DatabaseManager
# from utils.email_sender import EmailSender

# # Load environment variables
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# SENDER_EMAIL = os.getenv("SENDER_EMAIL")
# SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
# RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# # Initialize database and email sender
# db_manager = DatabaseManager("product_prices.db")
# email_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)

# # Set UI theme
# st.set_page_config(page_title="Price Tracker Bot", page_icon="💰", layout="wide")

# # Sidebar Navigation
# st.sidebar.title("⚙️ Navigation")
# page = st.sidebar.radio("Go to", ["🏠 Home", "💰 Price Tracker", "ℹ️ About"])

# # Home Page
# if page == "🏠 Home":
#     st.title("🏠 Welcome to the Price Tracker Chatbot!")
#     st.write("""
#     This web application allows users to track and compare product prices from different e-commerce platforms.  
#     🛒 **How It Works:**  
#     - Enter the name of a product, and the bot will fetch its prices from multiple sources.  
#     - Stay updated with price drops through **email notifications**.  
#     - Make smarter shopping decisions with real-time price tracking.  

#     Start searching for your favorite products and save money today! 💰  
#     """)
#     st.image("https://source.unsplash.com/800x300/?shopping,ecommerce", use_container_width=True)

# # Price Tracker Page
# elif page == "💰 Price Tracker":
#     st.title("💰 Product Price Tracker Chatbot")

#     # Sidebar Configuration
#     st.sidebar.subheader("🔔 Get notified when the price drops!")
#     recipient_email = st.sidebar.text_input("📩 Your Email for Notifications", RECIPIENT_EMAIL)

#     # User Guide
#     st.markdown("""
#     ### 🛒 How to Get the Best Results:
#     ✅ Be **specific** with your product search (include brand, model number, etc.)  
#     ✅ For **electronics**, mention storage, color, and model  
#     ✅ For **clothing**, mention size, color, and brand  
#     """)

#     # Search Input
#     product_query = st.text_input("🔍 Enter the product you want to search for:", placeholder="e.g., iPhone 15 Pro Max 256GB Black")

#     # Price Search Button
#     if st.button("🔍 Search Prices"):
#         if not product_query:
#             st.warning("⚠️ Please enter a product to search for.")
#         else:
#             with st.spinner(f"Searching the web for prices of **{product_query}**..."):
#                 st.subheader(f"🔎 Searching for: {product_query}")
#                 try:
#                     results = search_product_prices(product_query, GEMINI_API_KEY)

#                     if not results:
#                         st.error("🚫 No results found. Try a different product.")
#                     else:
#                         st.success(f"✅ Found {len(results)} price listings!")
#                         st.balloons()
#                         st.subheader("📊 Price Comparison Results")
#                         st.table(results)

#                 except Exception as e:
#                     st.error(f"⚠️ An error occurred: {str(e)}")

# # About Page
# elif page == "ℹ️ About":
#     st.title("ℹ️ About the Price Tracker Chatbot")
#     st.write("""
#     The **Price Tracker Chatbot** is a web-based tool designed to help users find the best deals on products.  
#     It uses AI-powered web scraping to retrieve price information from multiple online stores and displays it in an easy-to-read format.

#     ### 🌟 Features:
#     - **Real-time price tracking** using web search.  
#     - **Email notifications** for price drops.  
#     - **Simple and intuitive interface** for quick searches.  

#     This project is built using **Streamlit, Python, and the Gemini API**, making it an efficient and user-friendly price tracking solution.  

#     🚀 Save money and shop smarter with the **Price Tracker Chatbot**!  
#     """)
#     st.image("https://source.unsplash.com/800x300/?discount,shopping", use_container_width=True)


# import streamlit as st
# import os
# from dotenv import load_dotenv
# from utils.web_search import search_product_prices
# from utils.database_manager import DatabaseManager
# from utils.email_sender import EmailSender

# # Load environment variables
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# SENDER_EMAIL = os.getenv("SENDER_EMAIL")
# SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
# RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# # Initialize database and email sender
# db_manager = DatabaseManager("product_prices.db")
# email_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)

# # Set UI theme
# st.set_page_config(page_title="Price Tracker Bot", page_icon="💰", layout="wide")

# # Initialize session state for chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "assistant", "content": "👋 Hi! I'm your Price Tracker Bot. Just type a product name (e.g., 'iPhone 13') to get prices, or say 'about' for more info! 💰"}
#     ]

# # Sidebar for email notifications
# st.sidebar.title("⚙️ Settings")
# st.sidebar.subheader("🔔 Get notified when the price drops!")
# recipient_email = st.sidebar.text_input("📩 Your Email for Notifications", RECIPIENT_EMAIL or "", key="email_input")
# st.sidebar.write("ℹ️ Enter your email to receive price drop alerts!")

# # Main chat interface
# st.title("💬 Price Tracker Chatbot")
# st.write("Chat with me to track product prices in real-time!")

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Chat input
# user_input = st.chat_input("Type your message here...")

# # Process user input
# if user_input:
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Bot response logic
#     with st.chat_message("assistant"):
#         response = ""
#         user_input_lower = user_input.lower().strip()

#         # Check for specific commands first
#         if user_input_lower == "about":
#             response = """
#             ℹ️ I’m the **Price Tracker Chatbot**! I help you find the best deals on products by searching the web.  
#             - **How I work**: Just tell me a product name (e.g., 'iPhone 13'), and I’ll fetch prices from online stores.  
#             - **Features**: Real-time price tracking and email alerts for price drops.  
#             Built with ❤️ using Streamlit, Python, and the Gemini API.  
#             Let’s save you some money—ask me anything! 💰
#             """
#         elif user_input_lower == "track this":
#             if not recipient_email:
#                 response = "⚠️ Please enter your email in the sidebar so I can notify you about price drops!"
#             else:
#                 response = f"🔔 Great! I’ll notify you at {recipient_email} when the price drops. Anything else I can help with?"
#                 # Add logic here to save the last searched product to the database for tracking
#         else:
#             # Assume input is a product name
#             product_query = user_input.strip()
#             with st.spinner(f"Searching the web for prices of **{product_query}**..."):
#                 try:
#                     results = search_product_prices(product_query, GEMINI_API_KEY)
#                     if not results:
#                         response = f"🚫 No results found for '{product_query}'. Try something else!"
#                     else:
#                         response = f"✅ Found {len(results)} price listings for '{product_query}'!\n\nHere’s what I found:\n\n"
#                         for i, result in enumerate(results, 1):
#                             response += f"{i}. **{result.get('Product', 'Product')}**: {result.get('Price', 'N/A')} - [{result.get('Platform', 'Source')}]"
#                             # Note: No 'link' key in your data, so skipping the link part
#                             response += "\n"
#                         response += "\nWould you like me to track this for you? Just say 'Track this'!"
#                 except Exception as e:
#                     response = f"⚠️ Oops! Something went wrong: {str(e)}. Try again?"

#         # Add bot response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": response})
#         st.markdown(response)

# # Additional guidance in the sidebar
# with st.sidebar:
#     st.markdown("""
#     ### 🛒 Tips for Best Results:
#     ✅ Be **specific** (e.g., brand, model, size)  
#     ✅ For **electronics**: Include storage, color, etc.  
#     ✅ For **clothing**: Mention size, color, brand  
#     """)



import streamlit as st
import os
import json
from dotenv import load_dotenv
from utils.web_search import search_product_prices
from utils.database_manager import DatabaseManager
from utils.email_sender import EmailSender

# Set page config FIRST
st.set_page_config(page_title="Price Tracker Bot", page_icon="💰", layout="wide", initial_sidebar_state="expanded")

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Initialize database and email sender
db_manager = DatabaseManager("product_prices.db")
email_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD)

# Custom CSS for Netflix-inspired theme with flexbox for chat alignment
st.markdown("""
    <style>
    /* Main app background */
    .main {
        background-color: #141414; /* Netflix black */
        padding: 20px;
        min-height: 100vh;
    }
    /* Chat container */
    .chat-container {
        background-color: #1c1c1c; /* Slightly lighter black for contrast */
        border-radius: 8px;
        padding: 15px;
        max-height: 600px;
        overflow-y: auto;
        border: 1px solid #333;
        display: flex;          /* Flex container for alignment */
        flex-direction: column; /* Stack messages vertically */
    }
    /* User message */
    .chat-message-user {
        background-color: #333; /* Netflix red */
        color: white;
        border-radius: 8px;
        padding: 10px;
        margin: 5px 0;
        max-width: 70%;
        align-self: flex-end;   /* Align user messages to the right */
        font-size: 14px;
    }
    /* Assistant message */
    .chat-message-assistant {
        background-color: #333; /* Dark gray for assistant messages */
        color: #fff;
        border-radius: 8px;
        padding: 10px;
        margin: 5px 0;
        max-width: 70%;
        align-self: flex-start; /* Align AI messages to the left */
        font-size: 14px;
    }
    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #1c1c1c;
        padding: 15px;
        border-right: 1px solid #333;
    }
    /* Text input */
    .stTextInput>div>input {
        background-color: #333;
        color: #fff;
        border: 1px solid #E50914;
        border-radius: 5px;
    }
    /* Buttons */
    .stButton>button {
        background-color: #ffffff;
        color: white;
        border-radius: 5px;
        padding: 8px 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #f40612;
    }
    /* Title and subtitle */
    .title {
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .subtitle {
        color: #b3b3b3;
        font-size: 16px;
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* About box */
    .about-box {
        background-color: #1c1c1c;
        border-left: 4px solid #E50914;
        padding: 15px;
        border-radius: 5px;
        color: #fff;
        font-size: 14px;
        line-height: 1.6;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Sidebar text */
    .sidebar h2, .sidebar h4 {
        color: #E50914;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sidebar p, .sidebar div {
        color: #b3b3b3;
        font-size: 14px;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Remove default Streamlit styling */
    .stApp {
        background-color: #141414;
    }
    header {
        background-color: #141414 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for chat history if not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "👋 Hi! I'm your Price Tracker Bot. Type a product name (e.g., 'Nike shoes' or 'Pen') to get prices.💰"}
    ]

# Main chat interface
st.markdown('<div class="title">📦 Price Tracker Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Track prices in real-time or get shopping insights!</div>', unsafe_allow_html=True)

# Chat container
chat_container = st.container()
with chat_container:
    # Build the entire chat HTML in one string
    chat_html = '<div class="chat-container">'
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            chat_html += f'<div class="chat-message-user">{message["content"]}</div>'
        else:
            chat_html += f'<div class="chat-message-assistant">{message["content"]}</div>'
    chat_html += '</div>'
    # Render the chat HTML
    st.markdown(chat_html, unsafe_allow_html=True)

# Chat input at the bottom
user_input = st.chat_input("Type your message here...", key="chat_input")

# Sidebar for email notifications, tips, and About Me
with st.sidebar:
    st.markdown('<h2>⚙️ Settings</h2>', unsafe_allow_html=True)
    st.markdown('<h4>🔔 Price Drop Alerts</h4>', unsafe_allow_html=True)
    recipient_email = st.text_input("📩 Your Email", value=RECIPIENT_EMAIL or "", key="email_input", placeholder="Enter your email")
    st.markdown('<p>ℹ️ Get notified when prices drop!</p>', unsafe_allow_html=True)
    
    st.markdown('<h4>🛒 Tips for Best Results</h4>', unsafe_allow_html=True)
    st.markdown("""
        <div>
        ✅ Be <b>specific</b> (e.g., brand, model, size)  
        ✅ For <b>electronics</b>: Include storage, color.  
        ✅ For <b>pens</b>: Mention brand, type, etc.  
        </div>
    """, unsafe_allow_html=True)

    # Add About Me section
    st.markdown('<h4>ℹ️ About Me</h4>', unsafe_allow_html=True)
    st.markdown("""
        <div class="about-box">
        Hi, I'm Akash Choudhury, the creator of this Price Tracker Chatbot. 
        I'm a Software Developer with a passion for building tools that save time and money. 
        Feel free to reach out at akashchoudhury9368@gmail.com.
        </div>
    """, unsafe_allow_html=True)

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # Bot response logic
    response = ""
    user_input_lower = user_input.lower().strip()
    words = user_input_lower.split()
    is_json_requested = "json" in words

    if user_input_lower == "about":
        response = """
        <div class="about-box">
        👋 Welcome to the <b>Price Tracker Chatbot</b>! I’m here to help you snag the best deals by searching the web. Tell me a product name (e.g., 'Nike shoes' or 'Pen'), and I’ll fetch real-time prices from online stores. Or share your shopping adventures, and I’ll provide handy insights! With features like price tracking and email alerts for drops, I’ve got your back. Built with love using Streamlit, Python, and the Gemini API—let’s save some cash together! 💰
        </div>
        """
    elif user_input_lower == "track this":
        if not recipient_email:
            response = "⚠️ Please enter your email in the sidebar to enable price drop notifications!"
        else:
            response = f"🔔 Awesome! I’ll notify you at <b>{recipient_email}</b> when prices drop. Anything else I can assist with?"
    else:
        product_keywords = ["iphone", "shoes", "laptop", "tv", "headphones", "watch", "camera", "pen"]
        insight_phrases = ["insights", "went outside", "shop", "saw", "checked out"]
        detected_product = next((keyword for keyword in product_keywords if keyword in user_input_lower), None)

        if detected_product and any(phrase in user_input_lower for phrase in insight_phrases):
            if detected_product == "iphone":
                response = """
                👋 Cool, you went to check out an iPhone in a shop today! Since you didn’t specify a model, here are some general insights about iPhones in India as of March 27, 2025: Popular models like the iPhone 13, 14, and 15 are widely available, with the iPhone 16 series being the latest. The iPhone 13 is a great value option, often priced around ₹50,999 on Flipkart or Amazon.in. Pricing varies by storage and retailer—for instance, the iPhone 14 (128GB) typically costs ₹66,999, while the iPhone 15 starts at ₹79,900. Physical shops might offer slight discounts or EMI plans. Newer models like the iPhone 16 boast the A18 chip, 48MP cameras, and USB-C ports, while older ones like the iPhone 13 still deliver solid performance and iOS updates. <b>Shopping tip:</b> Compare online prices before buying in-store—e-commerce sites often have better deals, especially during sales. Which iPhone did you see? Tell me the model for specific prices or details!
                """
            elif detected_product == "shoes":
                response = """
                👋 Cool, you went to check out shoes in a shop today! Since you didn’t specify a brand or type, here are some general insights about shoes in India as of March 27, 2025: Popular brands like Nike, Adidas, and Puma dominate the casual and sports segments, while local brands like Bata and Liberty offer affordable options. Prices vary widely—casual sneakers from Nike might cost around ₹5,000-₹12,000 on Flipkart or Amazon.in, while premium running shoes can hit ₹15,000 or more. Features like lightweight cushioning, breathable materials, and anti-slip soles are trending, especially in athletic footwear. <b>Shopping tip:</b> Check online platforms for discounts—e-commerce sites often beat shop prices during sales events. What kind of shoes did you see? Tell me the brand or style, and I can give you specific prices or details!
                """
            elif detected_product == "laptop":
                response = """
                👋 Cool, you went to check out a laptop in a shop today! Since you didn’t specify a brand, here are some general insights about laptops in India as of March 27, 2025: Popular brands like Dell, HP, and Lenovo lead the market, with gaming options from ASUS ROG and MSI gaining traction. Prices range widely—an entry-level laptop might cost ₹35,000-₹50,000 on Flipkart or Amazon.in, while high-end models like the MacBook Pro can exceed ₹1,50,000. Features like Intel i5/i7 processors, SSD storage, and 16GB RAM are standard in mid-range models, with 4K displays and powerful GPUs in premium ones. <b>Shopping tip:</b> Look online for combo deals or bank offers—e-commerce sites often undercut shop prices during sales. Which laptop caught your eye? Tell me the brand or model for specific prices or details!
                """
            elif detected_product == "pen":
                response = """
                👋 Cool, you went to check out a pen in a shop today! Since you didn’t specify a brand or type, here are some general insights about pens in India as of March 27, 2025: Popular brands like Parker, Montblanc, and Lamy are favored for premium writing, while affordable options from Reynolds and Cello are widely used. Prices vary—a basic ballpoint pen from Reynolds might cost ₹10-₹50 on Flipkart or Amazon.in, while a luxury fountain pen from Parker can range from ₹1,000 to ₹10,000 or more. Features like smooth ink flow, ergonomic grips, and durable tips are key in everyday pens, with premium models offering craftsmanship and style. <b>Shopping tip:</b> Look online for bulk deals or festive discounts—e-commerce sites often beat local shop prices. What kind of pen did you see? Tell me the brand or type, and I can give you specific prices or details!
                """
        else:
            if len(user_input_lower) < 3 or not any(char.isalpha() for char in user_input_lower):
                response = f"🚫 No results found for '{user_input}'. Please enter a valid product name."
            else:
                product_query = user_input.strip()
                with st.spinner(f"Searching prices for **{product_query}**..."):
                    try:
                        results = search_product_prices(product_query, GEMINI_API_KEY)
                        if not isinstance(results, list) or len(results) == 0:
                            response = f"🚫 No results found for '{product_query}'. Try a different product name or check your spelling."
                        else:
                            if is_json_requested:
                                json_data = {
                                    "query": product_query,
                                    "results_count": len(results),
                                    "listings": [
                                        {
                                            "product": result.get("Product", "Product"),
                                            "price": result.get("Price", "N/A"),
                                            "platform": result.get("Platform", "Source")
                                        } for result in results
                                    ]
                                }
                                response = f"✅ Found {len(results)} price listings for '{product_query}'!\n\nHere’s the JSON:\n```json\n{json.dumps(json_data, indent=2)}\n```"
                            else:
                                response = f"✅ Found {len(results)} price listings for '{product_query}'!\n\nHere’s what I found:\n\n"
                                for i, result in enumerate(results, 1):
                                    response += f"{i}. **{result.get('Product', 'Product')}**: {result.get('Price', 'N/A')} - [{result.get('Platform', 'Source')}]"
                                    response += "\n"
                                response += "\nWould you like me to track this for you? Just say 'Track this'!"
                    except Exception as e:
                        response = f"⚠️ Oops! Something went wrong: {str(e)}. Try again?"

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.rerun()  # Rerun the app to update the chat display