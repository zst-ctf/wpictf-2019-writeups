# uncompyle6 version 3.3.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.0 (default, Oct  2 2018, 09:20:07) 
# [Clang 10.0.0 (clang-1000.11.45.2)]
# Embedded file name: ./jocipher.py
# Compiled at: 2019-03-02 01:41:21
import argparse, re
num = ''
first = ''
second = ''
third = ''

def setup():
    global first
    global num
    global second
    global third
    num += '1'
    num += '2'
    num += '3'
    num += '4'
    num += '5'
    num += '6'
    num += '7'
    num += '8'
    num += '9'
    num += '0'
    first += 'q'
    first += 'w'
    first += 'e'
    first += 'r'
    first += 't'
    first += 'y'
    first += 'u'
    first += 'i'
    first += 'o'
    first += 'p'
    second += 'a'
    second += 's'
    second += 'd'
    second += 'f'
    second += 'g'
    second += 'h'
    second += 'j'
    second += 'k'
    second += 'l'
    third += 'z'
    third += 'x'
    third += 'c'
    third += 'v'
    third += 'b'
    third += 'n'
    third += 'm'


def encode(string, shift):
    result = ''
    for i in range(len(string)):
        char = string.lower()[i]
        if char in num:
            new_char = num[(num.index(char) + shift) % len(num)]
            result += new_char
        elif char in first:
            new_char = first[(first.index(char) + shift) % len(first)]
            if string[i].isupper():
                result += new_char.upper()
            else:
                result += new_char
        elif char in second:
            new_char = second[(second.index(char) + shift) % len(second)]
            if string[i].isupper():
                result += new_char.upper()
            else:
                result += new_char
        elif char in third:
            new_char = third[(third.index(char) + shift) % len(third)]
            if string[i].isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char

    print result
    return 0


def decode(string, shift):
    result = ''
    shift = -1 * shift
    for i in range(len(string)):
        char = string.lower()[i]
        if char in num:
            new_char = num[(num.index(char) + shift) % len(num)]
            result += new_char
        elif char in first:
            new_char = first[(first.index(char) + shift) % len(first)]
            if string[i].isupper():
                result += new_char.upper()
            else:
                result += new_char
        elif char in second:
            new_char = second[(second.index(char) + shift) % len(second)]
            if string[i].isupper():
                result += new_char.upper()
            else:
                result += new_char
        elif char in third:
            new_char = third[(third.index(char) + shift) % len(third)]
            if string[i].isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char

    print result
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', '-s', type=str, required=True, help='the string to encode or decode')
    parser.add_argument('--shift', '-t', type=int, required=True, help='the shift value to use')
    parser.add_argument('--encode', '-e', required=False, action='store_true', help='encode the string')
    parser.add_argument('--decode', '-d', required=False, action='store_true', help='decode the string')
    args = parser.parse_args()
    setup()
    p = re.compile('[a-zA-Z0-9\\-{}]')
    if p.match(args.string) is not None:
        if args.encode:
            ret = encode(args.string, args.shift)
        else:
            if args.decode:
                ret = decode(args.string, args.shift)
        if ret is not 0:
            print 'Sorry, this cipher only uses the [a-zA-Z0-9\\-{}]'
    else:
        print 'Sorry, this cipher only uses the [a-zA-Z0-9\\-{}]'
    return


if __name__ == '__main__':
    main()
# okay decompiling jocipher.pyc
