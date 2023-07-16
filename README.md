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
        "surf_ace" { display "surf_ace - Tier 1" }
        "surf_andromeda" { display "surf_andromeda - Tier 1" }
        "surf_aser" { display "surf_aser - Tier 1" }
        "surf_beginner" { display "surf_beginner - Tier 1" }
        "surf_boreas" { display "surf_boreas - Tier 1" }
        "surf_calzone" { display "surf_calzone - Tier 1" }
        "surf_fornax" { display "surf_fornax - Tier 1" }
        "surf_garden" { display "surf_garden - Tier 1" }
        "surf_kitsune" { display "surf_kitsune - Tier 1" }
        "surf_legends" { display "surf_legends - Tier 1" }
        "surf_lovetunnel" { display "surf_lovetunnel - Tier 1" }
        "surf_me" { display "surf_me - Tier 1" }
        "surf_mesa_fixed" { display "surf_mesa_fixed - Tier 1" }
        "surf_pantheon" { display "surf_pantheon - Tier 1" }
        "surf_satellite_fix" { display "surf_satellite_fix - Tier 1" }
        "surf_school_fix" { display "surf_school_fix - Tier 1" }
        "surf_summit" { display "surf_summit - Tier 1" }
        "surf_sundown" { display "surf_sundown - Tier 1" }
        "surf_tendies" { display "surf_tendies - Tier 1" }
        "surf_trance" { display "surf_trance - Tier 1" }
        "surf_utopia_njv" { display "surf_utopia_njv - Tier 1" }
        "surf_void" { display "surf_void - Tier 1" }
        "surf_water_run_ksf" { display "surf_water_run_ksf - Tier 1" }
        "surf_whiteout" { display "surf_whiteout - Tier 1" }
        "surf_year3000" { display "surf_year3000 - Tier 1" }
        "surf_zoomathon" { display "surf_zoomathon - Tier 1" }
        "surf_zor" { display "surf_zor - Tier 1" }
    }
    "Tier 2"
    {
        "surf_8bit" { display "surf_8bit - Tier 2" }
        "surf_amplitude_light" { display "surf_amplitude_light - Tier 2" }
        "surf_anzchamps" { display "surf_anzchamps - Tier 2" }
        "surf_aqua_fix" { display "surf_aqua_fix - Tier 2" }
        "surf_beginner2" { display "surf_beginner2 - Tier 2" }
        "surf_cyberwave" { display "surf_cyberwave - Tier 2" }
        "surf_delight" { display "surf_delight - Tier 2" }
        "surf_doodles_njv" { display "surf_doodles_njv - Tier 2" }
        "surf_fortum_fix" { display "surf_fortum_fix - Tier 2" }
        "surf_holiday" { display "surf_holiday - Tier 2" }
        "surf_kloakk" { display "surf_kloakk - Tier 2" }
        "surf_lockdown" { display "surf_lockdown - Tier 2" }
        "surf_mesa_mine" { display "surf_mesa_mine - Tier 2" }
        "surf_orthodox" { display "surf_orthodox - Tier 2" }
        "surf_skipalot" { display "surf_skipalot - Tier 2" }
        "surf_spacejam" { display "surf_spacejam - Tier 2" }
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
