#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys


ERRMSG1 = 'Range of IP address is invalid. '
ERRMSG2 = 'The specified IP address is not suitable as CIDR. '
ERRMSG3 = 'Maybe around here({0} - {1}). '


def getCidrIpRange(ip1, ip2):
    u"""getCidrIpRange IPアドレスの範囲からCIDRを求める
    """
    rangedict = {0: 0, 1: 1, 3: 2, 7: 3, 15: 4, 31: 5, 63: 6, 127: 7, 255: 8}
    cl = [0, 0, 0, 0]

    a1, a2 = splitIPaddr(ip1, ip2)
    for i in range(len(cl)):
        if subtList(a2, a1, i) in rangedict:
            cl[i] = 8 - rangedict[subtList(a2, a1, i)]
        else:
            msg = (ERRMSG1 + ERRMSG2 + ERRMSG3).format(a1[i], a2[i])
            print msg
            sys.exit()

    mb = sumList(cl)
    return mb


def sumList(list):
    u"""sumList リストの各要素を全て合計
    """
    s = 0
    for v in list:
        s += v
    return s


def subtList(la, lb, idx):
    u"""subtList 2つのリストを受け取り、指定要素の値を減算し結果を返却
    ※第1パラメータ - 第2パラメータ(la - lb)
    ※リストの長さが同じであること
    """

    if not len(la) == len(lb):
        print 'list size error'
        return None

    if len(la) < idx:
        print 'index error'
        return None

    return int(la[idx]) - int(lb[idx])


def subtListall(la, lb):
    u"""subtListall 2つのリストを受け取り、全ての各要素の値を減算し結果をリストで返却
    ※第1パラメータ - 第2パラメータ(la - lb)
    ※リストの長さが同じであること
    """

    if not len(la) == len(lb):
        return None

    return [x - y for (x, y) in zip(la, lb)]


def splitIPaddr(ip1, ip2):
    u"""splitIPaddr IPアドレスをリストに分割
    パラメータでIPアドレスを受け取り(2個)それぞれを表記チェック
    表記に問題なければ「.」でIPアドレスを分割してリストで返却
    """

    if not checkIPaddr(ip1):
        print 'parameter ipaddr1 error ' + ip1

    if not checkIPaddr(ip2):
        print 'parameter ipaddr2 error ' + ip2

    li1 = ip1.split('.')
    li2 = ip2.split('.')

    return (li1, li2)


def checkIPaddr(ip):
    u"""checkIPaddr IPアドレスの表記チェック
    """
    re_str = r'^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}'
    re_str = re_str + r'([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    re_addr = re.compile(re_str)
    mach = re_addr.match(ip)
    if mach is not None:
        return True
    else:
        return False


def getParam_getcidr(argv):
    u"""getParam コマンドラインパラメータからIPアドレスを取得
    OK: ipaddr1 ipaddr2
    OK: ipaddr1 - ipaddr2
    """
    ip = []
    for v in argv:
        v = v.strip()
        if checkIPaddr(v):
            ip.append(v)
            if len(ip) >= 2:
                break
    else:
        if len(ip) < 2:
            print 'parameter error. getcidr need is 2 parameters(Ip address)'
            sys.exit()

    return tuple(ip)


def getCidr(*argv):
    ip1, ip2 = getParam_getcidr(argv[0])
    maskbit = getCidrIpRange(ip1, ip2)
    return ip1 + '/' + str(maskbit)

if __name__ == "__main__":
    param = sys.argv
    print getCidr(param)
