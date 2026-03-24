# coding=utf-8
"""Training and evaluation"""
import os
import multiprocessing as mp

# 1. 缓解显存碎片化
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'

# 2. 彻底封杀 TensorFlow（保留咱们成功的这一步）
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
_ = tf.config.list_logical_devices()

# 3. 显卡主权移交 PyTorch
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import torch
_ = torch.cuda.device_count()

# ================= 终极防御机制 =================
# 4. 封杀 CuDNN 的隐形显存黑洞（极其关键，专治大尺寸图像！）
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True

# 5. 封杀 DataLoader 子进程的显存窃取
try:
    mp.set_start_method('spawn', force=True)
except RuntimeError:
    pass
# ================================================

import run_lib
from absl import app
from absl import flags
from ml_collections.config_flags import config_flags
import logging

FLAGS = flags.FLAGS

config_flags.DEFINE_config_file(
  "config", None, "Training configuration.", lock_config=True)
flags.DEFINE_string("workdir", None, "Work directory.")
flags.DEFINE_enum("mode", None, ["train", "eval"], "Running mode: train or eval")
flags.DEFINE_string("eval_folder", "eval",
                    "The folder name for storing evaluation results")
flags.mark_flags_as_required(["workdir", "config", "mode"])


def main(argv):

  if FLAGS.mode == "train":
    tf.io.gfile.makedirs(FLAGS.workdir)
    gfile_stream = open(os.path.join(FLAGS.workdir, 'stdout.txt'), 'w')
    handler = logging.StreamHandler(gfile_stream)
    formatter = logging.Formatter('%(levelname)s - %(filename)s - %(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel('INFO')
    
    print(FLAGS.config)
    run_lib.train(FLAGS.config, FLAGS.workdir)

  elif FLAGS.mode == "eval":
    run_lib.evaluate(FLAGS.config, FLAGS.workdir, FLAGS.eval_folder)
  else:
    raise ValueError(f"Mode {FLAGS.mode} not recognized.")

if __name__ == "__main__":
  app.run(main)