import glob
import os
import operator
import tqdm
datadir = '../../data/breakfast/groundTruth'
savedir = '../../data/breakfast/label'

txtfiles = glob.glob(os.path.join(datadir, '*.txt'))

for txtfile in tqdm.tqdm(txtfiles):
    lines = open(txtfile, 'r').read().strip('\n').split('\n')
    label_dict = {}
    label_num = 0
    for line in lines:
        if line not in label_dict:
            label_num += 1
            label_dict[line] = label_num
    label_dict = sorted(label_dict.items(), key=operator.itemgetter(1), reverse=False)
    labelfile = open(os.path.join(savedir, os.path.basename(txtfile)), 'w')
    for item in label_dict:
        labelfile.write(item[0] + '\n')
    labelfile.close()