
# Universities ETL Pipeline (Poland)

This project is a simple **ETL (Extract, Transform, Load)** pipeline built in Python that fetches a list of universities in Poland from a public API, processes the data, and stores it in a PostgreSQL database.  
It is scheduled to run automatically every minute.

## Features
- **Extract**: Retrieves university data from the [Hipolabs Universities API](http://universities.hipolabs.com/).
- **Transform**:  
  - Cleans and formats `domains` and `web_pages` columns.  
  - Classifies universities into types such as *University*, *Polytechnic*, *Academy*, etc.  
- **Load**: Saves the processed data into a PostgreSQL database table (`universities`).
- **Logging**: Stores ETL logs in `etl.log`.
- **Scheduling**: Runs every minute using the `schedule` library.

## Requirements
- Python 3.8+
- PostgreSQL installed and running
- The following Python packages:
  ```bash
  pip install requests pandas sqlalchemy psycopg2 schedule
  ```

## Configuration

Edit the PostgreSQL connection string in the `load` function if needed:

```python
engine = create_engine("postgresql://postgres:123@localhost:5432/universities_etl")
```

## Data Source

The data is fetched from the [Hipolabs Universities API](http://universities.hipolabs.com/).

## Example Table Structure

| domains    | country | web\_pages                                       | name                               | type       |
| ---------- | ------- | ------------------------------------------------ | ---------------------------------- | ---------- |
| agh.edu.pl | Poland  | [http://www.agh.edu.pl/](http://www.agh.edu.pl/) | AGH University of Science and Tech | University |
| uw\.edu.pl | Poland  | [http://www.uw.edu.pl/](http://www.uw.edu.pl/)   | University of Warsaw               | University |

---

**Author:** Karol Szeląg

```

