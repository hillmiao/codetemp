"""
Do it here
"""
import web
from models import category
from config import render

class index:
    def GET(self):
        categories = category.get_category()
        return render.index(categories)
