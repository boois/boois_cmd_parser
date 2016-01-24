#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import unittest
from ..vali_rule_chker import ValiRuleChker
from ..vali_rule_info import ValiRuleInfo


class ValiRuleInfoTest(unittest.TestCase):
    def setUp(self):
        super(ValiRuleInfoTest, self).setUp()

    def tearDown(self):
        super(ValiRuleInfoTest, self).tearDown()

    def test_int_chker(self):
        # 不传值
        self.assertEquals(ValiRuleChker.int_chker(""), False, msg="int_chker error,input '' = True? expect False")
        # 整数1
        self.assertEquals(ValiRuleChker.int_chker(1), True, msg="int_chker error,input 1 = False? expect True")
        self.assertEquals(ValiRuleChker.int_chker("1"), True, msg="int_chker error,input '1' = False? expect True")
        self.assertEquals(ValiRuleChker.int_chker(" 1 "), True, msg="int_chker error,input ' 1 ' = False? expect True")
        # 整数0
        self.assertEquals(ValiRuleChker.int_chker(0), True, msg="int_chker error,input 0 = False? expect True")
        self.assertEquals(ValiRuleChker.int_chker("0"), True, msg="int_chker error,input '0' = False? expect True")
        # 负数
        self.assertEquals(ValiRuleChker.int_chker(-1), True, msg="int_chker error,input -1 = False? expect True")
        self.assertEquals(ValiRuleChker.int_chker("-1"), True, msg="int_chker error,input '-1' = False? expect True")
        self.assertEquals(ValiRuleChker.int_chker(" -1 "), True,
                          msg="int_chker error,input ' -1 ' = False? expect True")
        # 非数字
        self.assertEquals(ValiRuleChker.int_chker("a"), False, msg="int_chker error,input 'a' = True? expect False")
        # 小数
        self.assertEquals(ValiRuleChker.int_chker(0.1), False, msg="int_chker error,input 0.1 = True? expect False")
        self.assertEquals(ValiRuleChker.int_chker("0.1"), False, msg="int_chker error,input '0.1' = True? expect False")

    def test_p_int_chker(self):  # 正整数不包含0
        # 不传值
        self.assertEquals(ValiRuleChker.p_int_chker(""), False, msg="p_int_chker error,input '' = True? expect False")
        # 整数1
        self.assertEquals(ValiRuleChker.p_int_chker(1), True, msg="p_int_chker error,input 1 = False? expect True")
        self.assertEquals(ValiRuleChker.p_int_chker("1"), True, msg="p_int_chker error,input '1' = False? expect True")
        self.assertEquals(ValiRuleChker.p_int_chker(" 1 "), True,
                          msg="p_int_chker error,input ' 1 ' = False? expect True")
        # 整数0
        self.assertEquals(ValiRuleChker.p_int_chker(0), False, msg="p_int_chker error,input 0 = True? expect False")
        self.assertEquals(ValiRuleChker.p_int_chker("0"), False, msg="p_int_chker error,input '0' = True? expect False")
        self.assertEquals(ValiRuleChker.p_int_chker(" 0 "), False,
                          msg="p_int_chker error,input '0' = True? expect False")
        # 负数
        self.assertEquals(ValiRuleChker.p_int_chker(-1), False, msg="p_int_chker error,input -1 = True? expect False")
        self.assertEquals(ValiRuleChker.p_int_chker("-1"), False,
                          msg="p_int_chker error,input '-1' = True? expect False")
        # 非数字
        self.assertEquals(ValiRuleChker.p_int_chker("a"), False, msg="p_int_chker error,input 'a' = True? expect False")
        # 小数
        self.assertEquals(ValiRuleChker.p_int_chker(0.1), False,
                          msg="p_int_chker error,input '0.1' = True? expect False")
        self.assertEquals(ValiRuleChker.p_int_chker("0.1"), False,
                          msg="p_int_chker error,input '0.1' = True? expect False")

    def test_n_int_chker(self):  # 负整数不包含0
        # 不传值
        self.assertEquals(ValiRuleChker.n_int_chker(""), False, msg="n_int_chker error,input '' = True? expect False")
        # 负数
        self.assertEquals(ValiRuleChker.n_int_chker(-1), True, msg="n_int_chker error,input -1 = False? expect True")
        self.assertEquals(ValiRuleChker.n_int_chker("-1"), True,
                          msg="n_int_chker error,input '-1' = False? expect True")
        self.assertEquals(ValiRuleChker.n_int_chker(" -1 "), True,
                          msg="n_int_chker error,input ' -1 ' = False? expect True")
        # 整数0
        self.assertEquals(ValiRuleChker.n_int_chker(0), False, msg="n_int_chker error,input 0 = True? expect False")
        self.assertEquals(ValiRuleChker.n_int_chker("0"), False, msg="n_int_chker error,input '0' = True? expect False")
        self.assertEquals(ValiRuleChker.n_int_chker(" 0 "), False,
                          msg="n_int_chker error,input ' 0 ' = True? expect False")
        # 正数
        self.assertEquals(ValiRuleChker.n_int_chker(1), False, msg="n_int_chker error,input 1 = True? expect False")
        self.assertEquals(ValiRuleChker.n_int_chker("1"), False, msg="n_int_chker error,input '1' = True? expect False")
        self.assertEquals(ValiRuleChker.n_int_chker(" 1 "), False,
                          msg="n_int_chker error,input ' 1 ' = True? expect False")
        # 非数字
        self.assertEquals(ValiRuleChker.n_int_chker("a"), False, msg="n_int_chker error,input 'a' = True? expect False")
        self.assertEquals(ValiRuleChker.n_int_chker("-1-"), False,
                          msg="n_int_chker error,input '-1-' = True? expect False")
        # 小数
        self.assertEquals(ValiRuleChker.n_int_chker(0.1), False,
                          msg="n_int_chker error,input '0.1' = True? expect False")
        self.assertEquals(ValiRuleChker.n_int_chker("0.1"), False,
                          msg="n_int_chker error,input '0.1' = True? expect False")

    def test_float_chker(self):  # 浮点数不包含整数,但包含0
        # 不传值
        self.assertEquals(ValiRuleChker.float_chker(""), False, msg="float_chker error,input '' = True? expect False")
        # 整数1
        self.assertEquals(ValiRuleChker.float_chker(1), False, msg="float_chker error,input 1 = True? expect False")
        self.assertEquals(ValiRuleChker.float_chker("1"), False, msg="float_chker error,input '1' = True? expect False")
        # 整数0
        self.assertEquals(ValiRuleChker.float_chker(0), True, msg="float_chker error,input 0 = False? expect True")
        self.assertEquals(ValiRuleChker.float_chker("0"), True, msg="float_chker error,input '0' = False? expect True")
        # 负数
        self.assertEquals(ValiRuleChker.float_chker(-1), False, msg="float_chker error,input -1 = True? expect False")
        self.assertEquals(ValiRuleChker.float_chker("-1"), False,
                          msg="float_chker error,input '-1' = True? expect False")
        # 非数字
        self.assertEquals(ValiRuleChker.float_chker("a"), False, msg="float_chker error,input 'a' = True? expect False")
        self.assertEquals(ValiRuleChker.float_chker("-1-.-0-"), False,
                          msg="float_chker error,input '-1-.-0-' = True? expect False")
        # 正小数
        self.assertEquals(ValiRuleChker.float_chker(0.1), True, msg="float_chker error,input 0.1 = False? expect True")
        self.assertEquals(ValiRuleChker.float_chker("0.1"), True,
                          msg="float_chker error,input '0.1' = False? expect True")
        # 负小数
        self.assertEquals(ValiRuleChker.float_chker(-0.1), True,
                          msg="float_chker error,input -0.1 = False? expect True")
        self.assertEquals(ValiRuleChker.float_chker("-0.1"), True,
                          msg="float_chker error,input '-0.1' = False? expect True")

    def test_p_float_chker(self):  # 正小数不包含整数,也不包含0
        # 不传值
        self.assertEquals(ValiRuleChker.p_float_chker(""), False,
                          msg="p_float_chker error,input '' = True? expect False")
        # 整数1
        self.assertEquals(ValiRuleChker.p_float_chker(1), False, msg="p_float_chker error,input 1 = True? expect False")
        self.assertEquals(ValiRuleChker.p_float_chker("1"), False,
                          msg="p_float_chker error,input '1' = True? expect False")
        # 整数0
        self.assertEquals(ValiRuleChker.p_float_chker(0), False, msg="p_float_chker error,input 0 = True? expect False")
        self.assertEquals(ValiRuleChker.p_float_chker("0"), False,
                          msg="p_float_chker error,input '0' = True? expect False")
        # 负数
        self.assertEquals(ValiRuleChker.p_float_chker(-1), False,
                          msg="p_float_chker error,input -1 = True? expect False")
        self.assertEquals(ValiRuleChker.p_float_chker("-1"), False,
                          msg="p_float_chker error,input '-1' = True? expect False")
        # 非数字
        self.assertEquals(ValiRuleChker.p_float_chker("a"), False,
                          msg="p_float_chker error,input 'a' = True? expect False")
        # 正小数
        self.assertEquals(ValiRuleChker.p_float_chker(0.1), True,
                          msg="p_float_chker error,input 0.1 = False? expect True")
        self.assertEquals(ValiRuleChker.p_float_chker("0.1"), True,
                          msg="p_float_chker error,input '0.1' = False? expect True")
        # 负小数
        self.assertEquals(ValiRuleChker.p_float_chker(-0.1), False,
                          msg="p_float_chker error,input -0.1 = True? expect False")
        self.assertEquals(ValiRuleChker.p_float_chker("-0.1"), False,
                          msg="p_float_chker error,input '-0.1' = True? expect False")

    def test_n_float_chker(self):  # 负小数不包含整数,也不包含0
        # 不传值
        self.assertEquals(ValiRuleChker.n_float_chker(""), False,
                          msg="n_float_chker error,input '' = True? expect False")
        # 整数1
        self.assertEquals(ValiRuleChker.n_float_chker(1), False, msg="n_float_chker error,input 1 = True? expect False")
        self.assertEquals(ValiRuleChker.n_float_chker("1"), False,
                          msg="n_float_chker error,input '1' = True? expect False")
        # 整数0
        self.assertEquals(ValiRuleChker.n_float_chker(0), False, msg="n_float_chker error,input 0 = True? expect False")
        self.assertEquals(ValiRuleChker.n_float_chker("0"), False,
                          msg="n_float_chker error,input '0' = True? expect False")
        # 负数
        self.assertEquals(ValiRuleChker.n_float_chker(-1), False,
                          msg="n_float_chker error,input -1 = True? expect False")
        self.assertEquals(ValiRuleChker.n_float_chker("-1"), False,
                          msg="n_float_chker error,input '-1' = True? expect False")
        # 非数字
        self.assertEquals(ValiRuleChker.n_float_chker("a"), False,
                          msg="n_float_chker error,input 'a' = True? expect False")
        self.assertEquals(ValiRuleChker.n_float_chker("-0.1-"), False,
                          msg="n_float_chker error,input '-0.1-' = True? expect False")
        self.assertEquals(ValiRuleChker.n_float_chker("-0-.-1-"), False,
                          msg="n_float_chker error,input '-0-.-1-' = True? expect False")
        # 正小数
        self.assertEquals(ValiRuleChker.n_float_chker(0.1), False,
                          msg="n_float_chker error,input 0.1 = True? expect False")
        self.assertEquals(ValiRuleChker.n_float_chker("0.1"), False,
                          msg="n_float_chker error,input '0.1' = True? expect False")
        # 负小数
        self.assertEquals(ValiRuleChker.n_float_chker(-0.1), True,
                          msg="n_float_chker error,input -0.1 = False? expect True")
        self.assertEquals(ValiRuleChker.n_float_chker("-0.1"), True,
                          msg="n_float_chker error,input '-0.1' = False? expect True")

    def test_bool_chker(self):  # 负小数不包含整数,也不包含0
        # 不传值
        self.assertEquals(ValiRuleChker.bool_chker(""), False, msg="bool_chker error,input '' = True? expect False")
        # 原生布尔值
        self.assertEquals(ValiRuleChker.bool_chker(True), True,
                          msg="bool_chker error,input True = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(False), True,
                          msg="bool_chker error,input False = False? expect True")
        # 字符布尔值,同时测试大小写,空格
        self.assertEquals(ValiRuleChker.bool_chker(" true "), True,
                          msg="bool_chker error,input ' true ' = True? expect False")
        self.assertEquals(ValiRuleChker.bool_chker(" false "), True,
                          msg="bool_chker error,input ' false ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" True "), True,
                          msg="bool_chker error,input ' True ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" False "), True,
                          msg="bool_chker error,input ' False ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" TruE "), True,
                          msg="bool_chker error,input ' TruE ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" FalsE "), True,
                          msg="bool_chker error,input ' FalsE ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" FALSE "), True,
                          msg="bool_chker error,input ' FALSE ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" TRUE "), True,
                          msg="bool_chker error,input ' TRUE ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" 0 "), True,
                          msg="bool_chker error,input ' 0 ' = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(" 1 "), True,
                          msg="bool_chker error,input ' 1 ' = False? expect True")
        # 非法输入的字符串
        self.assertEquals(ValiRuleChker.bool_chker(" -1 "), False,
                          msg="bool_chker error,input '-1' = True? expect False")
        self.assertEquals(ValiRuleChker.bool_chker(" #$%^&*()_+_ "), False,
                          msg="bool_chker error,input '#$%^&*()_+_' = True? expect False")
        # 数字 0,1
        self.assertEquals(ValiRuleChker.bool_chker(0), True, msg="bool_chker error,input 0 = False? expect True")
        self.assertEquals(ValiRuleChker.bool_chker(1), True,
                          msg="bool_chker error,input 1 = False? expect True")
        # 小数
        self.assertEquals(ValiRuleChker.bool_chker(1.0), False, msg="bool_chker error,input 1.0 = True? expect False")
        self.assertEquals(ValiRuleChker.bool_chker(0.0), False,
                          msg="bool_chker error,input 0.0 = True? expect False")

    def test_int_list_chker(self):  # 1,2,3 or 1 , 2 , 3
        # 不传值
        self.assertEquals(ValiRuleChker.int_list_chker(""), False,
                          msg="int_list_chker error,input '' = True? expect False")
        # 传 仅传一个参数 '1',至少要一个逗号
        self.assertEquals(ValiRuleChker.int_list_chker("1"), False,
                          msg="int_list_chker error,input '1' = True? expect False")
        # 传 仅传一个参数 ' 1 ' 带空格,至少要一个逗号
        self.assertEquals(ValiRuleChker.int_list_chker(" 1 "), False,
                          msg="int_list_chker error,input ' 1 ' = True? expect False")
        # 传 '1,2,3'
        self.assertEquals(ValiRuleChker.int_list_chker(",1,2,3,"), False,
                          msg="int_list_chker error,input ',1,2,3,' = True? expect False")
        # 传带空格的 '1 ,2 , 3'
        self.assertEquals(ValiRuleChker.int_list_chker(" 1, 2, 3 "), True,
                          msg="int_list_chker error,input ' 1, 2, 3  ' = False? expect True")
        # 负数 '-1,-2,-3'
        self.assertEquals(ValiRuleChker.int_list_chker("-1,-2,-3"), True,
                          msg="int_list_chker error,input '-1,-2,-3' = False? expect True")
        # 小数 '0.1,0.2,0.3'
        self.assertEquals(ValiRuleChker.int_list_chker("0.1,0.2,0.3"), False,
                          msg="int_list_chker error,input '0.1,0.2,0.3' = True? expect False")
        # 传非法的字符串 'a,%,$'
        self.assertEquals(ValiRuleChker.int_list_chker(",a,%,$,a,%,$,"), False,
                          msg="int_list_chker error,input ' ,a,%,$,a,%,$, ' = True? expect False")
        # 传一堆空值 ,,,
        self.assertEquals(ValiRuleChker.int_list_chker(",,,"), False,
                          msg="int_list_chker error,input ' ,,, ' = True? expect False")
        # 传单个非法的字符串 'a'
        self.assertEquals(ValiRuleChker.int_list_chker(" a,1 "), False,
                          msg="int_list_chker error,input ' a,1 ' = True? expect False")

    def test_float_list_chker(self):  # 1,2,3 or 1 , 2 , 3
        # 不传值
        self.assertEquals(ValiRuleChker.float_list_chker(""), False,
                          msg="float_list_chker error,input '' = True? expect False")
        # 传 仅传一个参数 '1.0',至少要一个逗号
        self.assertEquals(ValiRuleChker.float_list_chker("1.0"), False,
                          msg="float_list_chker error,input '1.0' = True? expect False")
        # 传 '1.0,2.0,3.0'
        self.assertEquals(ValiRuleChker.float_list_chker("1.0,2.0,3.0"), True,
                          msg="float_list_chker error,input '1.0,2.0,3.0' = False? expect True")
        # 传 含空值的 ',1.0,,3.0,'
        self.assertEquals(ValiRuleChker.float_list_chker(",1.0,,3.0,"), False,
                          msg="float_list_chker error,input ',1.0,,3.0,' = True? expect False")
        # 传带空格的 '1.0,2.0,3.0'
        self.assertEquals(ValiRuleChker.float_list_chker("1.0 , 2.0 , 3.0"), True,
                          msg="float_list_chker error,input '1.0,2.0,3.0' = False? expect True")
        # 负数 '-1.0,-2.0,-3.0'
        self.assertEquals(ValiRuleChker.float_list_chker("-1.0,-2.0,-3.0"), True,
                          msg="float_list_chker error,input '-1.0,-2.0,-3.0' = False? expect True")
        # 整数 '1,2,3'
        self.assertEquals(ValiRuleChker.float_list_chker("1,2,3"), False,
                          msg="float_list_chker error,input '1,2,3' = True? expect False")
        # 传非法的字符串 'a,%,$'
        self.assertEquals(ValiRuleChker.float_list_chker("a,%,$,a,%,$"), False,
                          msg="float_list_chker error,input ' a,%,$,a,%,$ ' = True? expect False")
        # 传一堆空值 ,,,
        self.assertEquals(ValiRuleChker.float_list_chker(",,,"), False,
                          msg="float_list_chker error,input ' ,,, ' = True? expect False")
        # 传单个非法的字符串 'a'
        self.assertEquals(ValiRuleChker.float_list_chker(" a,1.0 "), False,
                          msg="float_list_chker error,input ' a,1.0 ' = True? expect False")

    def test_str_list_chker(self):  # a,b,c or a , b , c
        # 不传值
        self.assertEquals(ValiRuleChker.str_list_chker(""), False,
                          msg="str_list_chker error,input '' = True? expect False")
        # 传 仅传一个参数 'a',必须至少有一个逗号
        self.assertEquals(ValiRuleChker.str_list_chker("a"), False,
                          msg="str_list_chker error,input 'a' = True? expect False")
        # 传 仅传一个参数 ' a ' 带空格,必须至少有一个逗号
        self.assertEquals(ValiRuleChker.str_list_chker(" a "), False,
                          msg="str_list_chker error,input ' a ' = True? expect False")
        # 传 'a,b,c'
        self.assertEquals(ValiRuleChker.str_list_chker(",a,b,c,"), False,
                          msg="str_list_chker error,input ',a,b,c,' = True? expect False")
        # 传带空格的 'a , b , c'
        self.assertEquals(ValiRuleChker.str_list_chker(" a, b, c "), True,
                          msg="str_list_chker error,input ' a, b, c ' = False? expect True")
        # 传一堆空值 ,,,
        self.assertEquals(ValiRuleChker.str_list_chker(",,,"), False,
                          msg="str_list_chker error,input ' ,,, ' = True? expect False")

    def test_str_chker(self):  # 仅判断有值
        # 不传值
        self.assertEquals(ValiRuleChker.str_chker(""), True,
                          msg="str_list_chker error,input '' = False? expect True")
        # 只要传值即可
        self.assertEquals(ValiRuleChker.str_chker("a"), True,
                          msg="str_list_chker error,input 'a' = False? expect True")

    def test_guid_chker(self):  # a,b,c or a , b , c
        # 不传值
        self.assertEquals(ValiRuleChker.guid_chker(""), False,
                          msg="guid_chker error,input '' = True? expect False")
        # 传 仅传一个参数 'a'
        self.assertEquals(ValiRuleChker.guid_chker("a"), False,
                          msg="guid_chker error,input 'a' = True? expect False")
        # 传 仅传一个参数 ' a ' 带空格,必须至少有一个逗号
        self.assertEquals(ValiRuleChker.guid_chker(" a "), False,
                          msg="guid_chker error,input ' a ' = True? expect False")
        # 传 'e1495b94-2d00-46ca-a88f-5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_chker("e1495b94-2d00-46ca-a88f-5b2eeb4fc458"), True,
                          msg="guid_chker error,input 'e1495b94-2d00-46ca-a88f-5b2eeb4fc458' = False? expect True")
        # 头尾可以带空格
        self.assertEquals(ValiRuleChker.guid_chker(" e1495b94-2d00-46ca-a88f-5b2eeb4fc458 "), True,
                          msg="guid_chker error,input ' e1495b94-2d00-46ca-a88f-5b2eeb4fc458 ' = False? expect True")
        # 传 'e1495b942d0046caa88f5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_chker("e1495b942d0046caa88f5b2eeb4fc458"), True,
                          msg="guid_chker error,input 'e1495b942d0046caa88f5b2eeb4fc458' = False? expect True")
        # 头尾可以带空格
        self.assertEquals(ValiRuleChker.guid_chker(" e1495b942d0046caa88f5b2eeb4fc458 "), True,
                          msg="guid_chker error,input ' e1495b942d0046caa88f5b2eeb4fc458 ' = False? expect True")
        # 传带空格的 ' e1495b94 - 2d00 - 46ca - a88f - 5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_chker(" e1495b94 - 2d00 - 46ca - a88f - 5b2eeb4fc458"), False,
                          msg="guid_chker error,\
input ' e1495b94 - 2d00 - 46ca - a88f - 5b2eeb4fc458' = True? expect False")
        # 传带空格的 ' e14 95b942 d0046caa88 f5 b2eeb4 fc458 '
        self.assertEquals(ValiRuleChker.guid_chker(" e14 95b942 d0046caa88 f5 b2eeb4 fc458 "), False,
                          msg="guid_chker error,input ' e14 95b942 d0046caa88 f5 b2eeb4 fc458 ' = False? expect True")
        # 传带非十六进制的字符 'e1495b942dzzzzcaa88f5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_chker(" e14 95b942 d0046caa88 f5 b2eeb4 fc458 "), False,
                          msg="guid_chker error,input ' e14 95b942 d0046caa88 f5 b2eeb4 fc458 ' = True? expect False")
        # 传带非十六进制的字符 ' e1495zzz - 2zzz - 46zz - a8zz - 5b2eeb4fxxxx'
        self.assertEquals(ValiRuleChker.guid_chker(" e1495zzz - 2zzz - 46zz - a8zz - 5b2eeb4fxxxx"), False,
                          msg="guid_chker error,input ' e1495zzz - 2zzz - 46zz - \
a8zz - 5b2eeb4fxxxx' = True? expect False")
        # 传长度不够的 'e1495zzz'
        self.assertEquals(ValiRuleChker.guid_chker("e1495zzz"), False,
                          msg="guid_chker error,input 'e1495zzz' = True? expect False")
        # 传长度太长的 'e1495b942d0046caa88f5b2eeb4fc458e1495b942d0046caa88f5b2e'
        self.assertEquals(ValiRuleChker.guid_chker("e1495b942d0046caa88f5b2eeb4fc458e1495b942d0046caa88f5b2e"),
                          False,
                          msg="guid_chker error,input \
                          'e1495b942d0046caa88f5b2eeb4fc458e1495b942d0046caa88f5b2e' = True? expect False")

    def test_guid_list_chker(self):  # a,b,c or a , b , c
        # 不传值
        self.assertEquals(ValiRuleChker.guid_list_chker(""), False,
                          msg="guid_list_chker error,input '' = True? expect False")
        # 传 'e1495b94-2d00-46ca-a88f-5b2eeb4fc458',必须至少有一个逗号
        self.assertEquals(ValiRuleChker.guid_list_chker("e1495b94-2d00-46ca-a88f-5b2eeb4fc458"), False,
                          msg="guid_chker error,input 'e1495b94-2d00-46ca-a88f-5b2eeb4fc458' = True? expect False")
        # 传 'e1495b94-2d00-46ca-a88f-5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_list_chker(
            "e1495b94-2d00-46ca-a88f-5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458"),
            True,
            msg="guid_list_chker error,input 'e1495b94-2d00-46ca-a88f-5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458' = False? expect True")
        # 传 'e1495b942d0046caa88f5b2eeb4fc458,e1495b942d0046caa88f5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_list_chker(
            "e1495b942d0046caa88f5b2eeb4fc458,e1495b942d0046caa88f5b2eeb4fc458"),
            True,
            msg="guid_list_chker error,input 'e1495b942d0046caa88f5b2eeb4fc458,e1495b942d0046caa88f5b2eeb4fc458' = False? expect True")
        # 混排 'e1495b942d0046caa88f5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_list_chker(
            "e1495b942d0046caa88f5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458"),
            True,
            msg="guid_list_chker error,input 'e1495b942d0046caa88f5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458' = False? expect True")
        # 传带空格的 ' e1495b942d0046caa88f5b2eeb4fc458 , e1495b94-2d00-46ca-a88f-5b2eeb4fc458 '
        self.assertEquals(
            ValiRuleChker.guid_list_chker(" e1495b942d0046caa88f5b2eeb4fc458 , e1495b94-2d00-46ca-a88f-5b2eeb4fc458 "),
            True,
            msg="guid_list_chker error,input ' e1495b942d0046caa88f5b2eeb4fc458 , e1495b94-2d00-46ca-a88f-5b2eeb4fc458 ' = False? expect True")
        # 传一堆空值 ,,,
        self.assertEquals(ValiRuleChker.guid_list_chker(",,,"), False,
                          msg="guid_list_chker error,input ' ,,, ' = True? expect False")
        # 非十六进制字符 'z1495b942d0046caa88f5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_list_chker(
            "z1495b942d0046caa88f5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458"),
            False,
            msg="guid_list_chker error,input 'z1495b942d0046caa88f5b2eeb4fc458,e1495b94-2d00-46ca-a88f-5b2eeb4fc458' = True? expect False")
        # 长度错误 '6caa88f5b2eeb4fc458,6ca-a88f-5b2eeb4fc458'
        self.assertEquals(ValiRuleChker.guid_list_chker(
            "6caa88f5b2eeb4fc458,88f5b2eeb4fc45888f5b2eeb4fc45888f5b2eeb4fc458"),
            False,
            msg="guid_list_chker error,input '6caa88f5b2eeb4fc458,88f5b2eeb4fc45888f5b2eeb4fc45888f5b2eeb4fc458' = True? expect False")

    def test_zero_chker(self):  # a,b,c or a , b , c
        # 不传值
        assert ValiRuleChker.zero_chker("") is False
        # 传 0
        assert ValiRuleChker.zero_chker(0) is True
        # 传 ' 0 '
        assert ValiRuleChker.zero_chker(' 0 ') is True
        # 传 ' 0.0 '
        assert ValiRuleChker.zero_chker(' 0.0 ') is False
        # 传 ' 00 '
        assert ValiRuleChker.zero_chker(' 00 ') is False
        # 传 ' a '
        assert ValiRuleChker.zero_chker(' 00 ') is False

    def test_vali_rule_chker(self):
        # region 测试获得的值对不对
        chker = ValiRuleChker(
            r' field -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float" -w "haha, you got it" -v 1|2|3')
        assert chker.field == "field"
        assert chker.has_field == True
        assert chker.info == "test%s123123"
        assert chker.has_info == True
        assert chker.required == True
        assert chker.has_required == True
        assert chker.len == (1, 4)
        assert chker.has_len == True
        assert chker.regx == '/mo\\" -bi/gi'
        assert chker.has_regx == True
        assert chker.type == ValiRuleInfo.N_INT | ValiRuleInfo.P_FLOAT
        assert chker.has_type == True
        assert chker.warning == "haha, you got it"
        assert chker.has_warning == True
        assert chker.values == ["1", "2", "3"]
        assert chker.has_values == True

        chker = ValiRuleChker(r'')
        assert chker.field == ""
        assert chker.has_field == False
        assert chker.info == ""
        assert chker.has_info == False
        assert chker.required == False
        assert chker.has_required == False
        assert chker.len == (-1, -1)
        assert chker.has_len == False
        assert chker.regx == ''
        assert chker.has_regx == False
        assert chker.type == 0
        assert chker.has_type == False
        assert chker.warning == ""
        assert chker.has_warning == False
        assert chker.values == []
        assert chker.has_values == False
        chker = ValiRuleChker(r'-r mobi')
        assert chker.regx == (ValiRuleInfo.REGX_TMP.get("mobi") or "")
        chker = ValiRuleChker(r'-r 123123123123123123123123')
        assert chker.regx == (ValiRuleInfo.REGX_TMP.get("123123123123123123123123") or "")
        # endregion
        # region 测试两种chk的参数类型对不对
        chker = ValiRuleChker(
            r' field -i test%s123123 -n -l 1,4 -r "/[\-\d\.]+/" -t "zero|-int|+float" -w "haha, you got it"')
        # 空值是不被接受的
        msg, info = chker.chk("")
        assert chker.is_validated is False
        assert msg == ValiRuleChker.REQUIRED_ERR
        # 1,4的长度检查失败
        msg, info = chker.chk("abcde")
        assert chker.is_validated is False
        assert msg == ValiRuleChker.LEN_ERR
        # 类型不是负数或正小数或0
        msg, info = chker.chk("abc")
        assert chker.is_validated is False
        assert msg == ValiRuleChker.TYPE_ERR
        # 类型为负数
        msg, info = chker.chk("1")
        assert chker.is_validated is False
        assert msg == ValiRuleChker.TYPE_ERR
        # 类型为正小数
        msg, info = chker.chk("1.0")
        assert chker.is_validated is True
        assert msg == ValiRuleChker.OK
        # 类型为负数
        msg, info = chker.chk(-1)
        assert chker.is_validated is True
        assert msg == ValiRuleChker.OK
        # 类型为零
        msg, info = chker.chk(0)
        assert chker.is_validated is True
        assert msg == ValiRuleChker.OK
        # 检查所有预设的正则
        regx_yes_vals = {
            "mobi": ["13599445586", "13788888888", "13788888888", "18066666666", "15000000000", "17000000000"],
            # 手机号 +86 13599999999
            "email": ["boois@qq.com", "a@163.com", "a@1.2.3.com", "a.1.2.3@q.q.com"],  # 邮箱 boois@qq.com
            "zip_code": ["350001"],  # 邮政编码 350001
            "phone": ["88083006", "0591-88083006", "0591 88083006"],
            "account": ["abcder1034_1123123ASCET"],  # 账号 字母数字下划线
            "passwd": ["abcder1034_1123123ASCET"],  # 密码 字母数字下划线
            "nickname": [u"我了个去", "pig823", u"我了个pig823", u"我了个pig823_-134"],  # 昵称 中文英文数字下划线短连接线,不能有其他特殊字符
            "qq": ["66630720", "10000", "55552345"],  # QQ号 [1-9][0-9]{4,}
            "id_card": ["350700111111111111", "350700111111111"],  # 身份证
            "ip": ["0.0.0.0", "255.255.255.255", "192.168.3.1", "10.0.0.1", "127.0.0.1"],  # ip地址
            "url": ["http://www.baidu.com"],  # 网络链接
            "zh": [u"只有中文"],  # 仅为中文
        }
        regx_no_vals = {
            "mobi": ["13599", "137a", "ttt", " ", "444", "19400000000"],
            # 手机号 +86 13599999999
            "email": ["boois@qq"],  # 邮箱 boois@qq.com
            "zip_code": ["a123123"],  # 邮政编码 350001
            "phone": ["a88083006", "b0591-88083006"],
            "account": ["$12312312313123", "1asdfasdfasf"],  # 账号 字母数字下划线
            "passwd": ["$12312312313123", "1asdfasdfasf"],  # 密码 字母数字下划线
            "nickname": [u"$我了个去"],  # 昵称 中文英文数字下划线短连接线,不能有其他特殊字符
            "qq": ["66", "100", "aaa"],  # QQ号 [1-9][0-9]{4,}
            "id_card": ["3507001111", "35070011$1"],  # 身份证
            "ip": ["0.0.0.0.0", "255.255.255", "192.168", "a.a.a.a", "asdf$123asdf%"],  # ip地址
            "url": ["123"],  # 网络链接
            "zh": ["123123%1", "1111"],  # 仅为中文
        }
        for regx in ValiRuleInfo.REGX_TMP:
            chker = ValiRuleChker(r'-r "%s"' % regx)
            yes_vals = regx_yes_vals.get(regx)
            # print yes_vals
            for val in yes_vals:
                msg, info = chker.chk(val)
                self.assertEquals(chker.is_validated, True,
                                  msg="test_regx_yes regx= %s,val= %s" % (ValiRuleInfo.REGX_TMP[regx], val))
            no_vals = regx_no_vals.get(regx)
            for val in no_vals:
                msg, info = chker.chk(val)
                self.assertEquals(chker.is_validated, False,
                                  msg="test_regx_no regx= %s,val= %s" % (ValiRuleInfo.REGX_TMP[regx], val))

        chker = ValiRuleChker(r'-r "/^\d+$/gim"')
        msg, info = chker.chk("123123123123")
        assert chker.is_validated
        msg, info = chker.chk("1231aaaaa3123")
        assert not chker.is_validated

    def test_zero_rule(self):
        # region 测试两种chk的参数类型对不对
        chker = ValiRuleChker(
            r'-t zero|+int')

        msg, info = chker.chk("-1")
        assert chker.is_validated is False
        assert msg == ValiRuleChker.TYPE_ERR
        # 因为没有-n,所以输入空值也是可以的
        msg, info = chker.chk("")
        assert chker.is_validated is True
        assert msg == ValiRuleChker.OK

    def test_values_rule(self):

        chker = ValiRuleChker(
            r'-v 1|2|3')


if __name__ == '__main__':
    unittest.main()
