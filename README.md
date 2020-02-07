## Preparing the development environment

Clone a Git repository.

```
git clone https://github.com/arupratoncse/demo.git
```
and go to 
```
cd demo
```

## Creating a Python development environment

```
python3.7 -m venv venv
```

## Enable Python virtual environment

Run the script to activate the created Python virtual environment.

```
source venv/bin/activate #On Windows use `venv\Scripts\activate`
```

## Module installation in Python virtual environment

Install dependent modules. Since the Python modules that depend on requirements.txt are listed , **enable** the **Python virtual environment** and install with the pip command.。

```
pip install -r requirements.txt
```

If you get an error during installation, update the setuptools and pip versions as they may be out of date.

```
pip install -U pip setuptools
```
## Set API Key
In `demo/settings`  file set api `API_KEY='your api key'`

## Prepare database
Now go to demo directory where `manage.py` file exist and command
```
python manage.py migrate news
```
## Run Application
Start the development server:
```
python manage.py runserver
```
From a web browser , you can browse at http://127.0.0.1:8000/
