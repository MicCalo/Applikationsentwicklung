#!/usr/bin/env python3
# coding: utf8

from flask import Flask, render_template, request
from a1_information_block import InformationBlock

app = Flask(__name__)

@app.route('/')
def handle_index():
    request_info = InformationBlock("Request Information dfgdfg", {
        'method': request.method,
        'user_agent': request.user_agent.string,
        'languages': request.accept_languages,
        'encodings': request.accept_encodings,
        'url': request.base_url,
        'client IP': request.remote_addr})


    return render_template('info_table.html.jinja', info = request_info)

@app.route('/svg')
def handle_svg():
    shape = request.args.get('shape') or 'no arg'
    color = request.args.get('color') or 'blue'
    border = request.args.get('border') or 'forestgreen'
    return render_template('solution_svg.html.jinja', shape = shape, color=color, border=border)



if __name__ == '__main__':
    app.run()
