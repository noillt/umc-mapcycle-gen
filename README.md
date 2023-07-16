# umc-mapcycle-gen
Generates umc_mapcycle.txt with mapnames and their surf tiers with only those maps that have been zoned in influx timer

### Requirements:
- [noillt/maptier](https://github.com/noillt/maptier) database of maps
- influx timer database layout
- `python3 -m pip install PyMySQL`

### Configuration:
```sh
touch mysql-config.ini & chmod 0600 mysql-config.ini
vim mysql-config.ini
```
`mysql-config.ini`
```
[mysql]
host = 127.0.0.1
user = user
password = pass
database = db
```
