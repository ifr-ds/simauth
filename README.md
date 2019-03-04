# Simauth

Minimalistic auth microservice

## Development instructions

Create Python [virtual
environment](https://docs.python.org/3/tutorial/venv.html) with:

```
$ python3 -m venv <your-venv-name>
```

This will create the `<your-venv-name>` directory. If this command fail, you
likely lack some python packages. On ubuntu/debian:

```
$ sudo apt-get install python3 python3-dev python3-venv python3-pip
```

should solve the problem.

Virtual environment provides isolated development environment. It is important
not only to have, more or less, uniform development environment across many
computers or to avoid dependencies version conflicts between developed packages,
but also to avoid interference with OS. On linux, many system tools use python!
So **never, ever** install any python package as a root!

Virtual env need to be activated:

```
$ source <path-to-your-venv>/bin/activate
```

If succeeded, it change to prompt adding the name of venv to the prompt. Now
any python command will run in the venv.

Now, install package in development mode:

```
$ pip install -U -e .
```

`pip` is a python package manager. The `-U` options tells to upgrade package if
is already installed. Not needed for first installation, but it's good to remember
to add it. Otherwise, one can spend hours on debugging... 

The `-e` option installs package in *development* mode. Technically, instead of
copying package into python library path, it puts there a symlink to package source
directory. In that way, any changes to source code will be reflected immediately.

The `.` tells that current working directory is a package source.


### Running in development mode

API will be developed using [falcon](https://falcon.readthedocs.io/en/stable/)
microframework. To run it, just type:

```
$ gunicorn --reload simauth.api:app
```

The `simauth.api` is python module to load, `app` is an identifier from that module
that defines a WSGI object to be served by gunicorn. Thanks to `--reload`, any
change to source code will result in worker reload.

Use e.g. `curl` to interact with api:

```
$ curl localhost:8000/hello/world
{"status": "ok", "msg": "Hello world!"}%
```
