import torch
import torch.nn as nn

def double_conv(inc,outc,inter_c,kernel_size,act):
	'''
	returns a double Conv, uses a PRELU activation
	'''
	layers = [nn.Conv2d(inc,inter_c,kernel_size),
			  nn.PReLU(),
			  nn.Conv2d(inter_c,outc,kernel_size),
			  nn.PRELU()]
	return nn.Sequential(*layers) 

def pad_same(inp1,inp2):

	'''
	returns padding value needed for getting functionality same as TF's SAME padding method
	'''

	h,w = inp1.shape
	h1,w1 = inp2.shape
	pad_tuple = (torch.abs(w1-w),0,torch.abs(h-h1),0)
	return pad_tuple


def affine_warp(I,flow):
    '''
    I: Image
    flow: optical flow
    '''

    B,C,H,W = I.shape

    xx = torch.arange(0,W).view(1,-1).repeat(H,1)
    yy = torch.arange(0,H).view(-1,1).repeat(1,W)

    xx = xx.view(1,1,H,W).repeat(B,1,1,1)
    yy = yy.view(1,1,H,W).repeat(B,1,1,1)

    grid = torch.cat((xx,yy),1).float()

    vgrid = torch.zeros(grid.shape)
    vgrid[:,0,:,:] = grid[:,0,:,:] + flow[:,0,:,:]
    vgrid[:,1,:,:] = grid[:,1,:,:] + flow[:,1,:,:] #omit this addition for 1-D warping (stereo for example)
    
    vgrid[:,1,:,:] = 2.0*vgrid[:,1,:,:].clone()/max(H-1,1)-1.0
    vgrid[:,0,:,:] = 2.0*vgrid[:,0,:,:].clone()/max(W-1,1)-1.0

    vgrid = vgrid.permute(0,2,3,1)
     

    #change align corners as per need.
    output = nn.functional.grid_sample(I,vgrid,align_corners=True)

    return output


