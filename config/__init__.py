from .fcos_config import fcos_config


def build_config(args):
    print('==============================')
    print('Build {} ...'.format(args.version.upper()))

    cfg = fcos_config[args.version]

    return cfg
