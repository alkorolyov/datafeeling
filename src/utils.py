import os
import random
import numpy as np

import torch
import tensorflow as tf

DEFAULT_RANDOM_SEED = 42
def set_all_seeds(seed=DEFAULT_RANDOM_SEED):
    # python seeds
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

    # torch seeds
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    # tensorflow seeds
    tf.random.set_seed(seed)