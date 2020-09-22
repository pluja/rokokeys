# Rokokeys
Rokokeys is a reasonably safe method of saving your wallet's mnemonic seeds. This method is much better than writing down your seed on a phone or a not-so-securelly-saved paper.

> Note that this is a **functional** beta version. Much more improvements will come with the methodology and security.

## How it works:

It's simple. Rokokeys will ask you for a **secret**. This secret is a *salt* that will be added to each of your mnemonic seed words. Each resulting word (word+salt) will be hashed using an algorithm of your choice. 

Then Rokokeys will generate a QR code with the `rokokeys recovery` along with a `backup.csv`. You can now write down the `backup.csv` anywhere you want or save and distribute your QR code. It is safe as without the **secret** no one will be able to decrypt your mnemonic seed.

## IMPORTANT: Before using

Read this **very** important points before using Rokokeys to backup your seeds:
1. Anything displayed on a digital screen might be compromised in one way or another. 
2. Any device connected to the internet might be compromised.
3. Any device that *has been* connected to the internet might be compromised.
4. Your computer might have a *keylogger* or any other kind of malware on it.

To reduce the threat you should:
1. Know your threat model.
2. Use a newly and fresh installed OS. It is highly recommended to use [**Tails**.](https://tails.boum.org/)
3. Clone the repository, copy it to a USB drive and proceed without internet connection.
4. READ THE CODE. Even if you don't know anything about Python, read it and try to find if there's anything strange. Rokokeys does NOT need internet connection and it does NOT save your raw keys anywhere on the computer.
5. Again, [**use Tails on a USB drive**.](https://tails.boum.org/)
6. Don't use a shared computer.
7. Once the backup is finished, delete all evidences.
8. You should still keep a copy of your raw mnemonic seed somewhere.
9. SAVE THIS CODE. Just in case you need to recover your keys and you can't access this repository.
10. Make a test before the definitive copy. Just to learn the flow. Use 2 or 5 words.
10. Be safe. Doubt. Read the code.

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
\path\to\env\Scripts\activate
pip install -r requirements.txt
```

Now you should be ready to run it:
#### Rokokeys generator:
`python3 generator.py`

#### Rokokeys recovery:
`python3 recovery.py`
