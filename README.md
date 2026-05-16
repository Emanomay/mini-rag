#mini-rag-apply 

This is a project that implent a extranal context from other resoureses to be ubdates and to help for genrtaing quations 

## Requirments 

-python 3.8 or above 

## Install python using Miniconda 

Download Miniconda from [Here :https://anaconda.com/api/installers/Miniconda3-latest-Windows-x86_64.exe ]

2. then create a new enviroment using the following command :
```
$ conda create -n mini-rag-apply python=3.11 pip # make sure that the python version had  

```
3. activate the enviroment 
conda activete mini-rag-apply 



### Optional setup you command line for better readablity 
```bash 

export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "

``` 

### Instaltion 

### install the requierments packege 
```
pip install -r requirements.txt (which have the servers for prudcation and stream)

```
### setup the enviroment variables 
```
cp .env.example .env 

```
go to the .env after stup and put your main cridanilas and API's Key "confegiration

### how to run Fast API 

make a main.py file an take the app that we make with 

call hash ``` uvicorn main:app ```

then add http://127.0.0.1:8000/welcome 
then add docs and turn to swagger UI http://127.0.0.1:8000/docs 

you can use https://www.postman.com make a coliication and then add a request and then name it and then put what exatly after the / of the main host 
you can also recall with
### calling the fast API server 
 uvicorn main:app --reload --host 0.0.0.0 --port 5000 

 **GET {{api}}/welcome

### Json file for the coolication 
/mnt/c/Users/DELL/mini-rag-apply/assets/mini-rag-apply.postman_collection.json

### make a folder for routes to spaertae the load each srever in deff fiels to make it stucured 

1. make the __init__.py folder 
2. make the base.py folder to put the defult route 
  - call the fastapi and APIRouter
  - define the APIrouter 
  - type the defult function 
  - make the decirator with the defined varibale.get("/request")
  then go to the main and then type app.include_router(base.base_router)
  - please note that adding prefix for better acsess to spisfic people 

