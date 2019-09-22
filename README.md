# facenet_triple_loss
HOW TO RUN
--------------------------------------------------
0. change the direcotry to Samir and run below command

     cd /home/Samir/Samir
    
     source myenv/bin/activat

1. lign_dataset using mtcnn
 >> align_dataset_mtcnn.py ./images ./cropped



### Usage
1. Create a dataset of faces for each person and arrange them in below order.
```
root folder 
│
└───Person 1
│   │───IMG1
│   │───IMG2
│   │   ....
└───Person 2
|   │───IMG1
|   │───IMG2
|   |   ....
```


2. Use `align_dataset_mtcnn.py` to prepare our dataset for training. Run the following command:

python align_dataset_mtcnn.py ./images ./output_cropped
