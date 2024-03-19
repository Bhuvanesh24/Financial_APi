# Financial_API
This Django project provides an API for accessing stock data from a MySQL database hosted in XAMPP.

## Description

This project is aimed at building an API using the Django framework to facilitate the retrieval of stock data from a MySQL database. The API endpoints allow users to query stock data for specific tickers, filter by columns, and specify time periods.

## Installation

1. **Clone the Repository:**

2. **Install Dependencies:**
  - cd api
  -  pip install -r requirements.txt

3. **Populate MySQL Database:**
- Start XAMPP and ensure that the MySQL server is running.
- Create a new database and table in MySQL.
- Import the provided CSV file into the database table.
- or use run.py file which is given to populate the database

4. **Run the Application:**
5. ## Usage

Once the application is running, you can access the API endpoints using a web browser or API testing tool like Postman.

## API Endpoints

- `/api/ticker=AAPL`: Returns all data for the AAPL ticker.
- `/api/ticker=AAPL&column=revenue,gp`: Returns AAPL's data with revenue and gp columns only.
- `/api/ticker=AAPL&column=revenue,gp&period=5y`: Returns 5 years' worth of data for Apple, with only its revenue and gp columns.

## Performance Optimization

- Ensure that MySQL database tables are properly indexed for efficient querying.
- Implement caching mechanisms to reduce database load and response times.
- Use efficient database queries to fetch only the required data.
- Profile the code and optimize any bottlenecks for faster execution.
## Compression

Enable Gzip compression in Django project settings to reduce response size and improve performance.

## Testing

- Test the API endpoints with different parameters and ticker symbols (e.g., AAPL, ZNGA, YELP).
- Measure the response times to ensure they meet the specified requirement of responding in less than 100ms.
- Use Postman or curl to test the api endpoints and runtime
