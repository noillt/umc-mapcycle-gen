# umc-mapcycle-gen
Generates umc_mapcycle.txt with mapnames and their surf tiers with only those maps that have been zoned in influx timer

### Requirements:
- MySQL Database
- [noillt/maptier](https://github.com/noillt/maptier) database of maps
- influx timer database being in MySQL
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

### Example
```sh
python3 umc_mapcycle.py
```
Output:
```
umc_mapcycle
{
    "Tier 1"
    {
        "surf_year3000" { display "surf_year3000 - Tier 1" }
        "surf_zoomathon" { display "surf_zoomathon - Tier 1" }
        "surf_zor" { display "surf_zor - Tier 1" }
    }
    "Tier 2"
    {
        "surf_squirrelsonvacation" { display "surf_squirrelsonvacation - Tier 2" }
        "surf_stonks" { display "surf_stonks - Tier 2" }
        "surf_the_gloaming" { display "surf_the_gloaming - Tier 2" }
    }
    "Tier 3"
    {
        "surf_kitsune2" { display "surf_kitsune2 - Tier 3" }
        "surf_slob2_fix" { display "surf_slob2_fix - Tier 3" }
    }
}
```

### Automating
Create a `cron`:
```cron
0 0 * * * /path/to/umc_mapcycle.py > /path/to/cstrike/umc_mapcycle.txt
```
