boois_cmd_parser
===========================
a python program for parse a cmd_str to tuple ,r' cmd_name -foo value -bar "value" -baz "value\"value" ' to ("cmd_name",{"foo","value"})  
���ļ�ȡ��Ϊ`boois_cmd_parser`,�ҵ�һЩ��صĴ���Ҳ����`boois`��Ϊǰ׺  
���ļ��ò�������ַ���ʽ��ȡ����һ������ linux �����е��ַ�ת��Ϊһ��tuple ("��������",{"����1","ֵ"...})  
���ǲ��÷ָ����������ʽ������,���ǲ������ƽ������ķ�ʽ,����ֽڶ�ȡ�鼯  
  
��һ��cmd�������ַ��������������,�ַ����а���ת��"\"ʱ,��������ַ���ǰ��r,�����޷���ȷ����  
���пո��"-"�Ĳ���ֵ����˫���Ű���,˫��������Ҫ����˫���ŵ�����б��ת�� \"  
r"filed -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float"  

�൱��������һ��·����,��һ���һ����ĸ��  
��������������¨��,һ��������װ�����,һ��������װ�����ֵ�ġ�  
����������һ�����,�ʹ����¨�ĸ���+ֵ��¨�ĸ���,Ȼ����������¨����װ,�������ո�ʱ,���ǾͰѱ�¨�ĸ��ӹ��ϡ�  
Ȼ�����ǰѽ������ǿյ��ַ��ŵ�ֵ��¨��ȥ,ֱ��������һ����ܡ�  
��������һ�����ʱ,���Ǽ��һ��������¨��Ķ���,Ȼ������Ǵ浽�ֿ���ȥ,��ձ�¨,��ʼ����������  
�����Ǽ�·�ľ�ͷ,���Ǽ��һ��������¨��Ķ���,Ȼ������Ǵ浽�ֿ���ȥ,������ɡ�  
����Ĵ���ʽ��������,����ĳ��������м���һЩ ������ж�,�����ж���ϸ��,�����뿴����  



****
###������������������ Author:boois ����
###������������������ E-mail:boois@qq.com

===========================

####�ƻ�:

�����ҽ����ڱ���Ŀ����չͬ���Ĺ��ܵĸ����԰汾:   

1. js,
*  php
* object-c
* ruby
* dotnet
* java

####����boois_cmd_parser��һЩӦ�÷�ʽ:

1. ����ǰ�����ı�У�������,���ÿ��input��ֵ��ǰ�˵�У��: account -l 4,24  �Ϳ��Դ��� account��������ֻ������4-24λ������
* ���ں����post �� get �ĺ��У������
* ���� app �� ���������ȡһЩ�򵥵�����
* ���� ��Ϊweb��̨��ģ�������з�ʽ������һЩ����������,�����ļ��Ȳ���Ҫui�Ĳ�����
* ������������ :)

####2016.1.24����:

1. vali_rule_chker.ValiRuleInfo
  cmd :
    field (the first word)
    -i foo (ValiRuleInfo.info)
    -w foo (ValiRuleInfo.waring)
    -t foo (ValiRuleInfo.type)
        INT = 1 << 0  # ����
        P_INT = 1 << 1  # ������ positive integer
        N_INT = 1 << 2  # ������ negative integer
        FLOAT = 1 << 3  # С��
        P_FLOAT = 1 << 4  # ��С�� ������С����,����������
        N_FLOAT = 1 << 5  # ��С�� ������С����,���ݸ�����
        BOOL = 1 << 6  # ����ֵ true|false|0|1 ��Сд������
        INT_LIST = 1 << 7  # �������� 1,2,3,4,5
        STR_LIST = 1 << 8  # �ַ������� a,b,c,d,e
        DICT = 1 << 9  # �ֵ� "a":"foo",b:"bar","c":"baz","d":"qux",������˫���Ž�kv��������
        JSON = 1 << 10  # ��ͨ�� json.loads(foo)���ַ���
        GUID_LIST = 1 << 11  # 32λ�޺���GUID,36λ�к���GUID,..
        FLOAT_LIST = 1 << 12  # С����ϳɵ��б�
        ZERO = 1 << 13  # ��
        STR = 1 << 14  # �����ַ�
        GUID = 1 << 15  # 32λ�޺���GUID,36λ�к���GUID
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
        "zh": u"^[\u4e00-\u9fa5]*$",  # ��Ϊ����,�����и�Ҫ��,����ƥ������������Ҳʹ��u����,�����޷�ƥ��
    -n  (ValiRuleInfo.requried)
    -v 1|2|3|4 (ValiRuleInfo.values)
`info = ValiRuleInfo(r'field -i test%s123123 -n -l 1,5 -r "mobi" -t "-int|+float" -w "haha,your got it -v 1|2|3"')`

1. vali_rule_chker.ValiRuleChker
`chker = ValiRuleChker(r'field -i test%s123123 -n -l 1,5 -r "mobi" -t "-int|+float" -w "haha,your got it -v 1|2|3"')
 msg, info = chker.chk("foo")
 print chker.is_validated`
