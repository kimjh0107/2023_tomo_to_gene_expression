from pathlib import Path

# Hyperparameter 
LEARNING_RATE = 0.001
WEIGHT_DECAY =  0.1
ADAM_EPSILON = 1e-6
NUM_EPOCH = 1000

BATCH_SIZE = 8
DROPOUT = 0.5


# EarlyStopping
EARLYSTOPPING_METRIC = 'val_loss'
EARLYSTOPPING_MODE = 'min'
PATIENCE = 10
MODEL_PATH = 'model/'