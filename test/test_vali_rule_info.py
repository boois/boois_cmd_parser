#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import unittest
from ..vali_rule_info import ValiRuleInfo


class ValiRuleInfoTest(unittest.TestCase):
    def setUp(self):
        super(ValiRuleInfoTest, self).setUp()

    def tearDown(self):
        super(ValiRuleInfoTest, self).tearDown()

    def test_field(self):
        # 带field的模式
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.filed, "cmd_name", msg="ValiRuleInfo.field error")
        self.assertEquals(info.has_field, True, msg="ValiRuleInfo.has_field error")
        # 未带field的模式
        info = ValiRuleInfo(r'-i test%s123123 -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.filed, "", msg="ValiRuleInfo.field error")
        self.assertEquals(info.has_field, False, msg="ValiRuleInfo.has_field error")
        # 仅有field的模式
        info = ValiRuleInfo(r'cmd_name')
        self.assertEquals(info.filed, "cmd_name", msg="ValiRuleInfo.field error")
        self.assertEquals(info.has_field, True, msg="ValiRuleInfo.has_field error")
        # 什么也没有的模式
        info = ValiRuleInfo(r'')
        self.assertEquals(info.filed, "", msg="ValiRuleInfo.field error")
        self.assertEquals(info.has_field, False, msg="ValiRuleInfo.has_field error")

    def test_i(self):
        # 测试i有值的情况
        info = ValiRuleInfo(
            r'cmd_name -i "test%s123\"123" -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.info, 'test%s123\\"123', msg="ValiRuleInfo.info error")
        self.assertEquals(info.has_info, True, msg="ValiRuleInfo.has_info error")
        # 测试i 无值的情况
        info = ValiRuleInfo(r'cmd_name -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.info, "", msg="ValiRuleInfo.info error")
        self.assertEquals(info.has_info, False, msg="ValiRuleInfo.has_info error")

    def test_w(self):
        # 测试w有值的情况
        info = ValiRuleInfo(
            r'cmd_name -i "test%s123\"123" -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        # print info.warning
        self.assertEquals(info.warning, 'haha,your got it', msg="ValiRuleInfo.warning error")
        self.assertEquals(info.has_warning, True, msg="ValiRuleInfo.has_warning error")
        # 测试w无值的情况
        info = ValiRuleInfo(r'cmd_name -n -l 1,5 -r "mo\"bi" -t "-int|+float"')
        self.assertEquals(info.warning, '', msg="ValiRuleInfo.warning error")
        self.assertEquals(info.has_warning, False, msg="ValiRuleInfo.has_warning error")

    def test_n(self):
        # 测试 有n的情况
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.required, True, msg="ValiRuleInfo.required error")
        self.assertEquals(info.has_required, True, msg="ValiRuleInfo.has_required error")

        # 测试 有n,后面还带着值的情况
        info = ValiRuleInfo(
            r'cmd_name -i test%s123123 -n 123 -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.required, True, msg="ValiRuleInfo.required error")

        # 测试 无n的情况
        info = ValiRuleInfo(r'cmd_name -i "test%s123\"123" -l 1,5 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.required, False, msg="ValiRuleInfo.info error")
        self.assertEquals(info.has_required, False, msg="ValiRuleInfo.has_required error")

    def test_t(self):
        # 测试 未输入的情况:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r "mo\"bi" -w "haha,your got it"')
        self.assertEquals(info.type, 0, msg="ValiRuleInfo.type error")
        self.assertEquals(info.has_type, False, msg="ValiRuleInfo.has_type error")
        # 测试 无值的情况:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -t -r "mo\"bi" -w "haha,your got it"')
        self.assertEquals(info.type, 0, msg="ValiRuleInfo.type error")
        self.assertEquals(info.has_type, True, msg="ValiRuleInfo.has_type error")
        # 测试 1个值的情况:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -t float -r "mo\"bi" -w "haha,your got it"')
        self.assertEquals(info.type, ValiRuleInfo.FLOAT, msg="ValiRuleInfo.type error")
        self.assertEquals(info.has_type, True, msg="ValiRuleInfo.has_type error")
        # 测试 所有可选值覆盖情况:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -t float -r "mo\"bi" -w "haha,your got it"')
        self.assertEquals(info.type, ValiRuleInfo.FLOAT, msg="ValiRuleInfo.type error")
        # 测试 小写输入情况:
        info = ValiRuleInfo(
            r'cmd_name -i test%s123123 -n -t guid|str|int|p_int|n_int|float|p_float|n_float|bool|int_list|str_list|dict|json|guid_list -r "mo\"bi" -w "haha,your got it"')

        all_type = (ValiRuleInfo.INT |
                    ValiRuleInfo.P_INT |
                    ValiRuleInfo.N_INT |
                    ValiRuleInfo.FLOAT |
                    ValiRuleInfo.P_FLOAT |
                    ValiRuleInfo.N_FLOAT |
                    ValiRuleInfo.BOOL |
                    ValiRuleInfo.INT_LIST |
                    ValiRuleInfo.STR_LIST |
                    ValiRuleInfo.DICT |
                    ValiRuleInfo.JSON |
                    ValiRuleInfo.GUID_LIST |
                    ValiRuleInfo.STR |
                    ValiRuleInfo.GUID)
        self.assertEquals(info.type, all_type, msg="ValiRuleInfo.type error %s|%s" % (info.type, all_type))
        # 测试 正负号缩写输入情况:
        info = ValiRuleInfo(
            r'cmd_name -i test%s123123 -n -t "guid|str|int|+int|-int|float|+float|-float|bool|int_list|str_list|dict|json|guid_list" -r "mo\"bi" -w "haha,your got it"')
        self.assertEquals(info.type, all_type, msg="ValiRuleInfo.type error %s|%s" % (info.type, all_type))
        # 测试 奇怪的各种值的输入情况:
        info = ValiRuleInfo(
            r'cmd_name -i test%s123123 -n -t "%|1|b|&|.|+123|-vvv|-----+++=!@#$%^&*()_+.,/.;" -r "mo\"bi" -w "haha,your got it"')
        self.assertEquals(info.type, 0, msg="ValiRuleInfo.type error %s|%s" % (info.type, all_type))
        # 测试 TYPE_LIST 中的所有值是否全部为大写的常量格式
        for type in ValiRuleInfo.TYPE_LIST:
            self.assertEquals(type.isupper(), True, msg="type must be upper")
        # 测试 TYPE_LIST 中的所有值是否都可以在类属性中取到,并且对应的值是类属性的值
        for type in ValiRuleInfo.TYPE_LIST:
            self.assertEquals(ValiRuleInfo.TYPE_LIST[type], ValiRuleInfo.__getattribute__(ValiRuleInfo, type))
        # 测试 TYPE_LIST 中的所有值是否有重复的值
        self.assertEquals(len(ValiRuleInfo.TYPE_LIST),
                          len(dict((v, k) for k, v in ValiRuleInfo.TYPE_LIST.iteritems())),
                          msg="TYPE_LIST duplicate!")

    def test_l(self):
        # 测试 has_len:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.has_len, False, msg="ValiRuleInfo.has_len error")
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.has_len, True, msg="ValiRuleInfo.has_len error")
        # 测试l根本没输入的情况
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, -1), msg="ValiRuleInfo.len error")
        # 测试l没有值的情况
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, -1), msg="ValiRuleInfo.len error")
        # 测试l正常有值的情况 1,2
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l 4,24 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (4, 24), msg="ValiRuleInfo.len error")
        # 测试l带负号的情况
        info = ValiRuleInfo(
            r'cmd_name -i test%s123123 -n -l "-4,-24" -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-4, -24), msg="ValiRuleInfo.len error")
        # 测试l仅输入前一个数字 1, or 1
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l "-4" -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-4, -1), msg="ValiRuleInfo.len error")
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l "-4," -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-4, -1), msg="ValiRuleInfo.len error")
        # 测试l仅输入后一个数字 ,1
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l ",12" -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, 12), msg="ValiRuleInfo.len error")
        # 测试l 使用非数字: a,b or a,1 or 1,a or ,a or a
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l a,b -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, -1), msg="ValiRuleInfo.len error")
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l a,1 -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, 1), msg="ValiRuleInfo.len error")
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l 1,a -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (1, -1), msg="ValiRuleInfo.len error")
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l a -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, -1), msg="ValiRuleInfo.len error")
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l ,a -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, -1), msg="ValiRuleInfo.len error")
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -l a -r "mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.len, (-1, -1), msg="ValiRuleInfo.len error")

    def test_r(self):
        # 先测试无输入:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.regx, "", msg="ValiRuleInfo.regx error")
        self.assertEquals(info.has_regx, False, msg="ValiRuleInfo.has_regx error")
        # 先测试无值:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.regx, "", msg="ValiRuleInfo.regx error")
        self.assertEquals(info.has_regx, True, msg="ValiRuleInfo.has_regx error")
        # 测试原始正则,以/开头的都是原始正则:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r "/mo\"bi" -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.regx, '/mo\\"bi', msg="ValiRuleInfo.type error")
        # 测试所有正则:
        for regx in ValiRuleInfo.REGX_TMP:
            info = ValiRuleInfo(
                r'cmd_name -i test%s123123 -n -r "{regx}" -t "-int|+float" -w "haha,your got it"'.format(regx=regx))
            self.assertEquals(info.regx, ValiRuleInfo.REGX_TMP[regx], msg="ValiRuleInfo.type error")

    def test_v(self):
        # 先测试无输入:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -t "-int|+float" -w "haha,your got it"')
        self.assertEquals(info.values, [], msg="ValiRuleInfo.values error")
        self.assertEquals(info.has_values, False, msg="ValiRuleInfo.has_values error")
        # 先测试无值:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r -t "-int|+float" -w "haha,your got it" -v')
        self.assertEquals(info.values, [], msg="ValiRuleInfo.values error")
        self.assertEquals(info.has_values, True, msg="ValiRuleInfo.has_values error")
        # 测试正常值:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r "/mo\"bi" -t "-int|+float" -v "1|2|3"')
        self.assertEquals(info.values, ["1", "2", "3"], msg="ValiRuleInfo.values error")
        # 测试中文:
        info = ValiRuleInfo(r'cmd_name -i test%s123123 -n -r "/mo\"bi" -t "-int|+float" -v "1|我|3"')
        self.assertEquals(info.values, ["1", "我", "3"], msg="ValiRuleInfo.values error")


if __name__ == '__main__':
    unittest.main()
