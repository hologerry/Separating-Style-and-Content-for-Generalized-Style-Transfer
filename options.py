import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", type=str, default='dataset/seperating_trainset/',
                    help="path to folder containing images")
parser.add_argument("--mode", type=str, default='train', choices=["train", "test", "export"])
parser.add_argument("--output_dir", type=str, default='train_output', help="where to put output files")
parser.add_argument("--seed", type=int)
parser.add_argument(
    "--checkpoint",
    default=None,
    help="directory with checkpoint to resume training from or use for testing",
)
parser.add_argument(
    "--max_steps", type=int, help="number of training steps (0 to disable)"
)
parser.add_argument(
    "--max_epochs", type=int, default=200, help="number of training epochs"
)
parser.add_argument(
    "--summary_freq",
    type=int,
    default=100,
    help="update summaries every summary_freq steps",
)
parser.add_argument(
    "--progress_freq",
    type=int,
    default=50,
    help="display progress every progress_freq steps",
)
parser.add_argument(
    "--trace_freq", type=int, default=0, help="trace execution every trace_freq steps"
)
parser.add_argument(
    "--display_freq",
    type=int,
    default=500,
    help="write current training images every display_freq steps",
)
parser.add_argument(
    "--save_freq",
    type=int,
    default=500,
    help="save model every save_freq steps, 0 to disable",
)
parser.add_argument(
    "--aspect_ratio",
    type=float,
    default=1.0,
    help="aspect ratio of output images (width/height)",
)
parser.add_argument(
    "--ngf",
    type=int,
    default=64,
    help="number of generator filters in first conv layer",
)
parser.add_argument(
    "--ndf",
    type=int,
    default=64,
    help="number of discriminator filters in first conv layer",
)
parser.add_argument(
    "--dim", type=float, default=100, help="the dimension of the difference encode"
)
parser.add_argument(
    "--num_parallel_prefetch", type=int, default=2, help="the number of prefetch"
)
parser.add_argument(
    "--adam_lr", type=float, default=0.0002, help="initial learning rate for adam"
)
# parser.add_argument("--decay_rate", type=float, default=0.8, help="decay for learning rate")
# parser.add_argument("--decay_steps", type=float, default=12000, help="decay frequency for learning rate")

parser.add_argument(
    "--style_num", type=float, default=52, help="the number of styles in each batch"
)
parser.add_argument(
    "--content_num",
    type=float,
    default=52,
    help="the number of characters in each batch",
)
parser.add_argument(
    "--style_sample_n",
    type=float,
    default=7,
    help="the number of samples for each style",
)
parser.add_argument(
    "--content_sample_n",
    type=float,
    default=7,
    help="the number of samples for each content",
)
parser.add_argument(
    "--target_batch_size", type=int, default=52, help="number of target images in batch"
)

parser.add_argument("--image_channel", type=int, default=1, help="channel of images")
parser.add_argument(
    "--loss_func", type=str, default="l1_loss", help="loss function used"
)

# export options
parser.add_argument("--output_filetype", default="png", choices=["png", "jpg"])

a = parser.parse_args()
