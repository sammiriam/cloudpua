# -*- encoding: utf-8 -*-
""""""
from datetime import datetime

import click

from cloudpua import create_app
from cloudpua.db import Session
from cloudpua.pua import PUA

app = create_app()


@click.group()
def cli():
    """基本命令界面"""
    pass


@cli.command()
def unittest():
    """运行单元测试"""
    import pytest
    pytest.main(["tests"])


@cli.command()
def initdb():
    """创建数据库"""
    from cloudpua.db import DocumentBase
    engine = app.config.get('SQLALCHEMY_ENGINE')
    DocumentBase.metadata.create_all(engine)
    click.echo('Created db.')


@cli.command()
@click.option("--slug", prompt="ID")
@click.option("--title", prompt="标题")
@click.option("--author", prompt="作者")
@click.option("--description", prompt="描述")
def newpua(slug, title, author, description):
    """新建PUA条目"""
    print("一行一句，首字符<表示发出，>表示收到，空行表示结束")
    chat = []
    while True:
        line = input("请输入聊天内容: ")
        if line == "" or line[0] not in "<>":
            break
        else:
            chat.append((line[0] == "<", line[1:]))
    pua = PUA(slug=slug, title=title, author=author, description=description, view=0, date=datetime.now())
    pua.chat = chat
    session = Session()
    session.add(pua)
    session.commit()


@cli.command()
def listpua():
    """枚举全部的PUA"""
    pass  # TODO implement listpua


@cli.command()
@click.option("--host", type=str, default="127.0.0.1")
@click.option("--port", type=int, default=8080)
@click.option("--debug", type=bool, default=True)
@click.option("--config", default=None)
def runserver(host, port, debug, config):
    """
    运行服务器的基本命令

    :param host: 绑定的IP地址
    :param port: 绑定的端口号
    :param debug: 是否启用Debug模式
    :param config: 配置文件路径
    :return:
    """
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    cli()
