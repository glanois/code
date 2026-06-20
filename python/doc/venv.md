# Python Virtual Environment

# BASIC

This is the basic workflow for using a virtual environment:

```bash
mkdir ./venv
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
.
.
.
deactivate
```

# ADVANCED

You may find it necessary to install some Python packages at the system level.

`tkinter` is one such example.  `Pillow` is one you can install via `pip` but you'll probably want to do all these at once:

```bash
sudo apt update
sudo apt install python3-tk python3-pil python3-pil.imagetk
```

The problem is that site packages are not visible to a `venv`.  Therefore, you'll have to bring them into your `venv` when you create it via the `--system-site-packages` option.

```bash
python3 -m venv --system-site-packages venv_name
source venv_name/bin/activate
pip install -r requirements.txt   # any other deps
```

