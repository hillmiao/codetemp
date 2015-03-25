"""
"""
from config import db

def get_category():
    return db.query("SELECT * FROM category;")
