# README.md
# Legal Research Assistant

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set up the database:
    ```bash
    python database/populate_db.py
    ```

3. Run the scraper to populate the database with legal data:
    ```bash
    python scraper/scraper.py
    ```

4. Start the Flask API:
    ```bash
    python api/app.py
    ```

## Usage

- Access the list of cases:
    ```bash
    curl http://127.0.0.1:5000/cases
    ```

- Populate a HotDocs template:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"CaseName": "Example Case", "Court": "Supreme Court", "DecisionDate": "2022-01-01", "Summary": "Summary of the case."}' http://127.0.0.1:5000/populate
    ```
