# Web Crawler Dev Projects



## 📣 What is conda?


**Conda is an open source package management system and environment management system that can run on operating systems such as Windows, MacOS, and Linux. Conda can quickly install, execute and update packages.**

**Using conda time, you can create, list, remove and update environments in different Python versions and packages.**



➤  **資料來源：** [**建立 Python 虛擬環境**](https://simplelearn.tw/python-conda-virtual-environment/)   


&nbsp; <img src="./Images/Steps to create a virtual environment.png" alt="Step"/>





### 🎓 Step 1. Install and update `conda`

**First, search for Anaconda Prompt on the Windows start page.**


&nbsp; <img src="./Images/Anaconda Prompt.png" alt="Anaconda Prompt"/>




**At this point you can enter the following command to check the current version.**

&nbsp; <img src="./Images/Check Current Version.png" alt="Check Current Version"/>


```

conda –V

```





**If you want to update, you can enter the following command**


&nbsp; <img src="./Images/Update conda.png" alt="Update conda"/>


```

conda update conda

```





### 🎓 Step 2. Create a virtual environment

**You can enter the following command to see how many virtual environments are currently installed on the system.**


```

conda env list

```


&nbsp; <img src="./Images/env list.png" alt="env list"/>







**Suppose we want to create a virtual environment called `Web-Clawer` and install `python 3.8` version, then we can type the following command.**


```

conda create --name Web-Clawer python=3.8

```


&nbsp; <img src="./Images/Create a virtual environment.png" alt="Create a virtual environment"/>









### 🎓 Step 3. Start the virtual environment


**To start a new virtual environment you can use the following command.**


```

conda activate Web-Clawer

```


&nbsp; <img src="./Images/Start virtual environment.png" alt="Start virtual environment"/>









### 🎓 Step 4. Leave the virtual environment


**To shut down the virtual environment, use the following command in Windows**


```

conda deactivate

```






### 🎓 Step 5. Delete the package


**If you want to delete a package in the virtual environment (such as numpy in the newly created virtual environment Web-Clawer), you can enter the following command.**



```

conda remove --name Web-Clawer numpy

```






### 🎓 Step 6. Delete virtual ring


**If you want to delete the entire virtual environment, you can enter the following command to complete the deletion.**



```

conda env remove --name Web-Clawer

```




