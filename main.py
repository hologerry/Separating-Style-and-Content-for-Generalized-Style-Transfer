import json
from train import train
from test import test
import random
import os
import tensorflow as tf
import numpy as np
from model import a


def main():
    if tf.gfile.Exists(a.output_dir):
        tf.gfile.DeleteRecursively(a.output_dir)
        tf.gfile.MakeDirs(a.output_dir)

    if a.seed is None:
        a.seed = random.randint(0, 2**31 - 1)

    tf.set_random_seed(a.seed)
    np.random.seed(a.seed)
    random.seed(a.seed)

    if not os.path.exists(a.output_dir):
        os.makedirs(a.output_dir)

    for k, v in a._get_kwargs():
        print(k, "=", v)

    with open(os.path.join(a.output_dir, "options.json"), "w") as f:
        f.write(json.dumps(vars(a), sort_keys=True, indent=4))

    if a.mode == "train":
        train()
    elif a.mode == 'test':
        test()


main()
