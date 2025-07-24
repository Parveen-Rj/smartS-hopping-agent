# from litellm import completion
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def main():
#     api_key = os.getenv("GEMINI_API_KEY")
#      # 👇 User se sawal lena
#     user_question = input("Apna sawal poochhein: ")



#     response = completion(
#         model="gemini/gemini-2.0-flash",
#         messages=[
#             {
#                 "role": "user",
#                 "content":"user_question"
#             }
#         ],
#     )
#     print("Jawab:",response['choices'][0]['message']['content'])
# if __name__ == "__main__":
#     main()

# 


import streamlit as st
from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(page_title="🛍️ Smart Shopping Agent", page_icon="🛒")

st.title("🛒 Smart Shopping Agent")
st.markdown("Ask about **products, prices, or shopping suggestions**:")

user_input = st.text_input("🔍 What are you looking for?", placeholder="e.g. School shoes under 5000")

if st.button("🧠 Find Products"):
    if user_input.strip() != "":
        with st.spinner("Finding the best products for you..."):
            try:
                response = completion(
                    model="gemini/gemini-2.0-flash",
                    messages=[{"role": "user", "content": f"""
Act like a smart shopping assistant. 
User query: "{user_input}"

Reply in this format:

If possible show 3 products with:
- **Name**
- 💰 Price
- 📝 Short Description
- 🖼️ Image (if available, use markdown ![]())

If not found, say "Sorry, nothing matched your request."
"""}]
                )

                answer = response['choices'][0]['message']['content']
                st.markdown(answer)

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a product query.")
