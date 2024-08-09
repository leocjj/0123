
# Basic setup instructions


### Install Python using miniconda

    https://docs.anaconda.com/free/miniconda/index.html
    or
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh


### Open “Anaconda Powershell Prompt” application

```shell
    # Create a new environment
    conda create -n multitasking python=3.12
    # Check the list of environments
    conda env list
    # Activate the environment
    conda activate multitasking

    # Clone the repository
    git clone https://github.com/leocjj/0123.git
    cd .\0123\Python\concurrent_and_parallel\
    
    # Execute the scripts
    python 01_Intensive_CPU.py
    python 01_Intensive_IO.py
