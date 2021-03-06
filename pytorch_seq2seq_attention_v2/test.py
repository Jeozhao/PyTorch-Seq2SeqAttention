

128
| Epoch: 001 | Train Loss: 0.770 | Train PPL:   2.159 | Val. Loss: 0.011 | Val. PPL:   1.012 |

def train(model, epoch, criterion, optimizer, data_loader):
    model.train() 
    for batch_idx, (data, target) in enumerate(data_loader): 
        if cuda_gpu: 
            data, target = data.cuda(), 
            target.cuda() model.cuda() 
            data, target = Variable(data), Variable(target) 
            output = model(data) 
            optimizer.zero_grad() 
            loss = criterion(output, target) 
            loss.backward() optimizer.step() 
            if (batch_idx+1) % 400 == 0: 
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\\tLoss: {:.6f}'.format( epoch, (batch_idx+1) * len(data), len(data_loader.dataset), 100. * (batch_idx+1) / len(data_loader), loss.data[0])) 
                

def test(model, epoch, criterion, data_loader): 
    model.eval() 
    test_loss = 0 
    correct = 0 
    for data, target in data_loader: 
        test_loss += criterion(output, target).data[0] 
        pred = output.data.max(1)[1] # get the index of the max log-probability 
        correct += pred.eq(target.data).cpu().sum() 
        test_loss /= len(data_loader) # loss function already averages over batch size 
        acc = correct / len(data_loader.dataset)
        print('\\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\\n'.format( test_loss, correct, len(data_loader.dataset), 100. * acc)) 
        return (acc, test_loss)


       [[ 9],
        [ 5],
        [ 9],
        [ 5],
        [11],
        [ 9],
        [ 9],
        [11],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 5],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [10],
        [10],
        [ 9],
        [ 9],
        [ 4],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 8],
        [ 8],
        [ 9],
        [ 9],
        [ 4],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [11],
        [11],
        [ 9],
        [ 9],
        [ 4],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 5],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 6],
        [ 9],
        [10],
        [10],
        [ 9],
        [ 9],
        [ 4],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 8],
        [ 8],
        [ 9],
        [ 9],
        [ 4],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 5],
        [ 9],
        [11],
        [11],
        [ 9],
        [ 9],
        [ 4],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [10],
        [10],
        [ 9],
        [ 9],
        [ 4],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 7],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 8],
        [ 8],
        [ 9],
        [ 9],
        [ 4],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [11],
        [11],
        [ 9],
        [ 9],
        [ 4],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [10],
        [10],
        [ 9],
        [ 9],
        [ 4],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 8],
        [ 8],
        [ 9],
        [ 9],
        [ 4],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [11],
        [11],
        [ 9],
        [ 9],
        [ 4],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 6],
        [ 9],
        [10],
        [10],
        [ 9],
        [ 9],
        [ 4],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 8],
        [ 8],
        [ 9],
        [ 9],
        [ 4],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 5],
        [ 9],
        [11],
        [11],
        [ 9],
        [ 9],
        [ 4],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [10],
        [10],
        [ 9],
        [ 9],
        [ 4],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 8],
        [ 8],
        [ 9],
        [ 9],
        [ 4],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [11],
        [11],
        [ 9],
        [ 9],
        [ 4],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [11],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [11],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [10],
        [10],
        [ 9],
        [ 9],
        [ 4],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [10],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [10],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 8],
        [ 8],
        [ 9],
        [ 9],
        [ 4],
        [ 8],
        [ 9],
        [ 9],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 9],
        [ 8],
        [ 9],
        [ 3],
        [ 9],
        [ 9],
        [ 4],
        [ 3],
        [ 8],
        [ 9],
        [ 9],
        [ 9]]