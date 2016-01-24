#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import unittest
from ..cmd_parser import cmd_parser


class CmdParseTest(unittest.TestCase):
    def setUp(self):
        super(CmdParseTest, self).setUp()

    def tearDown(self):
        super(CmdParseTest, self).tearDown()

    def test_cmd_name(self):
        field, cmd_list = cmd_parser("cmd_name")
        # print field, cmd_list
        self.assertEquals(field, "cmd_name", msg=u" expect cmd_name='',this is '%s'" % field)

    def test_cmd_list(self):
        field, cmd_list = cmd_parser(r'-i test%s123123 -n -l 1,5 -r "mo\" bi" -t "-int|+float" -w "haha,your got it"')
        # print field, cmd_list
        self.assertEquals(cmd_list, {'i': 'test%s123123', 'l': '1,5', 'n': '', 'r': 'mo\\" bi', 't': '-int|+float',
                                     'w': 'haha,your got it'}, msg=u"cmd_list error")

    def test_all(self):
        field, cmd_list = cmd_parser(
            r'test_field_name -i test%s123123 -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        # print field, cmd_list
        self.assertEquals(field, "test_field_name", msg=u"cmd_name error")
        self.assertEquals(cmd_list, {'i': 'test%s123123', 'l': '1,5', 'n': '', 'r': 'mo\\"bi', 't': '-int|+float',
                                     'w': 'haha,your got it'}, msg=u"cmd_list error")

    def test_qoute(self):
        # TODO 测试所有值都加引号
        field, cmd_list = cmd_parser(
            r'cmd_name -i "test%s123\"123" -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        # 测试所有值都不加引号

        # 测试引号不闭合


if __name__ == '__main__':
    unittest.main()
