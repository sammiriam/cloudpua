# -*- encoding: utf-8 -*-
"""PUA模型层
"""

from sqlalchemy import String, Text, Column, DateTime, Integer

from .db import DocumentBase


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
        ori = self.content.copy()  # type: str
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
