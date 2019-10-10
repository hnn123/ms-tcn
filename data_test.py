import numpy as np

features_path = '/home/hcn/project/ms-tcn/data/50salads/features/rgb-01-1.npy'
features = np.load(features_path)
print(np.shape(features))