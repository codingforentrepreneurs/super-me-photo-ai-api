# SuperMe - Generative Photo AI
[![Star this repo](https://img.shields.io/github/stars/codingforentrepreneurs/super-me-photo-ai-api?style=social)](https://github.com/codingforentrepreneurs/super-me-photo-ai-api)

Learn how to build an API that trains and generate photos featuring... you! Using FastAPI, Upstash, Replicate, Jupyter, and more

__Tech Stack__
- [Python 3.13](https://github.com/python)
- [Django](https://github.com/django/django) (`pip install "Django>=5.1,<5.2"`)
- [Upstash](https://upstash.com) - serverless redis, qstash for async endpoint scheduling, rate limiting, caching, and more.
- [Replicate](https://replicate) - train and run generative ai model featuring your face
- [Python requests](https://github.com/psf/requests) (`pip install requests`)
- [Jupyter](https://jupyter.org/) (`pip install jupyter`)
- [Python Decouple](https://github.com/HBNetwork/python-decouple) to load environment variables (e.g. `.env`) with type casting and default values.
- [ostris/flux-dev-lora-trainer](https://replicate.com/ostris/flux-dev-lora-trainer). Model made to allow you to fine-tune FLUX with your own images (pre-trained model designed for your training)

## Tutorial
- [Let's build a AI Photo Generator with Python and FastAPI](https://www.youtube.com/watch?v=lV82LDKT16A)

## Getting Started

Download the following:
- [git](https://git-scm.com/)
- [VSCode](https://code.visualstudio.com/) (or [Cursor](https://cursor.com/))
- [Python](https://www.python.org/downloads/)

Open a command line (Terminal, VSCode Terminal, Cursor Terminal, Powershell, etc)

Clone this Repo
```bash
mkdir -p ~/dev/superme-api
cd ~/dev/superme-api
git clone https://github.com/codingforentrepreneurs/super-me-photo-ai-api .
```

Checkout the start branch
```bash
git checkout start
```

Make the code yours
```
rm -rf .git
git init
git add --all
git commit -m "I am the capitan now"
```

Create a Python vitual environment
_macOS/Linux/WSL_
```bash
python3.12 -m venv venv
source venv/bin/activate
```

_windows powershell_
```powershell
c:\Path\To\Python312\python.exe -m venv venv
.\venv\Scripts\activate
```

Install requirements
```bash
(venv) python -m pip install pip --upgrade
(venv) python -m pip install -r requirements.txt
```

To add support for `.heic` images (e.g. iPhone images) install `libheif` via [homebrew](https://brew.sh):
```bash
brew install libheif
(venv) python -m pip install pillow-heif
```
If on _linux_ or _Docker_, you can use `sudo apt-get install libheif-dev`
