# Flask Application with Prometheus and Grafana Monitoring
![Your paragraph text](https://github.com/user-attachments/assets/f3239062-a02b-450f-bd2a-e9bd310e993a)


This project demonstrates how to integrate Prometheus and Grafana for monitoring, alerting, and dashboard creation using a simple Flask application. The Flask app exposes metrics that Prometheus scrapes, and Grafana visualizes these metrics with interactive dashboards.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Application Setup](#step-1-application-setup)
  - [Step 2: Dockerize the Flask App](#step-2-dockerize-the-flask-app)
  - [Step 3: Set Up Prometheus](#step-3-set-up-prometheus)
  - [Step 4: Set Up Grafana](#step-4-set-up-grafana)
  - [Step 5: Set Up Alerts in Grafana](#step-5-set-up-alerts-in-grafana)
- [Accessing the Services](#accessing-the-services)
- [Technologies Used](#technologies-used)
- [License](#license)

## Project Overview

This project consists of:
1. A **Flask** application that exposes metrics for Prometheus to scrape.
2. **Prometheus** is used to collect and store metrics from the Flask app.
3. **Grafana** visualizes these metrics, allowing you to create dashboards and set up alerts based on specific conditions.

The project uses Docker and Docker Compose to simplify deployment and management of these services.

## Prerequisites

To run this project, you need to have the following tools installed:
- Docker
- Docker Compose

These tools will allow you to containerize the application and set up the monitoring infrastructure with minimal configuration.

## Setup Instructions

### Step 1: Application Setup
First, set up a simple Flask application that exposes metrics for Prometheus to scrape. This application will provide a `/metrics` endpoint where Prometheus can collect data about request processing times.

### Step 2: Dockerize the Flask App
To run the application in a container, create a `Dockerfile` to package the Flask app. Docker allows you to run the app in any environment with ease.

### Step 3: Set Up Prometheus
Next, configure Prometheus to scrape metrics from the Flask application. This involves creating a Prometheus configuration file (`prometheus.yml`) that tells Prometheus where to find the Flask app’s metrics endpoint.

### Step 4: Set Up Grafana
Grafana will be used to visualize the metrics collected by Prometheus. Once Grafana is set up, you’ll add Prometheus as a data source and create dashboards to visualize the Flask application’s performance.

### Step 5: Set Up Alerts in Grafana
In Grafana, you can set up alerts based on specific metrics. For example, you can configure an alert to notify you when request processing time exceeds a certain threshold.

## Accessing the Services

Once the services are up and running using Docker Compose, you can access them through the following URLs:
- **Flask App:** [http://localhost:5000](http://localhost:5000)
- **Prometheus UI:** [http://localhost:9090](http://localhost:9090)
- **Grafana UI:** [http://localhost:3000](http://localhost:3000)

Log in to Grafana with the default credentials (username: `admin`, password: `admin`) to start setting up dashboards and alerts.

## Technologies Used

![ScreenRecording2025-01-31at12 51 30-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/c708ab50-fa60-4939-bc50-1e36862907d3)


- **Flask** - Web framework for Python used to build the application.
- **Prometheus** - Open-source monitoring and alerting toolkit used to scrape and store metrics.
- **Grafana** - Open-source platform for monitoring and observability, used to visualize the metrics from Prometheus.
- **Docker** - Used to containerize the Flask app, Prometheus, and Grafana for easy deployment.
- **Docker Compose** - A tool for defining and running multi-container Docker applications.

  <img width="498" alt="Screenshot 2025-01-30 at 21 16 05" src="https://github.com/user-attachments/assets/f0b2c2da-6601-47a3-aff2-d10b02b204bf" />


<img width="1435" alt="Screenshot 2025-01-30 at 21 19 31" src="https://github.com/user-attachments/assets/bb7c69fc-f82f-4265-a583-7b7decf47841" />
<img width="1438" alt="Screenshot 2025-01-30 at 08 48 56" src="https://github.com/user-attachments/assets/c0eeb217-92b0-4a5b-97a9-67ccda635fed" />
<img width="1432" alt="Screenshot 2025-01-30 at 08 42 35" src="https://github.com/user-attachments/assets/1a061b36-da81-472d-af20-5508482cbe8d" />
<img width="1429" alt="Screenshot 2025-01-30 at 08 41 49" src="https://github.com/user-attachments/assets/b4103081-7349-4fd7-b604-b4be4d5fe67a" />
<img width="1405" alt="Screenshot 2025-01-30 at 08 21 48" src="https://github.com/user-attachments/assets/edf9d910-81d4-44e1-b798-0b919080c222" />
<img width="1440" alt="Screenshot 2025-01-29 at 22 42 00" src="https://github.com/user-attachments/assets/352f574f-7e11-4822-881d-c9f56a9f3028" />
<img width="1112" alt="Screenshot 2025-01-30 at 20 33 44" src="https://github.com/user-attachments/assets/62d5f680-0566-4f8f-9ef3-d7c4010a00fe" />




