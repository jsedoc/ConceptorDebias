import os
from tqdm import tqdm as tqdm
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader, ConcatDataset
from notify_run import Notify
import requests
import csv

notify = Notify()
requests.post('https://notify.run/JrovMidiez3Ehegk',data = {'message':'it works','action':None})
torch.cuda.init()
device = torch.device('cuda:1')
print(torch.cuda.get_device_name(device))

base_path = '/ssd2/chetanp'

epochs = 100
batch_size = 2 ** 15
lr = 1e-4

print('initialized')
notify.send('Initialized')

dataset = []
for i in range(4):
    path = os.path.join(base_path, 'brown_e_base' + str(i) + '.pt')
    data = torch.load(path)
    dataset.append(TensorDataset(data))
dataset = ConcatDataset(dataset)
data_loader = DataLoader(dataset, batch_size=batch_size, num_workers=16)

print('data loaded')
notify.send('data loaded')

final_loss = []

for iteration in range(7):
    class AutoEncoder(nn.Module):

        def __init__(self):
            super(AutoEncoder, self).__init__()

            # encode
            self.e1 = nn.Linear(9216, 2048)
            self.e2 = nn.Linear(2048, 2 ** (iteration+5))

            # decode
            self.d1 = nn.Linear(2 ** (iteration+5), 2048)
            self.d2 = nn.Linear(2048, 9216)

        def forward(self, x):
            encode = self.e2(F.relu(self.e1(x)))
            return self.d2(F.relu(self.d1(encode)))



    model = nn.DataParallel(AutoEncoder(),device_ids =[1,2]).to(device)

    criterion = nn.CosineSimilarity()
    loss_function = lambda x,y: (1-criterion(x,y)).mean()

    optimizer = torch.optim.Adam(
        model.parameters(), lr=lr, weight_decay=1e-5)

    notify.send('training begins {}'.format(iteration))
    notify.send('https://notify.run/JrovMidiez3Ehegk', 'https://notify.run/JrovMidiez3Ehegk')

    losses = []
    for i in range(epochs):

        running_loss = 0
        count = 0

        for data in tqdm(data_loader):
            ## Get Data
            sample = data[0].to(device)

            ## Pass forward
            output = model(sample)
            loss = loss_function(output, sample)

            ## Update Parameters
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            ## Update Running Loss
            running_loss += float(loss)
            count += 1

        #         if(i == 0): print('Enough GPU Memory Present')
        print('Epoch ' + str(i) + ' Loss: ' + str(running_loss / count))
        if i % 25 == 0:
            requests.post('https://notify.run/JrovMidiez3Ehegk',data = {'message':'Epoch ' + str(i) + ' Loss: ' + str(running_loss / count), 'action': None})
        losses.append(running_loss / count)

    final_loss.append(losses[-1])

    print('training complete')

    path = os.path.join(base_path,'brown_e_base_compressor_{}.pth'.format(iteration))
    torch.save(model.state_dict(), path)

    path = os.path.join(base_path,'optimizer_{}.pth'.format(iteration))
    torch.save(optimizer.state_dict(), path)

    path = os.path.join(base_path,'loss_{}.csv'.format(iteration))

    with open(path, 'w') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(losses)

    print('files written')

    notify.send('Training Complete {}. Outputs here:'.format(iteration), 'https://notify.run/c/cwbJ96TxHrJWdoPp')

    notify.send('Script Running Completed!')


path = os.path.join(base_path,'final_loss.csv')

with open(path, 'w') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(final_loss)

notify.send(str(final_loss))

