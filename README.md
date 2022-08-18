
# makeclean.py

A clean-up utility in python that removes files and folders. It is meant as a portable replacement for `rm -r` in `clean:` targets of makefiles, but
can be used for other similar situations.

It accepts an arbitrary number of path-objects and removes them if they exist, while ignoring non-existent ones.


## Install

Currently, the package is not release, so you have to install it from the repo.

Install via pip:

```bash
pip install git+https://github.com/Cube707/python-makeclean
```


## Usage

You can use it directly from the terminal:

```bash
makeclean foo.txt bar/
```

But it gets really helpful if you use it as the `clean:` target of a makefile, making it fully portable:

```makefile
TRASH = foo.txt bar/

clean:
    makeclean $(TRASH)
```

Use `makeclean --help` for more details.

---

*Copyright 2022 Jan Wille*
