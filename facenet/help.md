Virtula Env
----------------
window: https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/

1. lign_dataset using mtcnn
 >> python  align_dataset_mtcnn.py ./images ./cropped
2. Trained the model using above cropped dataset
 >> train_triplet.py




PACKAGES INSTALLED
------------------
pip install pandas
pip install matplotlib
pip install scipy
pip install tensorflow
pip install sklearn
pip install pip install opencv-python
pip install opencv-python
pip install numpy==1.16.2
pip install Pillow
pip install scipy==1.1.0
pip install keras
pip install imutils
history |grep pip

Tensor flow installation error
-----------------------------------
Error: 
ERROR: Could not find a version that satisfies the requirement tensorflow (fr
versions: none)
ROR: No matching distribution found for tensorflow

Solution:
pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl
