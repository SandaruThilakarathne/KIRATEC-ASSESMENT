# KIRATEC-ASSESMENT

##### Author:
    Theekshana Sandaru Thilakarathne

## Step 0
Follow these only if you don't have python 3x, pipenv, virtualenv and virtualenvwrapper installed in your machine.
If you do, then skip to step 1
#### a) Install python 3x
    
    1) For Ubuntu / Linux OS
        1. verify using 'python --version'
        
        if python 3.x there move to the step 1
        
        2. sudo apt update
        
        3. sudo apt install software-properties-common
        
        4. sudo add-apt-repository ppa:deadsnakes/ppa
        
        5. sudo apt update
        
        6. sudo apt install python3.10
        
        7. check python version to verify the installation using 'python ––version'
    
    2) For Windows
        1. verify using 'python --version'
        
        2. downlaod the python 3.10 using below link and install: -
           https://www.python.org/downloads/
           
        3. check python version to verify the installation using 'python ––version'
 
#### b) Install pip
    
    1) For Ubuntu / Linux OS
	    1. verify using 'pip --version'
	    
	    2. sudo apt update
	    
	    3. sudo apt install python3-pip
	    
	    4. verify the pip version to confirm

    2) For Windows
        
        1. verify using 'pip --version'
        
        if not available follow the steps
        
        2. python get-pip.py


## Step 1
#### 1) Install pipenv library
      1. For Ubuntu / Linux OS
            sudo pip3 install pipenv
      
      2. For Windows OS
            pip install pipenv
            
## Step 2
#### 1) Create a virtual environment
    run below command

    - pipenv shell

    this will create the virualenv and activate the virtualenv for you

    then run

    - pipenv sync --dev

    to install the dependacies


## Step 3
#### 1) run project
    python manage.py runserver

    credentials for superuser:
        username: admininvent
        password: admin