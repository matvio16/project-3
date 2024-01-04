-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/TAYCla
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "COUNTRIES" (
    "country_id" PRIMARY   NOT NULL,
    "country" varchar   NOT NULL
);

CREATE TABLE "REGIONS" (
    "region_id" PRIMARY   NOT NULL,
    "region" varchar   NOT NULL
);

CREATE TABLE "GDP" (
    "country_id" FOREIGN   NOT NULL,
    "region_id" FOREIGN   NOT NULL,
    "population" INT64   NOT NULL,
    "area_sq_mile" INT64   NOT NULL,
    "pop_density" float   NOT NULL,
    "coastlne_ratio" float   NOT NULL,
    "net_migration" float   NOT NULL,
    "infant_mortality_per_1000" float   NOT NULL,
    "GDP_per_capita" float   NOT NULL,
    "literacy_pct" float   NOT NULL,
    "phones_per_1000" float   NOT NULL,
    "birthrate" float   NOT NULL,
    "deathrate" float   NOT NULL
);

ALTER TABLE "COUNTRIES" ADD CONSTRAINT "fk_COUNTRIES_country_id" FOREIGN KEY("country_id")
REFERENCES "GDP" ("country_id");

ALTER TABLE "REGIONS" ADD CONSTRAINT "fk_REGIONS_region_id" FOREIGN KEY("region_id")
REFERENCES "GDP" ("region_id");

