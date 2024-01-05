import psycopg2 as psy
from flask import Flask, jsonify
from psycopg2.extras import RealDictCursor

conn = psy.connect("dbname=countrygdp user=postgres password = 'postgres'")
cur = conn.cursor(cursor_factory=RealDictCursor)



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/countries<br/>"
        f"/api/v1.0/regions<br/>"
        f"/api/v1.0/all<br/>"
        f"/api/v1.0/country/country_name<br/>"
        f"/api/v1.0/gdp<br/>"
        f"/api/v1.0/area<br/>"
        f"/api/v1.0/birthrate<br/>"
        f"/api/v1.0/coastline<br/>"
        f"/api/v1.0/infant_mortality<br/>"
        f"/api/v1.0/literacy<br/>"
        f"/api/v1.0/net_migration<br/>"
        f"/api/v1.0/phones<br/>"
        f"/api/v1.0/pop_density<br/>"
        f"/api/v1.0/population<br/>"
    )


# Return the JSON representation of the countries
@app.route("/api/v1.0/countries")
def countries():

    sql = "select country from countries"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries
@app.route("/api/v1.0/regions")
def regions():

    sql = "select region from regions"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries
@app.route("/api/v1.0/all")
def all():

    sql = "select country, region, population, area_sq_mile, pop_density, coastline_ratio, net_migration, infant_mortality_per_1000, gdp_per_capita, \
        literacy_pct, phones_per_1000, birthrate, deathrate \
        from gdp g \
        join countries c on g.country_id = c.country_id \
        join regions  r on g.region_id = r.region_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation a specific country
@app.route("/api/v1.0/country/<country_name>")
def country(country_name):

    sql = "select country, region, population, area_sq_mile, pop_density, coastline_ratio, net_migration, infant_mortality_per_1000, gdp_per_capita, \
        literacy_pct, phones_per_1000, birthrate, deathrate \
        from gdp g \
        join countries c on g.country_id = c.country_id \
        join regions  r on g.region_id = r.region_id \
        where c.country = '" + country_name + "'"
    cur.execute(sql)
    results = cur.fetchall()
    if results == []:
        return jsonify({"Error": f"Country {country_name} not found."}), 404
    else:
        return jsonify(results)

# Return the JSON representation of the countries with GDP per capita
@app.route("/api/v1.0/gdp")
def gdp():

    sql = "select country, gdp_per_capita \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and area
@app.route("/api/v1.0/area")
def area():

    sql = "select country, gdp_per_capita, area_sq_mile \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and birthrate
@app.route("/api/v1.0/birthrate")
def birthrate():

    sql = "select country, gdp_per_capita, birthrate \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and coastline
@app.route("/api/v1.0/coastline")
def coastline():

    sql = "select country, gdp_per_capita, coastline_ratio \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and infant mortality
@app.route("/api/v1.0/infant_mortality")
def infant_mortality():

    sql = "select country, gdp_per_capita, infant_mortality_per_1000 \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and literacy
@app.route("/api/v1.0/literacy")
def literacy():

    sql = "select country, gdp_per_capita, literacy_pct \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and net migration
@app.route("/api/v1.0/net_migration")
def net_migration():

    sql = "select country, gdp_per_capita, net_migration \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and phones per 1000
@app.route("/api/v1.0/phones")
def phones():

    sql = "select country, gdp_per_capita, phones_per_1000 \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and population density
@app.route("/api/v1.0/pop_density")
def pop_density():

    sql = "select country, gdp_per_capita, pop_density \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))

# Return the JSON representation of the countries with GDP per capita and population
@app.route("/api/v1.0/population")
def population():

    sql = "select country, gdp_per_capita, population \
        from gdp g \
        join countries c on g.country_id = c.country_id"
    cur.execute(sql)
    results = cur.fetchall()

    return (jsonify(results))


if __name__ == '__main__':
    app.run(debug=True)