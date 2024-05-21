import streamlit as st
import requests
import json

# Function to fetch blogs from the endpoint
def fetch_blogs():
    response = requests.get("http://127.0.0.1:8000/blogs")
    if response.status_code == 200:
        return response.json()  # Assuming the response is a list of dicts
    else:
        st.error("Failed to fetch blogs")
        return []

# Main function to display the blogs
def main():

    st.title("Blog Posts 📝")

    blogs = fetch_blogs()

    if blogs:
        for blog in blogs:
            # content = json.loads(blog['content'])
            # st.markdown(content)
            with st.expander(blog['title']):
                st.markdown(json.loads(blog['content'])) 

if __name__ == "__main__":
    main()