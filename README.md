# CounterMaker
Counter Maker Bot, Some options:

  - Adding counter to all sort file
  - Adding users to database
  - Showing users count
  - Anti - Spam

## Information

> It's based on telebot

> It uses Redis as database

> It's a clone for [@mkcounterbot](http://telegram.me/mkcounterbot)


### Installation

First we Clone the source code and go to that directory

```sh
$ git clone https://github.com/iTeam-co/Counter-Maker
$ cd Counter-Maker
```
Then open *bot.py* using

```sh
$ nano bot.py
```

Ater that:
Add your token to line 4
Make a public channel and put the channel username in line 5
Write your telegram ID in line 6
Save file and exit using `ctrl + c ; y ; enter`

Then we install the dependencies

```sh
$ apt-get update
$ apt-get install redis-server
$ pip install pyTelegramBotApi
$ pip install redis
```
Now we run the bot

```sh
$ python bot.py
```

### Developer

Email: Prsahrn@gmail.com

Telegram: [Parsa](http://telegram.me/prsahrn)

Powered By iTeam

[Persian Channel](https://telegram.me/iTeam_ir) ; [English Channel](https://telegram.me/iTeam_en)
