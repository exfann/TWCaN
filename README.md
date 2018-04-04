# TWCaN

TWCaN (Twitter Website Checker and Notice) is a Twitter bot that is designed to extract URLs from Twitter posts
and run ReDeCheck on those URLs. It then prioritizes the results based on the y-coordinated and returned those
results to Twitter.

## Download and Installation

TWCaN is programmed in Python 3. In order to download the tool, simply type the followin gin the terminal:

`git clone git@github.com:exfann/TWCaN.git`

#### Depenencies

A version of ReDeCheck that has been modified to update the `getOutputFilePath` function as detailed in the paper is
necessary in order for TWCaN to be able to prioritize the results. The ReDeCheck directory must be on the same level as
the directory for TWCaN.

In addition, one must obtain a consumer key, consumer secret key, access token, and access secret token from Twitter
in order to access the API.

#### Installing Python

If Python or Python3 is not installed, one can install them using the following commands in the terminal:

`sudo apt-get install python`

`sudo apt-get install python3`

#### Installing Tweepy

Tweepy is also necessary for TWCaN to run. To install Tweepy, simply type the following command into the terminal:

`pip install tweepy`

#### Installing Pillow

Pillow is necessary for TWCaN to crop images. To install, simply type the following command into the terminal:

`pip3 install Pillow`
