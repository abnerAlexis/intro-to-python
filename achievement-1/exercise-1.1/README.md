# Python
### Installation
Check whether you have Python installed with the following lines in your terminal.
``` 
 python --version
 python2 --version
 python3 --version
 ```
Python can be installed on a Mac via either Python’s official installer or the Homebrew package manager.  

![alt text](./images/Stp1-PythonVersionCheck.png)

### New Environment Setup
Command to setup a new environment; `pip3 install virtualenvwrapper`
![alt text](./images/Stp2-SetupNewVirtualEnv.png)

Then verify the location of virtualenvwrapper.sh
![alt text](./images/Stp3-VerifyingVirtualEnvLocation.png)

### Modify the shell startup file
For Z Shell (macOS 10.15+):
`sudo nano ~/.zshrc`
Add the following lines at the bottom of the file:
```
export VIRTUALENVWRAPPER_PYTHON=$(which python3.8)
source $(which virtualenvwrapper.sh)
```

Close the editor with `Ctrl + X`, type `Y` and press Enter, then reload your modified shell startup file.
for Z Shell, it’s `source ~/.zshrc`

![alt text](./images/Stp4-ModifyShellStartupFile.png)

### Creating a Virtual Environment
Command `mkvirtualenv cf-python-base`

![alt text](./images/Stp5-CreateNewVirtualEnv.png)

### VSCode
![alt text](./images/Stp6-VSCode.png)

### Installing IPython
Command `pip3 install ipython`
![alt text](./images/Stp7-InstallingIPython.png)

### Adding `requirements.txt`
Command `pip3 freeze` to see the requirements on terminal,  
`pip3 freeze > requirements.txt` to create a txt file in the project directory
![alt text](./images/Stp8-AddingRequirementsFile.png
)

### Creating cf-python-copy and Installing the packages from cf-python-base
![alt text](./images/Stp9-CreateaVirtualEnvCopy.png
)
![alt text](./images/Stp10-InstallingPackagesFromcf-python-base.png)
