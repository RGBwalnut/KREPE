#! /usr/bin/env python3

#from Bio.Seq import Seq
import numpy as np
import os
import random
#import matplotlib.pyplot as plt
import math
#import pandas as pd
#import struct
import mmh3 
from bitarray import bitarray
import sys
#These are packages I think we might need so I am just putting them at the top

'''-----------------------------Work in Progress---------------------------------------------'''

#Working on bloom filter class
kmer_length=int(sys.argv[1])
fasta_path=sys.argv[2]
fp=float(sys.argv[3])
kmer_list=[]

def main():
    number_of_kmers = 0
    #kmer_length=int(input("Enter Kmer Lengths: "))
    #fasta_path=input("File path (FASTA FORMAT): ")
    txt_path = fasta_path
    wrong_extension='.fasta'
    for character in wrong_extension:
        txt_path=txt_path.replace(character, "")
    cmd = f"grep -v 'length=' {fasta_path} > {txt_path}.txt" 
    os.system(cmd)

    occurrence_dict = {}
    with open(f'{txt_path}.txt', 'r') as file:
        os.system('date --iso=seconds')
        txt_file = file.read().replace('\n', '')
        os.system('date --iso=seconds')
        character_count=len(txt_file)-int(kmer_length)
        for i in range(character_count):
            number_of_kmers=number_of_kmers + 1
            kmers= txt_file[i:(i + kmer_length)]
            if not kmers in occurrence_dict:
                occurrence_dict[kmers] = 1
            else:
                occurrence_dict[kmers] += 1
            kmer_list.append(kmers)
        os.system('date --iso=seconds')
    if len(occurrence_dict.keys()) < 100:
        print(occurrence_dict)
    else:
        print('[very big occurrence dict]')
    print(4**kmer_length, len(occurrence_dict.keys()))
    # list_of_keys_with_more_than_one_occurrence = []
    key_list = list(occurrence_dict.keys())
    for key in key_list:
        if occurrence_dict[key] < 2:
            # list_of_keys_with_more_than_one_occurrence.append(key)
            occurrence_dict.pop(key)
    print('======================================================')
    if len(occurrence_dict.keys()) < 100:
        print(occurrence_dict)
    else:
        print('[very big occurrence dict]')
    print(4**kmer_length, len(occurrence_dict.keys()))
    # print(list_of_keys_with_more_than_one_occurrence)
    # hash_funcs, bloomeyfilter, total_bits = bloomfilter(number_of_kmers, fp)
    # print('h/t are:', hash_funcs, total_bits)
    # os.system('date --iso=seconds')
    # hashing(kmer_list, bloomeyfilter, total_bits)
    # os.system('date --iso=seconds')
    # #print(kmer_counting_dictionary)
    # #print(number_of_kmers, total_bits, kmer_counting_dictionary)
    # print(total_bits)
    # #print(hash_funcs)
    # print(kmer_counting_dictionary)
    # # print(bloomeyfilter)
    
def bloomfilter(number_of_kmers, fp):
    #inserted_kmers=len(set(kmer_list))
    total_bits=int(abs(math.ceil(number_of_kmers*(1.44*(math.log(fp, 2))))))
    bloomeyfilter = bitarray(total_bits)
    bloomeyfilter.setall(0)
    hash_funcs=math.ceil(total_bits / number_of_kmers) * np.log(2)
    return hash_funcs, bloomeyfilter, total_bits


def hashing(kmer_list, bloomeyfilter, total_bits):
    global kmer_counting_dictionary
    kmer_counting_dictionary={}
    for i in range(len(kmer_list)):
        hash_key=int(abs(mmh3.hash(kmer_list[(i)]))) % total_bits
        kmer_counting_dictionary.update({kmer_list[i]: 1})
        if bloomeyfilter[hash_key:(hash_key + 1)] == bitarray('0'):
            bloomeyfilter[hash_key:(hash_key + 1)] = bitarray('1')
        else:
            new_value=kmer_counting_dictionary.get(kmer_list[i], 0) + 1
            kmer_counting_dictionary.update({kmer_list[i] : new_value})
    return kmer_counting_dictionary


if __name__ == '__main__':
    main()
# #txt_file= str(open(f'{txt_path}.txt', 'w'))
#     #now the counting begins
#     #blomfilter = BloomFilter()


# '''

        
# Useful for dealing with bits and filiping them, uses struct packages, probablt needs to be tinkered on, those functions at the bottom are from a previous project I have done

# def float_to_bin(num):
#     """Given a float, return a string with the individual bits"""
#     result = format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')
#     return result

# def bin_to_float(binary):
#     return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]
#python already has a hash function so we can use that with our bloom filter

# def bitflip(x, pos):
#      fs = pack('f',x)
#      bval = list(unpack('BBBB',fs))
#      [q,r] = divmod(pos,8)
#      bval[q] ^= 1 << r
#      fs = pack('BBBB', *bval)
#      fnew=unpack('f',fs)
#      return fnew[0]