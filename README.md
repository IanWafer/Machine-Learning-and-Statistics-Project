# Machine Learning and Statistics Project

Student: Ian Wafer
Student no.: G00376322
Email: g00376322@gmit

Lecturer: Ian McLoughlin
Due date: 08/01/21

Below are the instructions we have been issued to complete for the machine learning and statistics end of term project-
![Instructions](/images/instructions.png 'Instructions')

This repository contains my project submission on power prediction based on wind speed - [link](https://github.com/IanWafer/Machine-Learning-and-Statistics-Project)

### Contents of submission
- powerproduction.txt: original  dataset received.  
- requirements.txt: the pacage requirements to run the application.  
- Machine Learning & Statistics Project.ipynb: Description of methods used and model trained.  
- model.json: output of serialized model to JSON.  
- model.h5: output of serialized weights.  
- wind_predict_server.py: server for web interface.  
- Dockerfile: to place application in container if required.  
- .dockerignore: create quicker container image if any future changes are made.  
- .gitignore: files to  ignorer on git upload.  
- README.md: Standard description of the application and how to run it.  
- static/index.html: web application  host location.  
- Licence: standard licence.  

### Packages Used
* pandas
* numpy
* seaborn
* matplotlib.pyplot
* pylab
* sklearn  
* sklearn.linear_model
* sklearn.preprocessing
* tensorflow.keras
* collections
* sklearn.pipeline


### How to download this repository
Go to Github profile located here- [link](https://github.com/IanWafer)  
Click repository labeled IanWafer/Machine-Learning-and-Statistics-Project.  
Click the download button or clone the repository to your own Github account.  

### How to run the code within the Jupyter Notebook
Install a python code client (Anaconda recommended. See here for installer- [link](https://www.anaconda.com/products/individual))  
Run a command line client (cmder recommended. See here for installer- [link](https://cmder.net/))  
Ensure you are in the correct directory where .ipynb is located using the cd command to navigate.  
To open the descriptions and code type Jupyter Notebook in the command window.  
Your default browser window should be open now in the Jupyter interface. Select Machine Learning & Statistics Project.ipynb to open the file.  
To run all of the code click the cell button from the menu at the top of the browser window and select Run All.  
To test any of the scripts within the notebook double click the cell to enter the edit mode and press shift + enter to run the code.  


### Setting up the virtual environment
To open a virtual environment to run only the required packages and versions required run the following commands
~~~ 
python -m venv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt 
~~~

### Launch the web application
To run the server navigate to the location using the cd command and type in the below to run the server
~~~
python wind-server-predict.py
~~~

This should result in the following in the command line interface-
![Server Running](/images/server_running.png 'Server running')

When the server is up and running use the browser to navigate to 127.0.0.1:5000/ to bring you to the web interface. From here a wind speed between 0 and 25 can be entered. Note any value below 0.325 and above 24.499  will result in a score of 0 as this is the start up speed required for power generation on the low end and the system cut off on the high end.
