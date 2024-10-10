import torch.nn as nn
import torch
import torch.nn.functional as F



class MCF(nn.Module):
    def __init__(self, in_in, in_out, in_kn) -> None:
        super().__init__()

        self.cnn_layer=nn.Sequential(
            nn.Conv2d(in_channels=in_in, out_channels=in_out,
                      kernel_size=in_kn)

        )