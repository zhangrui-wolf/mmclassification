_base_ = '../repvggB1g2_4xb64-coslr-120e_in-1k.py'

model = dict(backbone=dict(deploy=True))
