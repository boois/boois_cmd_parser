#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
本模块用于输入参数的合法性
'''
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
from vali_rule_info import ValiRuleInfo
import re


class ValiRuleChker(object):
    '''
    标准用法:
    chker = ValiRuleChker(r'field -i test%s123123 -n -l 1,5 -r "mobi" -t "-int|+float" -w "haha,your got it -v 1|2|3"')
    chker.chk(request.form) 或 chk({"field","12312123"})
    字段名为空的用法:
    chker = ValiRuleChker(r'-i test%s123123 -n -l 1,5 -r "mobi" -t "-int|+float" -w "haha,your got it"')
    msg,info = chker.chk("123123123123")

    执行完chk方法后,调用chker.is_validated来判断是否完全测试通过

    也可以通过查看 msg来查看相应结果

    type类型是严格指定的
    比如 int_list就是严格的int数组,必须包含逗号,具体的看test中的测试文档,如果要同时允许1个元素的list通过测试,就指定  int|int_list
    同理   str|str_list
    str就是任意值,可为空
    有增加一个zero类型,因为正负数是不含0的
    比如指定  zero|+int = 大于零的所有数,  而  +int 表示的是从1开始的所有正数

    可选值 -v  1|2|3
    必须值其中的一个值

    '''

    REQUIRED_ERR = 1  # 必选项错误
    LEN_ERR = 2  # 长度错误
    TYPE_ERR = 4  # 类型错误
    REGX_ERR = 8  # 正则错误
    VAL_ERR = 16  # 可选值错误
    OK = 32  # 成功

    # region类型检查器
    @staticmethod
    def p_int_chker(val):  # 只允许正整数,不含0
        if ValiRuleChker.zero_chker(val):
            return False
        if isinstance(val, int):
            if val <= 0:
                return False
        elif not str(val).strip().isdigit():
            return False
        return True

    @staticmethod
    def n_int_chker(val):  # 只允许负整数,不含0
        if ValiRuleChker.zero_chker(val):
            return False
        if isinstance(val, int):
            if val >= 0:
                return False
        elif not str(val).strip().startswith("-") or not str(val).strip()[1:].isdigit():
            return False
        return True

    @staticmethod
    def int_chker(val):  # 整数都可以,含0
        if ValiRuleChker.zero_chker(val):
            return True
        return ValiRuleChker.p_int_chker(val) or ValiRuleChker.n_int_chker(val)

    @staticmethod
    def p_float_chker(val):  # 正小数,不含整数,不含0
        if ValiRuleChker.zero_chker(val):
            return False
        if isinstance(val, float):
            return val > 0
        if str(val).strip().replace(".", "").isdigit() and len(str(val).strip().split(".")) == 2:
            return True
        return False

    @staticmethod
    def n_float_chker(val):  # 负小数,不含整数,不含0
        if ValiRuleChker.zero_chker(val):
            return False
        if isinstance(val, float):
            return val < 0
        if str(val).strip().replace(".", "").replace("-", "").isdigit():
            val_arr = str(val).strip().split(".")
            if len(val_arr) == 2:
                if val_arr[1].isdigit() and val_arr[0].startswith("-") and val_arr[0][1:].isdigit():
                    return True
        return False

    @staticmethod
    def float_chker(val):  # 小数都可以,含0
        if ValiRuleChker.zero_chker(val):
            return True
        return ValiRuleChker.p_float_chker(val) or ValiRuleChker.n_float_chker(val)

    @staticmethod
    def bool_chker(val):  # True,False;'true'|'false'不分大小写;'0'|'1'|0|1也可以
        if isinstance(val, bool):
            return True
        if isinstance(val, int) and (val == 1 or val == 0):
            return True
        if str(val).strip().lower() in ["true", "false", "0", "1"]:
            return True
        return False

    @staticmethod
    def int_list_chker(val):  # 1,2,3;,,,;但至少要带一个逗号
        if not val:
            return False
        if not isinstance(val, str):
            return False
        if val.find(",") == -1:
            return False
        val = val.strip()
        for int_val in val.split(","):
            if int_val.replace(" ", "") == "":  # 不允许有空值传入
                return False
            if not ValiRuleChker.int_chker(int_val):
                return False
        return True

    @staticmethod
    def str_list_chker(val):  # a,b,c;,,,;但至少要带一个逗号
        if not val:
            return False
        if not isinstance(val, str):
            return False
        if val.find(",") == -1:
            return False
        val = val.strip()
        for str_val in val.split(","):
            if str_val.replace(" ", "") == "":  # 不允许有空值传入
                return False
            if not ValiRuleChker.str_chker(str_val):
                return False
        return True

    @staticmethod
    def guid_chker(val):  # 32位无横杠guid,36位带横杠guid;,,,;但至少要带一个逗号
        if not val:
            return False
        if not isinstance(val, str):
            return False
        val = val.strip()
        if len(val) != 32 and len(val) != 36:
            return False
        if len(val) == 36:
            group = val.split("-")
            if len(group) != 5:
                return False
            else:  # e1495b94-2d00-46ca-a88f-5b2eeb4fc458
                if len(group[0]) != 8 \
                        or len(group[1]) != 4 \
                        or len(group[2]) != 4 \
                        or len(group[3]) != 4 \
                        or len(group[4]) != 12:
                    return False
        filter_result = [_ for _ in val.strip().lower() if
                         _ in ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

        if len(filter_result) != 32:
            return False
        return True

    @staticmethod
    def guid_list_chker(val):  # 32位无横杠guid,36位带横杠guid;,,,;但至少要带一个逗号
        if not val:
            return False
        if not isinstance(val, str):
            return False
        if val.find(",") == -1:
            return False
        val = val.strip()
        for guid in val.split(","):
            if guid.replace(" ", "") == "":  # 不允许有空值传入
                return False
            if not ValiRuleChker.guid_chker(guid):
                return False
        return True

    @staticmethod
    def str_chker(val):  # 仅占位,所有的都可以,主要用于 str|str_list,表示可以是一个字符串也可以是一个a,b类型
        return True

    @staticmethod
    def float_list_chker(val):  # 1.0,2.0,3.0;,,,;但至少要带一个逗号
        if not val:
            return False
        if not isinstance(val, str):
            return False
        if val.find(",") == -1:
            return False
        val = val.strip()
        for float_val in val.split(","):
            if float_val.replace(" ", "") == "":  # 不允许有空值传入
                return False
            if not ValiRuleChker.float_chker(float_val):
                return False
        return True

    @staticmethod
    def zero_chker(val):  # 1.0,2.0,3.0;,,,;但至少要带一个逗号
        return val == 0 or str(val).strip() == "0"

    # endregion
    is_validated = True

    def __init__(self, rule):
        self.vali_rule_info = ValiRuleInfo(rule)

    def chk(self, val_dict_or_str):
        '''
        按照规则检查相应的内容,
        :param val_dict_or_str:可以是一个dict,比如request.form,也可以直接传一个字符串进来
        :return:
        '''
        val = val_dict_or_str
        if isinstance(val_dict_or_str, dict):
            val = val_dict_or_str.get(self.field, "")

        if self.has_required and val != 0:  # 如果需要输入该字段
            if not val:  # 但是又没有值
                self.is_validated = False
                return (ValiRuleChker.REQUIRED_ERR, "%s必须输入值" % self.field)

        if val == 0 or (val is not None and val != ""):  # 只要具备值,就要通过以下检查
            val = str(val)
            # 判断长度
            if self.has_len:
                min_len, max_len = self.len
                if min_len != -1:
                    if len(val) < min_len:
                        self.is_validated = False
                        return (ValiRuleChker.LEN_ERR, "%s长度不能小于{min_len}".format(min_len=min_len) % self.field)
                if max_len != -1:
                    if len(val) > max_len:
                        self.is_validated = False
                        return (ValiRuleChker.LEN_ERR, "%s长度不能大于{max_len}".format(max_len=max_len) % self.field)
            # 检查预设值
            if self.has_values and len(self.values) != 0:
                if val.strip() not in self.values:
                    self.is_validated = False
                    return (ValiRuleChker.VAL_ERR, "%s的值必须为{vals}".format(vals="或".join(self.values)) % self.field)
            # 根据我们获取到的type或值,逐个检查所需类型:
            is_passed = False
            type_list = []
            for rule_type in ValiRuleInfo.TYPE_LIST:
                if ValiRuleInfo.TYPE_LIST[rule_type] & self.type != 0:
                    type_list.append(rule_type)
                    func = ValiRuleChker.__getattribute__(self, "%s_chker" % rule_type.lower())
                    if func:
                        if func(val):  # 只要有一个满足条件即认为通过验证
                            is_passed = True
                            break
            if not is_passed and len(type_list) != 0:
                self.is_validated = False
                return (ValiRuleChker.TYPE_ERR, "%s必须是类型{type}".format(type="或".join(type_list)) % self.field)
            # 测试正则表达式

            if self.has_regx and self.regx != "":
                val = str(val)
                regx = self.regx
                has_gan = regx.startswith("/")
                if has_gan:
                    regx = regx[1:]
                regx_flags = ["/", "/i", "/g", "/m", "/ig", "/gi", "/mi", "/im", "/gm", "/mg", "/igm", "/gim", "/img",
                              "/mig", "/gmi", "/mgi"]
                end_flag = ""
                if has_gan:
                    for flag in regx_flags:
                        if regx.endswith(flag):
                            end_flag = flag
                            regx = regx[:-len(flag)]
                            break
                re_flags = 0
                if "g" in end_flag:
                    pass
                    # re_flags = re_flags|re.
                if "i" in end_flag:
                    re_flags = re_flags | re.I
                if "m" in end_flag:
                    re_flags = re_flags | re.M
                # print regx
                if re.match(regx, str(val).decode("utf8"), re_flags) is None:
                    self.is_validated = False
                    return (ValiRuleChker.REGX_ERR, "%s没有通过正则{regx}检查".format(regx=self.regx) % self.field)

        self.is_validated = True
        return (ValiRuleChker.OK, "通过验证!")

    cmd_list = property(fget=lambda self: self.vali_rule_info.cmd_list)
    field = property(fget=lambda self: self.vali_rule_info.filed)
    len = property(fget=lambda self: self.vali_rule_info.len)
    field = property(fget=lambda self: self.vali_rule_info.filed)
    type = property(fget=lambda self: self.vali_rule_info.type)
    regx = property(fget=lambda self: self.vali_rule_info.regx)
    info = property(fget=lambda self: self.vali_rule_info.info)
    warning = property(fget=lambda self: self.vali_rule_info.warning)
    required = property(fget=lambda self: self.vali_rule_info.required)
    values = property(fget=lambda self: self.vali_rule_info.values)

    has_field = property(fget=lambda self: self.vali_rule_info.has_field)
    has_len = property(fget=lambda self: self.vali_rule_info.has_len)
    has_regx = property(fget=lambda self: self.vali_rule_info.has_regx)
    has_info = property(fget=lambda self: self.vali_rule_info.has_info)
    has_warning = property(fget=lambda self: self.vali_rule_info.has_warning)
    has_required = property(fget=lambda self: self.vali_rule_info.has_required)
    has_type = property(fget=lambda self: self.vali_rule_info.has_type)
    has_values = property(fget=lambda self: self.vali_rule_info.has_values)
