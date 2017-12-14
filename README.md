# ijcnlp17_sk
Code to replicate experiments in the IJCNLP 2017 paper "Learning kernels over strings using Gaussian Processes"

# Dependencies

1) Install tensorflow

2) Install GPy

3) Install flakes

## For the synthetic data experiments

4) Download GloVe embeddings

5) Install NLTK

6) Download PTB sample from NLTK

## For the Emotion Analysis experiments:

7) Download GloVe embeddings (if not done yet)

8) Download emotion dataset


# Performance experiments

For these you do not need GloVe or PTB. Just run performance/run.sh. It will store results in a folder. Then run plot.sh to plot.


# Synthetic data

Assuming you put the embeddings in the required place, the script run.sh is enough to replicate the experiments. Or if you have a GPU you can use run_gpu.sh. More fine-grained options are available in run.py.

The scripts will generate the data and perform the synthetic experiments, storing data in the 'results' folder. The script plot.sh will plot the results using bar plots, as in the paper.


# Emotion Analysis experiments

(coming soon)
