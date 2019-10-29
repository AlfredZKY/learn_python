import rlp
import sys
sys.path.append('./src')

test_list = ["zky",
             chr(0),
             chr(126),
             "The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog",
             ["Peter Piper picked a peck of pickled peppers",
              "Betty Botter bought some butter"],
             '']

for test in test_list:
    if isinstance(test, list):
        for s in test:
            print("original string in list :" + s)
            print("original string in list :" + hex(len(s)))
    else:
        print("original string :" + test)
        print("original string length: " + hex(len(test)))
    print("after encode : 0x" + rlp.encode(test).encode('hex'))
