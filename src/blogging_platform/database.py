from models import Blog

class Database:
    def __init__(self):
        self.blogs = []

    def add_blog(self, blog: Blog):
        self.blogs.append(blog)
        return True

    def get_blogs(self):
        return self.blogs

db = Database()