#!/usr/bin/env python3
import itertools
import hashlib
import string

charset = string.ascii_lowercase


def find_pt(starting, target_hash, repeat):
    for p in itertools.product(charset, repeat=repeat):
        text = starting + ''.join(p)
        m = hashlib.sha3_256()
        m.update(text.encode("utf-8"))
        my_hash = str(m.hexdigest())

        if my_hash == target_hash:
            return text

        print("Trying:", text)

starting = 'wpictf2019powSOJ8I662GM'
target_hash = '948b7e445051681c3c4e506277274b5ec4080a47269b03a09adca1a7f8ef3755'
repeat = 5
print('Found:', find_pt(starting, target_hash, repeat))
