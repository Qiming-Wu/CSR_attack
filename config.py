import torch
import os
from tensorboardX import SummaryWriter


class Config():
    '''
    Config class
    '''
    def __init__(self):
        self.dataset_root = './data'
        self.device       = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.lr           = 1e-5                # learning rate
        self.batch_size   = 1                   # batch size
        self.epochs       = 2                   # epochs
        self.checkpoints  = './checkpoints'     # checkpoints dir
        self.writer       = SummaryWriter()     # tensorboard writer

        self.__mkdir(self.checkpoints)

    def __mkdir(self, path):
        '''
        create directory while not exist
        '''
        if not os.path.exists(path):
            os.makedirs(path)
            print('create dir: ',path)