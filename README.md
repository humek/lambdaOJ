# Online Judge Web Project

LambdaOJ



## Requirements

Basic Requirements:

* python
* python-pip
* python-virtualenv

To start from uWSGI, you need to have it installed:

```
sudo pip install uwsgi
```



## Installation

First, `cd` into the `lambdaOJ` directory,
create and activate virtual environment:

```
virtualenv --no-site-packages venv
source venv/bin/activate
```

Then, install requirements:

```
pip install -r requirements.txt
```

Create local database
```
./db_create.py  
./db_migrate.py
```



## Testing

Make sure you have activated the virtual environment:

```
source venv/bin/activate
```

Run it (without a web server):

```
./lambdaoj.py
```

It will listen on `127.0.0.1:5000` by default.
	


## uWSGI

Initialization:

```
./init-uwsgi.sh
```

It will prompt for `user`, `group`, `port` for lambdaOJ Web Process,
and generate `lambdaoj.ini` and `run.sh`.

After that, you can execute `run.sh` to run from uWSGI each time.

Of course, for actual use,
you also need to configure your web server.
