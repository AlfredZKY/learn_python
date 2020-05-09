strs = [
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-0170db1f394b35d995252228ee359194b13199d259380541dc529fb0099096b0.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-0170db1f394b35d995252228ee359194b13199d259380541dc529fb0099096b0.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-0170db1f394b35d995252228ee359194b13199d259380541dc529fb0099096b0.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-0cfb4f178bbb71cf2ecfcd42accce558b27199ab4fb59cb78f2483fe21ef36d9.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-0cfb4f178bbb71cf2ecfcd42accce558b27199ab4fb59cb78f2483fe21ef36d9.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-0cfb4f178bbb71cf2ecfcd42accce558b27199ab4fb59cb78f2483fe21ef36d9.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-3ea05428c9d11689f23529cde32fd30aabd50f7d2c93657c1d3650bca3e8ea9e.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-3ea05428c9d11689f23529cde32fd30aabd50f7d2c93657c1d3650bca3e8ea9e.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-3ea05428c9d11689f23529cde32fd30aabd50f7d2c93657c1d3650bca3e8ea9e.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-50c7368dea9593ed0989e70974d28024efa9d156d585b7eea1be22b2e753f331.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-50c7368dea9593ed0989e70974d28024efa9d156d585b7eea1be22b2e753f331.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-50c7368dea9593ed0989e70974d28024efa9d156d585b7eea1be22b2e753f331.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-5294475db5237a2e83c3e52fd6c2b03859a1831d45ed08c4f35dbf9a803165a9.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-5294475db5237a2e83c3e52fd6c2b03859a1831d45ed08c4f35dbf9a803165a9.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-5294475db5237a2e83c3e52fd6c2b03859a1831d45ed08c4f35dbf9a803165a9.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-7d739b8cf60f1b0709eeebee7730e297683552e4b69cab6984ec0285663c5781.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-7d739b8cf60f1b0709eeebee7730e297683552e4b69cab6984ec0285663c5781.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-7d739b8cf60f1b0709eeebee7730e297683552e4b69cab6984ec0285663c5781.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-0377ded656c6f524f1618760bffe4e0a1c51d5a70c4509eedae8a27555733edc.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-0377ded656c6f524f1618760bffe4e0a1c51d5a70c4509eedae8a27555733edc.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-0377ded656c6f524f1618760bffe4e0a1c51d5a70c4509eedae8a27555733edc.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-559e581f022bb4e4ec6e719e563bf0e026ad6de42e56c18714a2c692b1b88d7e.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-559e581f022bb4e4ec6e719e563bf0e026ad6de42e56c18714a2c692b1b88d7e.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-proof-of-spacetime-fallback-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-559e581f022bb4e4ec6e719e563bf0e026ad6de42e56c18714a2c692b1b88d7e.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-840969a6a9533823ecdc37310ef8c99d35991a2145300e10be0b883f1226a0f6.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-840969a6a9533823ecdc37310ef8c99d35991a2145300e10be0b883f1226a0f6.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-840969a6a9533823ecdc37310ef8c99d35991a2145300e10be0b883f1226a0f6.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-e3c3fd959a83bf60522a401dc3bf0e2d48f0e2172bcdf4c0cb3c39fa4deacd87.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-e3c3fd959a83bf60522a401dc3bf0e2d48f0e2172bcdf4c0cb3c39fa4deacd87.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-e3c3fd959a83bf60522a401dc3bf0e2d48f0e2172bcdf4c0cb3c39fa4deacd87.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-e4a49558d04647264048879511e843136e4488499e23bc442a341083a19ee79c.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-e4a49558d04647264048879511e843136e4488499e23bc442a341083a19ee79c.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%200%2C%200%3E-Sha256Hasher-e4a49558d04647264048879511e843136e4488499e23bc442a341083a19ee79c.vk",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-Sha256Hasher-8a0719d8b9de3605f89b084c73210dfe2a557407c6343f8d32640094f2c9d074.meta",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-Sha256Hasher-8a0719d8b9de3605f89b084c73210dfe2a557407c6343f8d32640094f2c9d074.params",
"https://cs-cn-filecoin.oss-cn-beijing.aliyuncs.com/testnet3/proof_params/v25/v25-stacked-proof-of-replication-MerkleTree%3CPoseidonHasher%2C%208%2C%208%2C%200%3E-Sha256Hasher-8a0719d8b9de3605f89b084c73210dfe2a557407c6343f8d32640094f2c9d074.vk"]

from multiprocessing import Process
import os
import subprocess
def run_proc(name):
    cmd = 'wget ' + name
    subprocess.call(cmd,shell=True)
 
if __name__ == '__main__':
    for item in strs:
        print('Parent process %s.' % os.getpid())
        p = Process(target = run_proc, args = (item, ))
        p.start()
        p.join()
        print("End!!!")

