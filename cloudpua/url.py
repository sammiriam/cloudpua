# -*- encoding: utf-8 -*-
"""This module handles web pages
"""
from datetime import datetime

import humanize
from flask import Blueprint, abort, jsonify, render_template, request, url_for
from flask import json

from cloudpua.db import Session
from .pua import PUA, pua_search

url_blueprint = Blueprint("url_blueprint", __name__, template_folder="templates", static_folder="static")


@url_blueprint.route('/', methods=['GET'])
def home_page():
    """主页"""
    return render_template("index.html")


@url_blueprint.route('/pua/<string:slug>', methods=['GET', 'POST'])
def pua_view(slug):
    """PUA详情页面"""
    if request.method == 'GET':
        session = Session()
        pua = session.query(PUA).filter_by(slug=slug).first()
        if pua is None:
            abort(404)
        return render_template('pua_detail.html', pua=pua, chat=pua.chat)
    else:
        # 创建新的PUA
        slug = request.form.get('slug')
        title = request.form.get('title')
        description = request.form.get('description')
        author = request.form.get('author')
        data = json.loads(request.form.get('data'))
        pua = PUA(
            slug=slug,
            title=title,
            description=description,
            author=author,
            date=datetime.now(),
            view=0
        )
        parsed_data = list(map(
            lambda x: (x['me'], x['content']),
            data
        ))
        pua.chat = parsed_data
        session = Session()
        session.add(pua)
        session.commit()
        return jsonify(redirect=url_for('url_blueprint.pua_view', slug=slug))


@url_blueprint.route('/plist', methods=["GET"])
def pua_list():
    """PUA列表与搜索页面"""
    kw = request.args.get('q', default='')
    result = pua_search(kw)
    return render_template("pua_list.html", result=result, kw=kw)


@url_blueprint.route('/create', methods=['GET'])
def pua_create():
    """创建PUA页面"""
    return render_template("create_pua.html")


@url_blueprint.route('/about', methods=['GET'])
def about():
    """关于页面"""
    return render_template('about.html')


@url_blueprint.app_template_filter('datetime')
def _jinja2_datetime_filter(date: datetime, fmt=None):
    return humanize.naturaltime(date)
    #return date.strftime("%Y-%m-%d %H:%M:%S")
