from flakes.string.string_kernel import StringKernel
import numpy as np
import random
import datetime as dt
import string
import os
import argparse

#SLENS = range(10, 101, 10)
SLENS = range(5, 21, 5)
ALPHABET = string.ascii_letters
COEFS = [1.0] * 5


def get_time(data, mode):
    sk = StringKernel(order_coefs=COEFS, alphabet=list(ALPHABET), mode=mode)
    before = dt.datetime.now()
    sk.K(data)
    after = dt.datetime.now()
    return (after-before).total_seconds()


def main(args):
    sk_times = []
    vsk_times = []
    if args.gpu is not None:
        vsk_gpu_times = []
    
    for slen in SLENS:
        # Generate random instances
        data = [[''.join([random.choice(ALPHABET) for j in range(slen)])] for i in range(100)]

        # Default SK
        sk_times.append(get_time(data, 'cynaive'))

        # VSK (Numpy version)
        vsk_times.append(get_time(data, 'numpy'))

        # VSK GPU (TensorFlow version)
        if args.gpu is not None:
            vsk_gpu_times.append(get_time(data, 'tf'))

    os.makedirs(args.results, exist_ok=True)
    np.savetxt(os.path.join(args.results, 'sk.tsv'), sk_times)
    np.savetxt(os.path.join(args.results, 'vsk.tsv'), vsk_times)
    if args.gpu is not None:
        np.savetxt(os.path.join(args.results, 'vsk_gpu.tsv'), vsk_gpu_times)


if __name__ == "__main__":
    random.seed(1000)
    parser = argparse.ArgumentParser(description='Run SK performance experiments')
    parser.add_argument('results', type=str, help="Folder where to store results")
    parser.add_argument('--gpu', type=int, default=None, help="Whether to include GPU results or not. Th number is GPU id where to perform the experiments.")
    args = parser.parse_args()
    main(args)
