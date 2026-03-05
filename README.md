# 🚀 SME Sales Data Pipeline (ETL & Analytics)

An end-to-end Data Engineering pipeline designed for Small and Medium Enterprises (SMEs). This system automates daily sales data extraction, performs data cleaning/validation using Pandas, stores records in a relational SQL database, and generates business intelligence reports in Excel format.

------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **ORM:** SQLAlchemy 2.0 (Modern Mapped Styles)
* **Data Processing:** Pandas
* **Environment Management:** Python-Dotenv
* **Reporting:** Openpyxl (Excel Engine)
* **Logging:** Centralized Python Logging Module

------------------------------------------------------------------------------------------------------------

## 📁 Project Structure
```text
├── data/               # Input: Raw CSV daily sales files
├── src/                # Core: Models, CRUD operations, and Data Extractor
├── output/             # Output: Automated Excel Analytics reports
├── main.py             # Orchestrator: The main entry point to run the pipeline
├── config.py           # Configuration: Logging & Path management
└── .env.example        # Environment variables template

------------------------------------------------------------------------------------------------------------

🌟 Key Features
    ● Automated ETL: Seamlessly Extracts, Transforms, and Loads data from CSV to SQL.

    ● Inventory Sync: Automatically updates product stock levels upon every sale record.

    ● Modern SQL Logic: Leverages SQLAlchemy 2.0 features for high performance and type safety.

    ● Business Insights: Generates professional Excel reports ranked by revenue and volume.

    ● Robust Logging: Full traceability of every pipeline step via app.log.

------------------------------------------------------------------------------------------------------------

⚙️ Installation & Usage
    1- Clone the repository:
        git clone [https://github.com/your-username/sme-sales-pipeline.git](https://github.com/your-username/sme-sales-pipeline.git)

    2- Install dependencies:
        pip install -r requirements.txt

    3- Setup Environment:
        Create a .env file in the root directory based on .env.example:
        DATABASE_URL=sqlite:///./sme_sales.db

    4- Run the Pipeline:
        python main.py

------------------------------------------------------------------------------------------------------------

📈 Roadmap
    ● [ ] Dockerization: Containerize the application using Docker for easy deployment.

    ● [ ] Data Validation: Implement strict schema validation using Pydantic.

    ● [ ] Orchestration: Schedule and monitor daily runs using Apache Airflow.

✨ Developed by Abdulelah Ibrahim Muhmin — Data Engineering Enthusiast.