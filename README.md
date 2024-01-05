<h1>Project 3</h1>

<h3>Project Overview & Purpose</h3>

The affects of socioeconomic and climate change indicators on GDP per Capita

<h3>Project Instructions</h3>

- You can use this database to analyze if socioeconomic and climate change indicators have an effect on GDP per Capita.​

- We used PETL python library to import the csv file and clean the data​

- From the cleaned data, Pandas DataFrame that was created, can be used to draw analysis and/or create data visualizations

- Also FLASK API can be used to view the dataset and draw analysis as well

<h3>API Routes</h3>
/api/v1.0/countries - returns a list of all countries in the dataset<br>
/api/v1.0/regions - returns a list of all unique regions in the dataset<br>
/api/v1.0/all - returns all useful data for each country<br>
/api/v1.0/country/country_name - returns all data for the specified country (country_name). If a country is not found, an error will occur.<br>
/api/v1.0/gdp - returns each country with their GDP Per Capita<br>
/api/v1.0/area - returns each country with their GDP Per Capita and area in sq. mi.<br>
/api/v1.0/birthrate - returns each country with their GDP Per Capita and birthrate<br>
/api/v1.0/coastline - returns each country with their GDP Per Capita and coastline (coast/area ratio)<br>
/api/v1.0/infant_mortality - returns each country with their GDP Per Capita and infant mortality (per 1000 births)<br>
/api/v1.0/literacy - returns each country with their GDP Per Capita and literacy %<br>
/api/v1.0/net_migration - returns each country with their GDP Per Capita and net migration<br>
/api/v1.0/phones - returns each country with their GDP Per Capita and phones (per 1000)<br>
/api/v1.0/pop_density - returns each country with their GDP Per Capita and population density (per sq. mi.)<br>
/api/v1.0/population - returns each country with their GDP Per Capita and population<br>

<h3>Databases Used and Why</h3>

- We used postgres to create our databases
  
-Since our data wasn't complex, we decided to use postgres over mongoDB and SQLite

<h3>ETL Workflow with Diagram</h3>

![GDP](https://github.com/matvio16/project-3/assets/15304495/e78077b1-9840-4a24-b205-bc24fe390410)


<h3>Ethical Considerations</h3>

1. Data Security and Privacy: Ensuring that individuals' data is secure from unauthorized access by using encryption and access controls. Also, privacy regulations should be considered like HIPPA, GLBA, GDPR and etc.
2. Fairness and Bias: Regularly testing algorithms and models to identify any bias in results that unfairly disadvantage certain groups.
3. Transparency and Accountability: Making sure the data science process and decision-making transparent and understandly.
4. Informed Consent: Does the end-user understand what type of data is being collected and how it will be used?
5. Data Accuracy: Ensuring that the data is accurate, that the cleaning process did not accidentally introduce bias. 


<h3>References</h3>
https://www.kaggle.com/datasets/fernandol/countries-of-the-world <br>
https://www.psycopg.org/psycopg3/docs/ <br>
https://petl.readthedocs.io/en/stable/#
