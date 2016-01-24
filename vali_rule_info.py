#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
本模块用于输入参数的合法性
'''
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
from cmd_parser import cmd_parser


class ValiRuleInfo(object):
    '''
    用来描述一个基于 r"filed -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float -w test%s123123" 规则的实体类
    1.首先 self.filed, self.cmd_list 是最基础的数据,表名字段名称和命令列表,cmd_list指的是解析出来的命令和值
    2.用cmd字符串初始化当前类后,可以利用的属性如下:
        info.filed # 字段名称
        info.len # 长度 (起始长度,结束长度),其中某个长度提取失败时返回值-1
        info.type # 类型的或运算结果,实际使用时 用 ValiRuleInfo.INT & info.type 如果不等于0,则ValiRuleInfo.INT存在于type
                  # type可选值请参见-t参数常量设置,大小写不敏感,正负数可以简写为  +int -int 出现-号时,值请用引号包裹
        info.regx # 正则表达式,在命令的值中 /开头表示原生正则,否则会拿到REGX_TMP中提取,如果REGX_TMP中没有则返回空字符串
        info.info # 当前字段的输入提示
        info.warning # 当检测未通过时显示的信息
        info.required # 是否是必须值
    3.has_field,has_len,has_regx,has_info,has_warning,has_required 用来判断是否有输入该命令
    '''

    """下方是-t参数的值配置"""
    INT = 1 << 0  # 整数
    P_INT = 1 << 1  # 正整数 positive integer
    N_INT = 1 << 2  # 负整数 negative integer
    FLOAT = 1 << 3  # 小数
    P_FLOAT = 1 << 4  # 正小数 可以无小数点,兼容正整数
    N_FLOAT = 1 << 5  # 负小数 可以无小数点,兼容负整数
    BOOL = 1 << 6  # 布尔值 true|false|0|1 大小写不敏感
    INT_LIST = 1 << 7  # 数字数组 1,2,3,4,5
    STR_LIST = 1 << 8  # 字符串数组 a,b,c,d,e
    DICT = 1 << 9  # 字典 "a":"foo",b:"bar","c":"baz","d":"qux",必须用双引号将kv包裹起来
    JSON = 1 << 10  # 能通过 json.loads(foo)的字符串
    GUID_LIST = 1 << 11  # 32位无横线GUID,36位有横线GUID,..
    FLOAT_LIST = 1 << 12  # 小数组合成的列表
    ZERO = 1 << 13  # 零
    STR = 1 << 14  # 任意字符
    GUID = 1 << 15  # 32位无横线GUID,36位有横线GUID

    TYPE_LIST = {
        "INT": INT,
        "P_INT": P_INT,
        "N_INT": N_INT,
        "FLOAT": FLOAT,
        "P_FLOAT": P_FLOAT,
        "N_FLOAT": N_FLOAT,
        "BOOL": BOOL,
        "INT_LIST": INT_LIST,
        "STR_LIST": STR_LIST,
        "DICT": DICT,
        "JSON": JSON,
        "GUID_LIST": GUID_LIST,
        "FLOAT_LIST": FLOAT_LIST,
        "ZERO": ZERO,
        "STR": STR,
        "GUID": GUID,
    }

    REGX_TMP = {
        "mobi": r"^0?(13|14|15|18|17)[0-9]{9}$",  # 手机号 +86 13599999999
        "email": r"^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]*\.)+[A-Za-z]{2,14}$",  # 邮箱 boois@qq.com
        "zip_code": r"^\d{6}$",  # 邮政编码 350001
        "phone": r"^\d+$|^\d{4}[\s-]\d+$|^\+{0,1}86[\s-]\d{4}[\s-]\d+$",
        "account": r"^[a-zA-Z][0-9a-zA-Z_]*$",  # 账号 字母数字下划线
        "passwd": r"^[a-zA-Z][0-9a-zA-Z_]*$",  # 密码 字母数字下划线
        "nickname": u"^[\u4e00-\u9fa5_0-9a-zA-Z-]*$",  # 昵称 中文英文数字下划线短连接线,不能有其他特殊字符
        "qq": r"^[1-9][0-9]{4,}$",  # QQ号 [1-9][0-9]{4,}
        "id_card": r"^(\d{15}$|^\d{18}$|^\d{17}(\d|X|x))$",  # 身份证
        "ip": r"^((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))$",
    # ip地址
        "url": r"^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]*",  # 网络链接
        "zh": u"^[\u4e00-\u9fa5]*$",  # 仅为中文,这里有个要点,中文匹配必须正则规则也使用u编码,否则无法匹配
    }

    def __init__(self, rule):
        self.filed, self.cmd_list = cmd_parser(rule, qoute_err=True)
        self.info = self.cmd_list.get("i", "")
        # 处理类型参数
        self.type_str = self.cmd_list.get("t", "").replace("+", "P_").replace("-", "N_")
        type_arr = self.type_str.split("|")
        self.type = 0  # 通过反射和位运算来指定权限
        for type in [_.upper() for _ in type_arr if _.upper() in self.TYPE_LIST]:
            # print type
            self.type = self.type | self.__getattribute__(type)
        # 处理正则表达式
        self.regx_str = self.cmd_list.get("r", "")
        if self.regx_str.startswith("/"):  # 如果是以反斜杠开头则表示是一个原生正则
            self.regx = self.regx_str
            pass
        elif self.regx_str.lower() in self.REGX_TMP:  # 如果存在于模板文件列表中则取出
            self.regx = self.REGX_TMP.get(self.regx_str.lower())
        else:  # 否则为空
            self.regx = ""
        # 处理长度字符串
        self.len_str = self.cmd_list.get("l") or ""
        len_arr = self.len_str.split(",")

        # 定义一个构架长度值的方法,用来做一些异常值排除
        def get_len_val(val):
            if val.isdigit():
                return int(val)
            elif val.strip().startswith("-") and val.replace("-", "").isdigit():
                return -int(val.replace("-", ""))
            else:
                return -1

        if len(len_arr) == 1:
            self.len = get_len_val(len_arr[0]), -1
        if len(len_arr) >= 2:
            self.len = get_len_val(len_arr[0]), get_len_val(len_arr[1])

        self.required = self.cmd_list.get("n") is not None
        self.warning = self.cmd_list.get("w", "")
        self.values = self.cmd_list.get("v")
        self.values = [] if self.values is None or self.values == "" else self.values.split("|")

    def __str__(self):
        return """<ValiRuleInfo:{filed:%s, len:%s, len_str:%s, type:%s,\
type_str:%s, regx:%s, regx_str:%s, info:%s, warning:%s, required:%s,values=%s}>""" % (
            self.filed, self.len, self.len_str, self.type, self.type_str, self.regx, self.regx_str, self.info,
            self.warning,
            self.required, self.values)

    has_field = property(fget=lambda self: self.filed is not None and self.filed is not "")
    has_len = property(fget=lambda self: self.cmd_list.get("l") is not None)
    has_regx = property(fget=lambda self: self.cmd_list.get("r") is not None)
    has_info = property(fget=lambda self: self.cmd_list.get("i") is not None)
    has_warning = property(fget=lambda self: self.cmd_list.get("w") is not None)
    has_required = property(fget=lambda self: self.cmd_list.get("n") is not None)
    has_type = property(fget=lambda self: self.cmd_list.get("t") is not None)
    has_values = property(fget=lambda self: self.cmd_list.get("v") is not None)

# if __name__ == "__main__":
#     info = ValiRuleInfo(r' field -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float"',False)
#     print info
