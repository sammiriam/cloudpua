# -*- encoding: utf-8 -*-
"""This module test if the py.test environment correctly setup.
"""


def test_test_environments():
    assert True


def test_import_package():
    from cloudpua import create_app
    create_app()
