import torch

from .fcos import FCOS


# build object detector
def build_model(args, 
                cfg,
                device, 
                num_classes=80, 
                trainable=False, 
                coco_pretrained=None,
                resume=None):
    print('==============================')
    print('Build {} ...'.format(args.version.upper()))

    if 'fcos' in args.version:
        model = FCOS(args=args,
                     cfg=cfg,
                     device=device, 
                     num_classes=num_classes, 
                     trainable=trainable,
                     conf_thresh=cfg['conf_thresh'],
                     nms_thresh=cfg['train_nms_thresh'] if trainable else cfg['test_nms_thresh'],
                     topk=args.topk)

    print('==============================')
    print('Model Configuration: \n', cfg)

    # Load COCO pretrained weight
    if coco_pretrained is not None:
        print('Loading COCO pretrained weight ...')
        checkpoint = torch.load(coco_pretrained, map_location='cpu')
        # checkpoint state dict
        checkpoint_state_dict = checkpoint.pop("model")
        # model state dict
        model_state_dict = model.state_dict()
        # check
        for k in list(checkpoint_state_dict.keys()):
            if k in model_state_dict:
                shape_model = tuple(model_state_dict[k].shape)
                shape_checkpoint = tuple(checkpoint_state_dict[k].shape)
                if shape_model != shape_checkpoint:
                    checkpoint_state_dict.pop(k)
            else:
                print(k)

        model.load_state_dict(checkpoint_state_dict, strict=False)

    if resume is not None:
        print('keep training: ', resume)
        checkpoint = torch.load(resume, map_location='cpu')
        # checkpoint state dict
        checkpoint_state_dict = checkpoint.pop("model")
        model.load_state_dict(checkpoint_state_dict)
                        

    return model
