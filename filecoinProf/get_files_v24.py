strs = [
"v24-proof-of-spacetime-election-PoseidonHasher-0b0b9781bcb153efbb3cab4be3a792c4f555d4ab6f8dd62b27e1dcad08a34f22.meta",
"v24-proof-of-spacetime-election-PoseidonHasher-0b0b9781bcb153efbb3cab4be3a792c4f555d4ab6f8dd62b27e1dcad08a34f22.params",
"v24-proof-of-spacetime-election-PoseidonHasher-0b0b9781bcb153efbb3cab4be3a792c4f555d4ab6f8dd62b27e1dcad08a34f22.vk",
"v24-proof-of-spacetime-election-PoseidonHasher-0b499a953f1a9dcab420b3ba1e6b1f3952dc7f17cf67ed10406ae9a43e2b8ec5.meta",
"v24-proof-of-spacetime-election-PoseidonHasher-0b499a953f1a9dcab420b3ba1e6b1f3952dc7f17cf67ed10406ae9a43e2b8ec5.params",
"v24-proof-of-spacetime-election-PoseidonHasher-0b499a953f1a9dcab420b3ba1e6b1f3952dc7f17cf67ed10406ae9a43e2b8ec5.vk",
"v24-proof-of-spacetime-election-PoseidonHasher-27a7fc680a47e4821f40cf1676fb80b9888820ef6867a71a175b4c9ae068ad3f.meta",
"v24-proof-of-spacetime-election-PoseidonHasher-27a7fc680a47e4821f40cf1676fb80b9888820ef6867a71a175b4c9ae068ad3f.params",
"v24-proof-of-spacetime-election-PoseidonHasher-27a7fc680a47e4821f40cf1676fb80b9888820ef6867a71a175b4c9ae068ad3f.vk",
"v24-proof-of-spacetime-election-PoseidonHasher-5916054ae98e28fc2f0470d1fb58eb875a6865be86f0b8c4e302d55f13217fef.meta",
"v24-proof-of-spacetime-election-PoseidonHasher-5916054ae98e28fc2f0470d1fb58eb875a6865be86f0b8c4e302d55f13217fef.params",
"v24-proof-of-spacetime-election-PoseidonHasher-5916054ae98e28fc2f0470d1fb58eb875a6865be86f0b8c4e302d55f13217fef.vk",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-49442c8ce7545579cbd689d578301d0cc1e46e94e2499a0ec36de7ff4f4694a2.meta",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-49442c8ce7545579cbd689d578301d0cc1e46e94e2499a0ec36de7ff4f4694a2.params",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-49442c8ce7545579cbd689d578301d0cc1e46e94e2499a0ec36de7ff4f4694a2.vk",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-d84aa4581c74190f845596893ebe5b71da32ecf16e1d151b9fff74ee8f94d77c.meta",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-d84aa4581c74190f845596893ebe5b71da32ecf16e1d151b9fff74ee8f94d77c.params",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-d84aa4581c74190f845596893ebe5b71da32ecf16e1d151b9fff74ee8f94d77c.vk",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-fc32be6028c2398175466f36fa36810842ae8948fae15c84454af5b61ca99e15.meta",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-fc32be6028c2398175466f36fa36810842ae8948fae15c84454af5b61ca99e15.params",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-fc32be6028c2398175466f36fa36810842ae8948fae15c84454af5b61ca99e15.vk",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-fe437922fe766f61b112750506d6be0e4ad5daa85ff9ce96549d99253ba61cbe.meta",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-fe437922fe766f61b112750506d6be0e4ad5daa85ff9ce96549d99253ba61cbe.params",
"v24-stacked-proof-of-replication-PoseidonHasher-Sha256Hasher-fe437922fe766f61b112750506d6be0e4ad5daa85ff9ce96549d99253ba61cbe.vk",
]



from multiprocessing import Process
import os
import subprocess
url = "https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v24/filecoin-proof-parameters_32GiB/"
def run_proc(name):
    cmd = 'wget ' + url + name
    subprocess.call(cmd,shell=True)
 
if __name__ == '__main__':
    for item in strs:
        print('Parent process %s.' % os.getpid())
        p = Process(target = run_proc, args = (item, ))
        p.start()
        p.join()
        print("End!!!")

