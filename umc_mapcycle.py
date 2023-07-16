import pymysql.cursors, configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('mysql-config.ini')

# Get MySQL credentials from the configuration file
mysql_host = config.get('mysql', 'host')
mysql_user = config.get('mysql', 'user')
mysql_password = config.get('mysql', 'password')
mysql_database = config.get('mysql', 'database')

# Connect to the database
influx_conn = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_password, db=mysql_database)

try:
    # Execute the SQL query
    mapcycle_query = "SELECT DISTINCT inf_maps.mapname, maps.tier " \
                     "FROM inf_maps " \
                     "INNER JOIN inf_zones ON inf_maps.mapid = inf_zones.mapid " \
                     "INNER JOIN maps ON inf_maps.mapname = maps.mapname " \
                     "ORDER BY inf_maps.mapname ASC"
    with influx_conn.cursor() as cursor:
        cursor.execute(mapcycle_query)
        mapcycle_result = cursor.fetchall()

    maplist = []
    for row in mapcycle_result:
        maplist.append({'mapname': row[0], 'tier': row[1]})

    output = {}

    for row in maplist:
        mapname = row['mapname']
        tier = row['tier']

        if 'maps' not in output:
            output['maps'] = {}

        if tier not in output['maps']:
            output['maps'][tier] = {}

        output['maps'][tier][mapname] = tier

    sorted_output = {'maps': dict(sorted(output['maps'].items()))}

    print("umc_mapcycle")
    print("{")
    for map_tier in sorted_output['maps']:
        print("    \"Tier "+str(map_tier)+"\"")
        print("    {")
        for map_name in sorted_output['maps'][map_tier]:
            print("        \""+map_name+"\" { display \""+map_name+" - Tier " + str(map_tier)+"\" }")
        print("    }")
    print("}")
finally:
    # Close the database connection
    influx_conn.close()
