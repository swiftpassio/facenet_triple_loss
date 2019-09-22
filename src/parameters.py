import os

if os.path.exists("./cropped1")==False:
    os.makedirs("./cropped1")

ALPHA = 0.5
THRESHOLD = 0.5
IMAGE_SIZE=96 
LAYERS_TO_FREEZE= 60
NUM_EPOCHS= 1
STEPS_PER_EPOCH= 1
BATCH_SIZE= 64
