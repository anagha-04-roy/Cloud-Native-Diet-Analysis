# Cloud-Native-Diet-Analysis

This repository contains our group project for the Cloud-Native Application Development course.

The project focuses on analyzing the **All_Diets.csv** dataset and implementing cloud-native concepts such as containerization, serverless simulation, and CI/CD automation.

## Project Tasks

### Task 1 – Dataset Analysis (Team Task)

The dataset analysis component is based on the project requirements provided in the course materials.

As a team, we downloaded the dataset, reviewed the requirements, and verified the project setup.

*(This section will be updated once the team completes the implementation and analysis.)*



### Task 2 – Dockerization (Person A)

Person A is responsible for:

* Creating the Dockerfile
* Building and testing the Docker image
* Simulating deployment using Docker
* Performing container validation and testing

*(This section will be updated when Task 2 is completed.)*



### Task 3 – Serverless Function with Azurite (Person B)

Person B is responsible for:

* Setting up Azurite for local Blob Storage simulation
* Uploading the dataset to Blob Storage
* Implementing the serverless-style processing function
* Processing nutritional data
* Saving results to simulated NoSQL storage

*(This section will be updated when Task 3 is completed.)*



### Task 4 – CI/CD Pipeline (Person C)

This section was completed by Person C and focuses on the CI/CD pipeline implementation using GitHub Actions.

Completed work:

* Created the GitHub repository
* Added the initial project structure and placeholder files
* Configured the GitHub Actions workflow in `.github/workflows/deploy.yml`
* Implemented automated workflow execution on repository updates

Current pipeline actions:

* Repository checkout
* Python environment setup
* Dependency installation
* Basic syntax validation
* Docker image build

The pipeline is configured to run automatically whenever code is pushed to the `main` branch.


## Repository Structure (Current)

```text
Cloud-Native-Diet-Analysis/
│
├── data_analysis.py
├── lambda_function.py
├── Dockerfile
├── requirements.txt
│
└── .github/
    └── workflows/
        └── deploy.yml

## Team Members

### Person A

* Task 2: Dockerization
* Task 5: Enhancement Research

### Person B

* Task 3: Serverless Function and Azurite Simulation

### Person C

* Task 4: GitHub Repository Management
* GitHub Actions CI/CD Pipeline



## Notes

This repository is actively being developed as part of the course project.

Additional code, documentation, screenshots, and configuration files will be added as team members complete their assigned tasks.

The repository serves as the central location for project collaboration, version control, and integration of all project deliverables.
