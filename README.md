# facenet_triple_loss

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

python align_dataset_mtcnn.py ./YOUR_DIRECTIORY_CONTAINING_DATA ./output_cropped
