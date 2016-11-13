# -*- encoding: utf-8 -*-
""""""

import click

from cloudpua import create_app

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
    from cloudpua.db import DocumentBase, engine
    DocumentBase.metadata.create_all(engine)
    click.echo('Created db.')


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
