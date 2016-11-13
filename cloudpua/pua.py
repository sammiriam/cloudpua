# -*- encoding: utf-8 -*-
"""PUA模型层
"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from .db import DocumentBase, Session


class PUA(DocumentBase):
    __tablename__ = "pua"

    slug = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    author = Column(String)
    date = Column(DateTime)
    content = Column(Text)
    view = Column(Integer)

    @property
    def chat(self):
        """返回PUA的聊天记录

        :return 聊天记录的元组列表
        """
        ori = self.content  # type: str
        return list(map(lambda x: (x[0] == '<', x[1:]), ori.split('\n')))

    @chat.setter
    def chat(self, value):
        """设置PUA的聊天记录

        [(True, "Hello!"), (False, "Yes!")]

        元组第一个bool值表示是否是我发出的对话。

        :param value: 聊天记录的元组列表
        """
        assert isinstance(value, list)
        self.content = "\n".join(map(lambda x: "<{}".format(x[1]) if x[0] else ">{}".format(x[1]), value))


class PUATag(DocumentBase):
    __tablename__ = "tags"
    tag = Column(String, primary_key=True)
    pua = Column(String, ForeignKey(PUA.slug), primary_key=True)


def pua_search(kw):
    """根据关键字搜索PUA

    从标签、标题、描述、内容中搜索，返回PUA列表
    """
    # TODO: 现在默认返回全部，修改这个伪实现
    session = Session()
    return session.query(PUA).all()
