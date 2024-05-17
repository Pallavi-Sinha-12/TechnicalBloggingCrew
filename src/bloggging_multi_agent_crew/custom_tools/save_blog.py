from crewai_tools import tool
import os

@tool("save_blog")
def save_blog(title, content):
    """Save a blog post to a markdown file."""
    os.makedirs("blogs", exist_ok=True)
    file_name = title.replace(" ", "_").lower() + ".md"
    folder_path = "blogs/"
    file_path = folder_path + file_name
    with open(file_path, "w") as file:
        file.write(content)
    return file_path