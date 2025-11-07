# Titanic-ML-App
![logo](images/titanic.png)

This project uses the titanic machine learning from disaster data sets on *kaggle*.

# Problem statement
You are a data scientist that has been able to time travel back in time to the early 20th century. Using the survival data from the titanic disaster you are to construct a Machine learning model in order to predict who would or would not survive. Create a streamlit app to deploy your ML model to make it accessible to all potential passengers in an effort to save their lives. 

## Environment setup

First install `uv` using:
```bash
pip3 install uv 
```

Next create a virtual environment using:
```shell 
uv venv .venv --python 3.11
```

Activate the virtual environment.

For mac:
```shell
source .venv/bin/activate
```
For windows:
```shell
.venv\Scripts\activate
```

Install packages and dependencies using:
```shell
uv sync
```

## Running the application
Bash and powershell scripts have been created to allow for easy execution of the app (backend + frontend).

For mac/linux users:

```shell
bash run_app.sh
```

For windows users, run the following:
```shell
.\run_app.psl
```

If the above scripts don't work, we can manually start the backend with:
```shell
cd src/backend
uvicorn api:app --reload
```

The frontend can be started with:
```shell
cd src/frontend
streamlit run app.py
```

In case of windows powershell usage replace the above forward slashes with back slashes.


## App preview
Once the app is launched, the following should be visible
![logo](images/App_image.png)
