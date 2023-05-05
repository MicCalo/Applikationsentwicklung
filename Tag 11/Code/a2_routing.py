#!/usr/bin/env python3
# coding: utf8

from flask import Flask
app = Flask(__name__)

# 'index' routing rule (bare address)
@app.route('/')
def hello_world():
   return 'Hello World!'

# routing rule for addresses ending with /demo1
@app.route('/demo1')
def hello_world_html():
   return '<html><head><title>Hello World with HTML</title></head><body><h1>Hello World</h1>&#127793;Guten Tag! &#127808;</body></html>'


# routing rule for addresses ending with /demo1/*
@app.route('/demo1/<name>')
def hello_world_html_with_name(name: str):
   return f'<html><head><title>Hello World with HTML and Name</title></head><body><h1>Hallo World</h1>&#127793;Guten Tag <b>{name}</b>&#127808;</body></html>'


# routing rule for addresses ending with /demo2[*]
@app.route('/demo2')
@app.route('/demo2/')
@app.route('/demo2/<name>')
@app.route('/demo2/<name>/')
def hello_world_css(name: str=''):
   return f'<html><head><title>Hello World with HTML and CSS</title><link rel="stylesheet" href="/static/stylesheet.css" /></head><body><h1>Hallo World</h1>&#127793;Guten Tag <b>{name}</b>&#127808;</body></html>'



if __name__ == '__main__':
   app.run()