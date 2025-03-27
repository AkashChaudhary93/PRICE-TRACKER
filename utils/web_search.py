import google.generativeai as genai
import json
import re

def search_product_prices(query, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    You are a shopping assistant. Search the web for current prices of: {query} in India.
    
    Check major e-commerce websites like Amazon.in, Flipkart, and other Indian retailers.
    Include specific model numbers and variants if available.
    
    Return ONLY a JSON array with the following format:
    [
        {{
            "Product": "Exact product name",
            "Platform": "Website name",
            "Price": "Price with ₹ symbol"
        }}
    ]
    
    If you find multiple listings, include all of them.
    """

    try:
        response = model.generate_content(prompt)
        text_response = response.text
        
        # Debug output
        print(f"Raw response for '{query}':\n{text_response}")
        
        # Extract JSON if wrapped in code blocks
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text_response)
        if json_match:
            text_response = json_match.group(1).strip()
        
        # Try to clean up the response if it's not valid JSON
        text_response = text_response.replace('```', '').strip()
        
        try:
            results = json.loads(text_response)
            if isinstance(results, list):
                return results
            else:
                print("Warning: Response was not a list")
                return []
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON response")
            return []

    except Exception as e:
        print(f"Error during web search: {e}")
        return []