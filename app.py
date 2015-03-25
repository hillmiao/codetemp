#!/usr/bin/python
"""
All start from here :)
"""

import web
import routes

app = web.application(routes.urls, globals())

if __name__ == '__main__':
    app.run()
