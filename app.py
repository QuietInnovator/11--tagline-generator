import streamlit as st
from input_handler import get_business_info, generate_tagline

def main():
    st.title("Business Tagline Generator")
    st.write("Generate a compelling tagline for your business using AI.")

    # Get business information
    business_info = get_business_info()

    # Generate tagline button
    if st.button("Generate Tagline"):
        if not all([business_info['name'], business_info['industry'], business_info['description']]):
            st.warning("Please fill in all required fields (Business Name, Industry, and Description)")
        else:
            with st.spinner("Generating your tagline..."):
                tagline = generate_tagline(business_info)
                if tagline:
                    st.success("Here's your generated tagline:")
                    st.markdown(f"## {tagline}")
                    
                    # Add a copy button
                    st.button("Copy Tagline", 
                             on_click=lambda: st.write(f"Tagline copied to clipboard: {tagline}"))

if __name__ == "__main__":
    main() 