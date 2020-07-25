# docker-python-pip-practice

# Requirements

- docker
- docker-compose

# Usage

## Setup

```
docker-compose run app pip install -r requirements.txt -t /pip-lib
```

## Run

```
docker-compose run app python main.py hello
```

# License

MIT

# References

- [pip install](https://pip.pypa.io/en/stable/reference/pip_install/)
- [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
