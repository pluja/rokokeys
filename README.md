# Rokokeys
Rokokeys is a reasonably safe method of saving your wallet's mnemonic seeds. This method is much better than writing down your seed on a phone or a not-so-securelly-saved paper.

> Note that this is a **functional** beta version. Much more improvements will come with the methodology and security.

## How it works:

It's simple. Rokokeys will ask you for a **secret**. This secret is a *salt* that will be added to each of your mnemonic seed words. Each resulting word (word+salt) will be hashed using an algorithm of your choice. 

Then Rokokeys will generate a QR code with the `rokokeys recovery` along with a `backup.csv`. You can now write down the `backup.csv` anywhere you want or save and distribute your QR code. It is safe as without the **secret** no one will be able to decrypt your mnemonic seed.

## Install and use

Getting Rokokeys to work is very easy. First, you will need to clone this repository with:

`git clone https://github.com/pluja/rokokeys/`

Once you cloned the repo, you should navigate into the newly created directory containing all the files. Use `cd rokokeys`.

Now you will need to have `python3` and `python3-venv` installed on your computer. To do so:

#### On Linux:
`sudo apt install python3 python3-pip python3-venv`

#### On Windows
1. Download the latest Python3 version from [here](https://www.python.org/downloads/windows/)
2. Install it.
3. Now from your command prompt: `pip install virtualenv`

Finally run the following commands:
##### Linux:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##### Windows:
```
virtualenv venv
/path/to/env/Scripts/activate
pip install -r requirements.txt
```

Now you should be ready to run it:
#### Rokokeys generator:
`python3 generator.py`

#### Rokokeys recovery:
`python3 recovery.py`
