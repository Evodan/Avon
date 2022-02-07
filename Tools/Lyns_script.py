# all the imports

import glob
import logging
import os
import pickle
import random
import re
import shutil
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset, RandomSampler, SequentialSampler
from torch.utils.data.distributed import DistributedSampler
from tqdm.notebook import tqdm, trange

from pathlib import Path

from transformers import (
    MODEL_WITH_LM_HEAD_MAPPING,
    WEIGHTS_NAME,
    AdamW,
    AutoConfig,
    PreTrainedModel,
    PreTrainedTokenizer,
    get_linear_schedule_with_warmup,
)

try:
    from torch.utils.tensorboard import SummaryWriter
except ImportError:
    from tensorboardX import SummaryWriter

data = pd.read_csv('NewScript.txt', sep=':')
data.columns = {'line', 'name'}

CHARACTER_NAME = 'Nessa'


contexted = []

# context window of size 7
n = 7

for i in data[data.name == CHARACTER_NAME].index:
  if i < n:
    continue
  row = []
  prev = i - 1 - n # we additionally substract 1, so row will contain current responce and 7 previous responces
  for j in range(i, prev, -1):
    row.append(data.line[j])
  contexted.append(row)

columns = ['response', 'context']
columns = columns + ['context/' + str(i) for i in range(n - 1)]

df = pd.DataFrame.from_records(contexted, columns=columns)