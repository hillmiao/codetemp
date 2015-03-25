"""
Global config
"""
import web

db = web.database(dbn='mysql', user='root', db='oulu')
render = web.template.render('views')
