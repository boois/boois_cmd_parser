boois_cmd_parser
===========================
a python program for parse a cmd_str to tuple ,r' cmd_name -foo value -bar "value" -baz "value\"value" ' to ("cmd_name",{"foo","value"})  
该文件取名为`boois_cmd_parser`,我的一些相关的代码也会用`boois`作为前缀  
该文件用采用逐个字符流式读取来将一串类似 linux 命令行的字符转换为一个tuple ("命令名称",{"命令1","值"...})  
不是采用分割符和正则表达式来处理,而是采用类似解释器的方式,逐个字节读取归集  
  
将一个cmd命令行字符串解析成命令包,字符串中包含转义"\"时,请务必在字符串前加r,否则无法正确解析  
带有空格和"-"的参数值请用双引号包裹,双引号内需要出现双引号的请用斜杠转义 \"  
r"filed -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float"  

相当于我们在一条路上走,走一会捡到一个字母。  
假设我们有两个篓子,一个是用来装命令的,一个是用来装命令的值的。  
当我们碰到一个横杠,就打开命令背篓的盖子+值背篓的盖子,然后逐个往命令背篓里面装,当碰到空格时,我们就把背篓的盖子关上。  
然后我们把接下来非空的字符放到值背篓里去,直到碰到下一个横杠。  
当碰到下一个横杆时,我们检查一下两个背篓里的东西,然后把它们存到仓库里去,清空背篓,开始继续捡东西。  
当我们捡到路的尽头,我们检查一下两个背篓里的东西,然后把它们存到仓库里去,任务完成。  
大体的处理方式就是这样,具体的程序里面有加了一些 命令符判定,引号判定等细节,具体请看代码  



****
###　　　　　　　　　 Author:boois 萧鸣
###　　　　　　　　　 E-mail:boois@qq.com

===========================

####计划:

后续我将会在本项目中扩展同样的功能的各语言版本:   

1. js,
*  php
* object-c
* ruby
* dotnet
* java

####关于boois_cmd_parser的一些应用方式:

1. 用于前端做文本校验或配置,如对每个input的值做前端的校验: account -l 4,24  就可以代表 account这个输入框只能输入4-24位的文字
* 用于后端做post 和 get 的后端校验配置
* 用于 app 端 向服务器拉取一些简单的配置
* 用于 作为web后台的模拟命令行方式来操作一些例如清理缓存,备份文件等不需要ui的操作。
* 其他的再想想 :)

####2016.1.24新增:

1. vali_rule_chker.ValiRuleInfo
  cmd :
    field (the first word)
    -i foo (ValiRuleInfo.info)
    -w foo (ValiRuleInfo.waring)
    -t foo (ValiRuleInfo.type)
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
    -r foo (ValiRuleInfo.regx)
        "mobi": r"^0?(13|14|15|18|17)[0-9]{9}$",
        "email": r"^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]*\.)+[A-Za-z]{2,14}$",
        "zip_code": r"^\d{6}$",
        "phone": r"^\d+$|^\d{4}[\s-]\d+$|^\+{0,1}86[\s-]\d{4}[\s-]\d+$",
        "account": r"^[a-zA-Z][0-9a-zA-Z_]*$",
        "passwd": r"^[a-zA-Z][0-9a-zA-Z_]*$",
        "nickname": u"^[\u4e00-\u9fa5_0-9a-zA-Z-]*$",
        "qq": r"^[1-9][0-9]{4,}$",
        "id_card": r"^(\d{15}$|^\d{18}$|^\d{17}(\d|X|x))$",
        "ip": r"^((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))$",
        "url": r"^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]*",
        "zh": u"^[\u4e00-\u9fa5]*$",  # 仅为中文,这里有个要点,中文匹配必须正则规则也使用u编码,否则无法匹配
    -n  (ValiRuleInfo.requried)
    -v 1|2|3|4 (ValiRuleInfo.values)
`info = ValiRuleInfo(r'field -i test%s123123 -n -l 1,5 -r "mobi" -t "-int|+float" -w "haha,your got it -v 1|2|3"')`

1. vali_rule_chker.ValiRuleChker
`chker = ValiRuleChker(r'field -i test%s123123 -n -l 1,5 -r "mobi" -t "-int|+float" -w "haha,your got it -v 1|2|3"')
 msg, info = chker.chk("foo")
 print chker.is_validated`
