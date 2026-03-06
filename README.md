# SME Sales Pipeline 🚀

This is a robust Data Pipeline designed to automate sales data processing. It is fully containerized using **Docker** and managed within a **WSL (Linux)** environment for maximum portability and reliability.

------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Containerization:** Docker
* **Environment:** WSL2 (Ubuntu)
* **Secret Management:** Python-dotenv

------------------------------------------------------------------------------------------------------------

## 📁 Project Structure
```text
├── data/               # Input: Raw CSV daily sales files
├── src/                # Core: Models, CRUD operations, and Data Extractor
├── output/             # Output: Automated Excel Analytics reports
├── outputs/            # Local host volume (Output data)   
├── main.py             # Orchestrator: The main entry point to run the pipeline
├── .gitignore          # Files excluded from GitHub
├── .dockerignore       # Files excluded from Docker Build
├── Dockerfile          # Image build instructions
├── config.py           # Configuration: Logging & Path management
├── .env.example        # Environment variables template
└── requirements.txt    # Python dependencies

------------------------------------------------------------------------------------------------------------

🚀 Getting Started
1. Prerequisites
    ● WSL2 (Ubuntu recommended)
    ● Docker Desktop (with WSL2 integration enabled)
    ● Git

2. Environment Configuration
Do not share your .env file. Instead, use the template:
    1. Create a .env file in the root directory.
    2. Add your variables:
        2.1- USER_NAME=your_name
        2.2- APP_PHASE=development

3. Building the Image
Generate the Docker image using the following command:
docker build -t sales-pipeline:1.0 .

4. Running the Pipeline
Execute the container and map the local outputs folder to receive the output:
docker run --rm --env-file .env -v $(pwd)/outputs:/app/output sales-pipeline:1.0

------------------------------------------------------------------------------------------------------------

📊 Key Features
    ● Data Isolation: Uses Docker volumes to separate code from generated data.
    ● Security: Sensitive information is managed via environment variables.
    ● Optimized Images: Built on python:3.11-slim to reduce image size and deployment time.
    ● Cross-Platform Ready: Tested on WSL2 to guarantee compatibility with Linux-based production servers.

------------------------------------------------------------------------------------------------------------

🛡️ License
Distributed under the MIT License. See LICENSE for more information.

✨ Developed by Abdulelah Ibrahim Muhmin — Data Engineering Enthusiast.