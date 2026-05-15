#mini-rag-apply 

This is a project that implent a extranal context from other resoureses to be ubdates and to help for genrtaing quations 

## Requirments 

-python 3.8 or above 

## Install python using Miniconda 

Download Miniconda from [Here :https://anaconda.com/api/installers/Miniconda3-latest-Windows-x86_64.exe ]

2. then create a new enviroment using the following command :
```
$ conda create -n mini-rag-apply python=3.8 

```
3. activate the enviroment 
conda activete mini-rag-apply (project_name)



### Optional setup you command line for better readablity 
```bash 

export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "

``` 

### Instaltion 

### install the requierments packege 
```
pip install -r requirements.txt

```
### setup the enviroment variables 
```
cp .env.example .env 

```
go to the .env after stup and put your main cridanilas and API's Key "confegiration