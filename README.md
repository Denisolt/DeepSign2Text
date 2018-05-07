# Classification of American Sign Language (ASL)

## Background:

The project was started as the final project for Data MInig Course. The requirements were to create 2 classification algorithms and 2 evaluation techniques. According to National Institute on Deafness and Other Communication Disorders (NIDCD),  about 2 to 3 out of every 1,000 children in the United States are born with a detectable level of hearing loss in one or both ears.[1](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing#1) and  about 28.8 million U.S. adults could benefit from using hearing aids.[2](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing#8)

## Dataset:

The dataset used in this implementation is [ASL Alphabet](https://www.kaggle.com/grassknoted/asl-alphabet) from Kaggle. 

The data set is a collection of images of alphabets from the American Sign Language, separated in 29 folders which represent the various classes. The training data set contains 87,000 images which are 200x200 pixels. There are 29 classes, of which 26 are for the letters A-Z and 3 classes for *SPACE*, *DELETE* and *NOTHING*.

Examples of the dataset (letters A to D):

<img src="https://github.com/Denisolt/DeepSign2Text/blob/master/resources/A1.jpg?raw=true" width="200">            <img src="https://github.com/Denisolt/DeepSign2Text/blob/master/resources/B1.jpg?raw=true" width="200">            <img src="https://github.com/Denisolt/DeepSign2Text/blob/master/resources/C1.jpg?raw=true" width="200">            <img src="https://github.com/Denisolt/DeepSign2Text/blob/master/resources/D1.jpg?raw=true" width="200">

## Networks:

2 types of networks were utilised:

- using Transfer Learning from Inception V3
- CNN built from scratch

### Transfer Learning:

**Transfer learning** or inductive transfer is a research problem in [machine learning](https://en.wikipedia.org/wiki/Machine_learning) that focuses on storing knowledge gained while solving one problem and applying it to a different but related problem.[[3]](https://en.wikipedia.org/wiki/Transfer_learning#cite_note-1) For example, knowledge gained while learning to recognize cars could apply when trying to recognize trucks. This area of research bears some relation to the long history of psychological literature on [transfer of learning](https://en.wikipedia.org/wiki/Transfer_of_learning), although formal ties between the two fields are limited.

The weights of **Inception V3** were utlized. 

Inception-v3 is trained for the [ImageNet](http://image-net.org/) Large Visual Recognition Challenge using the data from 2012. This is a standard task in computer vision, where models try to classify entire images into [1000 classes](http://image-net.org/challenges/LSVRC/2014/browse-synsets), like "Zebra", "Dalmatian", and "Dishwasher".

Inception is well suited for this task due to the fact that it works with images, therefore the features that all images have in common are already extracted.

### Convolutionl Neural Net:

In this implementation a regular **CNN** was created in **Keras** using a network similar to **VGG 16**.

Data was preprocessed with some data augmentation from Keras and fed into the network. 

<img src="https://raw.githubusercontent.com/Denisolt/DeepSign2Text/master/resources/cnn.png?token=AQYtUT7FCn67aoY0C4H22tV3Yi3FgQPwks5a-PUzwA%3D%3D">


## Results:

The network have shown high performance results.

| Implementation                         | training loss | training accuracy | validation loss | validation accuracy |
| -------------------------------------- | ------------- | ----------------- | --------------- | ------------------- |
| Convolutional Neural Network (scratch) | 0.0584        | 0.9851            | 0.3794          | 0.9225              |
| Transfer Learning                      |               |                   |                 |                     |

# Insert a graph here

## Deployment:

Dependencies used are located in a req.txt file

```bash
git clone https://github.com/Denisolt/DeepSign2Text.git
cd DeepSign2Text
virtualenv -p python3 venv
source venv/bin/activate
pip install -r req.txt
jupyter notebook
```

Now either open the **ScratchCNN** notebook or **TransferLearning** notebook. 

Run the notebook. 

## Additional Resources:
All additional resources including other datasets and published papers are located in the folder [resources](https://github.com/Denisolt/DeepSign2Text/tree/master/resources)
