# 🚗 Real-Time Vehicle Telemetry Data Pipeline on AWS

## 📌 Project Overview

This project demonstrates an end-to-end real-time vehicle telemetry data pipeline built using AWS cloud services.

The pipeline simulates live connected vehicle telemetry data and processes streaming events in real time using AWS Kinesis, Lambda, S3, Athena, DynamoDB, and QuickSight.

This project represents a real-world automotive telemetry analytics architecture similar to connected vehicle platforms used in modern automotive companies.

---

# 🚀 Architecture

## End-to-End Pipeline Flow

Vehicle Simulator → Amazon Kinesis → AWS Lambda → Amazon S3 → Athena → QuickSight Dashboard

---

# 🏗️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon Kinesis | Real-time data streaming |
| AWS Lambda | Serverless data processing |
| Amazon S3 | Historical telemetry storage |
| Amazon DynamoDB | Latest vehicle state storage |
| Amazon Athena | Query historical telemetry data |
| Amazon QuickSight | Dashboard & visualization |
| CloudWatch | Monitoring & logs |

---

# 📊 Features

- Real-time vehicle telemetry streaming
- Serverless event-driven architecture
- Historical telemetry storage
- Live telemetry state management
- SQL analytics using Athena
- Interactive QuickSight dashboards
- Scalable cloud-native pipeline

---

# 📂 Project Structure

```bash
real-time-vehicle-telemetry-data-pipeline/
│
├── Architecture/
│   ├── architecture.png
│   └── data_model.png
│
├── Simulator/
│   └── simulator.py
│
├── Lambda/
│   └── lambda_function.py
│
├── Athena/
│   └── athena.sql
│
├── Dashboard/
│   └── dashboard.png
│
├── README.md
│
└── requirements.txt
```

---

# ⚙️ Data Model

The telemetry schema includes:

- vehicle_id
- speed
- engine_temp
- fuel_level
- latitude
- longitude
- timestamp

---

# 🔄 Pipeline Workflow

## Step 1 — Vehicle Simulator

Python script generates fake telemetry data every second.

Example:

```json
{
  "vehicle_id": "V12",
  "speed": 82,
  "engine_temp": 101,
  "fuel_level": 64,
  "latitude": 12.9716,
  "longitude": 77.5946,
  "timestamp": "2026-05-09T10:20:30"
}
```

---

## Step 2 — Real-Time Streaming

Telemetry events are pushed into Amazon Kinesis Data Streams.

---

## Step 3 — Lambda Processing

AWS Lambda consumes records from Kinesis and:

- Stores historical data into S3
- Updates latest vehicle state into DynamoDB

---

## Step 4 — Historical Analytics

Athena queries telemetry JSON files directly from S3.

Example Query:

```sql
SELECT * 
FROM vehicle_data
LIMIT 10;
```

---

## Step 5 — Dashboard Visualization

Amazon QuickSight visualizes:

- Vehicle speed trends
- Fuel level monitoring
- Engine temperature alerts
- Real-time telemetry insights

---

# 📈 Dashboard Preview

## Vehicle Telemetry Dashboard

- Average Vehicle Speed
- Fuel Consumption Trends
- Engine Temperature Alerts

---

# 🧠 Key Learnings

- Real-time event streaming
- Serverless data engineering
- Cloud-native architecture
- AWS analytics ecosystem
- Data lake concepts
- End-to-end ETL pipeline design

---

# 🚀 Future Improvements

- Kafka integration
- Spark streaming analytics
- Real-time alert notifications
- Predictive maintenance ML models
- CI/CD deployment pipeline
- Infrastructure as Code using Terraform

---

# 👨‍💻 Author

Rohit  
Aspiring AWS Data Engineer

---