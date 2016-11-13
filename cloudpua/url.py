# -*- encoding: utf-8 -*-
"""This module handles web pages
"""

from flask import Blueprint, request, render_template

url_blueprint = Blueprint("url_blueprint", __name__, template_folder="templates", static_folder="static")


@url_blueprint.route('/', methods=['GET'])
def home_page():
    """主页"""
    return render_template("index.html")


@url_blueprint.route('/pua/<string:slug>', methods=['GET', 'POST'])
def pua_view(slug):
    """PUA详情页面"""
    if request.method == 'GET':
        return "you're looking for pua {}".format(slug)
    else:
        return "You're posting new pua"


@url_blueprint.route('/plist', methods=["GET"])
def pua_list():
    """PUA列表与搜索页面"""
    return render_template("pua_list.html")


@url_blueprint.route('/create', methods=['GET'])
def pua_create():
    """创建PUA页面"""
    return render_template("create_pua.html")
