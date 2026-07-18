#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project  : auto_web_20251210
@File     : test_baidu.py
@Author   : 刘金刚
@email    : 234234234@qq.com 
@Date     : 2026/7/18 14:58
"""
from selenium import webdriver


class TestBaidu:
    def test_baidu(self):
        driver = webdriver.Edge()
        driver.get("https://www.baidu.com")