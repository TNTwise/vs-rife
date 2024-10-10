import torch
import torch.nn.functional as F

def grid_proc(tenFlow, tenFlow_div, backwarp_tenGrid):
        tenFlow = torch.cat([tenFlow[:, 0:1] / tenFlow_div[0], tenFlow[:, 1:2] / tenFlow_div[1]], 1)
        g = (backwarp_tenGrid + tenFlow).permute(0, 2, 3, 1)
        return g

def warp(tenInput, g):
    
    return torch.nn.functional.grid_sample(
        input=tenInput,
        grid=g,
        mode="bilinear",
        padding_mode="border",
        align_corners=True,
    )
