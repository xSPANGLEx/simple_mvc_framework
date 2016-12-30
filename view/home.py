#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
import sys

class home:

    def __init__(self):
        self.text="homeView"

    def view(self):
        data = \
"""<html>
<head>
    <title>test</title>
</head>
<body>
    <form action=/ method="POST">
        <input type="text" name="test">
        <input type="submit" value="submit">
    </form>
</body>
</html>"""
        return data
