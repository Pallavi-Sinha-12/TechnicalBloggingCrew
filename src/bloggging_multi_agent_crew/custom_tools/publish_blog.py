from crewai_tools import tool
import requests
import json


@tool("publish_blog")
def publish_blog(title, content):

    """Publish the blog to the blogging platform."""

    api_url = "http://localhost:8000/publish/blog/"
    data = {"title": title, "content": json.dumps(content)}
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        return "Blog published successfully"
    else:
        return "Failed to publish blog"