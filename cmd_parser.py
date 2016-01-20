# coding:utf-8
'''
萧鸣-原创:boois@qq.com 2016.1.21
本模块用于将一串命令行字符串解析成命令组
filed -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float
=> ('filed', {'i': 't', 'r': '/mo\\"-bi/gi', 'l': '1', 't': '-int|+float'})
'''
#TODO Please translate into English


def cmd_parse(cmd_str, is_print=False):
    """
    将一个cmd命令行字符串解析成命令包,字符串中包含转义"\"时,请务必在字符串前加r,否则无法正确解析
    带有空格和"-"的参数值请用双引号包裹,双引号内需要出现双引号的请用斜杠转义 \"
    r"filed -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float"
    :param cmd_str: 命令字符串
    :param is_print: 是否print遍历过程
    :return: ("命令名称",{命令字典})
    """
    # 相当于我们在一条路上走,走一会捡到一个字母。
    # 假设我们有两个篓子,一个是用来装命令的,一个是用来装命令的值的。
    # 当我们碰到一个横杆,就打开命令背篓的盖子+值背篓的盖子,然后逐个往命令背篓里面装,当碰到空格时,我们就把背篓的盖子关上。
    # 然后我们把接下来非空的字符放到值背篓里去,直到碰到下一个横杆。
    # 当碰到下一个横杆时,我们检查一下两个背篓里的东西,然后把它们存到仓库里去,清空背篓,开始继续捡东西。
    # 当我们捡到路的尽头,我们检查一下两个背篓里的东西,然后把它们存到仓库里去,任务完成。
    cmd_store = {}  # 用来保存命令的仓库
    last_char = ""  # 上一个字符,如果碰到"-",要和前面的空格搭配在一起才表示是命令开始
    is_start = False  # 表示开始碰到第一个字符,用来过滤掉刚开始的一段空白的路
    is_cmd_start = False  # 表示开始碰到第一个横杆字符,表示正式地收集命令参数了
    field = []  # 碰到第一个横杠之前的所有有效字符将被认为是我们的主命令名称,也就是我们的字段名
    cmd_bag = []  # 命令背篓
    cmd_bag_is_open = False  # 命令背篓是否开启
    val_bag = []  # 值背篓
    val_bag_is_open = False  # 值背篓是否开启
    qout_start = False  # 表示是否之前有一个引号没有关闭,如果上一个字符是斜杠,则不判定为引号
    is_cmd_char = False  # 表示当前的-是不是命令符,只有空格+横杆为命令符,如果包含在双引号内就不是命令符
    for i in xrange(len(cmd_str)):  # 逐个字符流状读取
        if is_print:
            print "捡到一个:|" + cmd_str[i] + "|"
        is_cmd_char = last_char == " " and cmd_str[i] == "-" and not qout_start  # 带空格的横杆,并且引号是闭合的
        if is_print:
            if is_cmd_char:
                print "当前的-是一个命令符"
        if qout_start:  # 如果之前已经有一个引号了
            if last_char != "\\" and cmd_str[i] == "\"":  # 当前还是一个引号
                qout_start = False  # 表示引号已经闭合了
        elif last_char != "\\" and cmd_str[i] == "\"":  # 如果之前不是引号，当前却是引号
            qout_start = True  # 表示引号等待闭合

        if not is_start and cmd_str[i] != " ":  # 还没开始时,碰到第一个非空字符
            is_start = True  # 一切都开始了
            if is_print:
                print "开始捡东西了!"

        if is_print:
            print ("---还没开始捡呢,先放着!" if not is_start else "")

        if is_start and not is_cmd_start and cmd_str[i] != " " and not is_cmd_char:  # 开始收集field,并且命令还没开始收集
            field.append(cmd_str[i])
        if not is_cmd_start and is_cmd_char:  # 碰到第一个横杆,表示正式开始收集命令啦
            if is_print:
                print field, "创建field"
                print "命令收集开始了"

            is_cmd_start = True  # 命令收集开始了

        # 如果命令背篓关了,值背篓是开的,就往值背篓里面放
        if not cmd_bag_is_open and val_bag_is_open:
            if cmd_str[i] != " " and not is_cmd_char and cmd_str[i] !="\"":  # 只要不是空格、引号和命令符就往里面放
                val_bag.append(cmd_str[i])
            elif cmd_str[i] == "\"" and last_char == "\\":
                val_bag.append(cmd_str[i])
            elif not qout_start:  # 一碰到空格,就把值背篓盖上
                val_bag_is_open = False
                if is_print:
                    print "碰到空格,val_bg关闭了"

        # 如果命令背篓是开着的,就往命令背篓里面放
        if cmd_bag_is_open:
            if cmd_str[i] != " " and not is_cmd_char:  # 只要不是空格和横杠就往里面放
                cmd_bag.append(cmd_str[i])
            else:  # 一碰到空格,就把命令背篓盖上
                cmd_bag_is_open = False
                if is_print:
                    print "碰到空格,cmd_bg关闭了"

        # 如果碰到一个命令符,就检查一下自己的背包是不是有东西,有东西就处理掉,然后把背包清空,盖子打开
        if is_cmd_char:
            if cmd_bag:
                if is_print:
                    print cmd_bag, "倾倒cmd_bg"
                    print val_bag, "倾倒val_bag"
                cmd_store["".join(cmd_bag)] = "".join(val_bag)
            cmd_bag = []
            cmd_bag_is_open = True
            if is_print:
                print "cmd_bg打开了"

            val_bag = []
            val_bag_is_open = True
            if is_print:
                print "val_bag打开了"

        if i == len(cmd_str) - 1:  # 走到了路的尽头,一切都结束了
            if cmd_bag:
                if is_print:
                    print cmd_bag, "倾倒cmd_bg"
                    print val_bag, "倾倒val_bag"
                cmd_store["".join(cmd_bag)] = "".join(val_bag)
            cmd_bag = []
            cmd_bag_is_open = False
            if is_print:
                print "一切都结束了,cmd_bg永远地关闭了"
            val_bag = []
            val_bag_is_open = False
            if is_print:
                print "一切都结束了,val_bag永远地关闭了"
        last_char = cmd_str[i]
    return "".join(field), cmd_store


if __name__ == "__main__":

    print cmd_parse(r' filed -i test%s123123 -n -l 1,4 -r "/mo\" -bi/gi" -t "-int|+float"',False)
    print cmd_parse(r'python -h',False)
    print cmd_parse(r'python -i love u u u -name u',False)
