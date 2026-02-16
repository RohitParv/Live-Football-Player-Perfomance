# Live Football Player Performance Analyzer

A full-stack machine learning application that simulates live football matches and dynamically evaluates player performance in real time.

This project combines realistic football event simulation, performance analytics, and ML-based feature analysis within an interactive dashboard.

---

## Project Overview

The Live Football Player Performance Analyzer:

- Simulates real-time football match events
- Tracks multiple players simultaneously
- Dynamically updates player performance ratings
- Uses a trained ML model to analyze feature importance
- Allows manual event injection (goal, assist, key pass, etc.)
- Displays live score trends with visual charts

The system behaves like a live match engine combined with a performance analytics platform.

---

## Machine Learning Component

### Dataset Generation
- Custom synthetic dataset generator
- Realistic football metrics:
  - Goals
  - Assists
  - Shots on target
  - Key passes
  - Pass accuracy
  - Tackles
  - Interceptions
  - Clearances
  - Yellow cards
  - Activity rate

### Model
- RandomForestRegressor
- Feature importance extraction endpoint
- Performance score prediction (0–100 scale)
- Trend detection (UP / DOWN / STABLE)

### ML Endpoints
- `/api/v1/players/performance`
- `/api/v1/model/feature-importance`

---

## Full Stack Architecture

### Backend
- FastAPI
- Python
- Scikit-learn
- Joblib
- In-memory match simulation engine
- REST APIs

### Frontend
- React (Vite)
- Dynamic polling (20-second refresh)
- Dropdown player selector
- Manual event trigger UI
- Performance trend chart visualization

---

## Core Features

- 6-player live simulation
- Possession-based event logic
- Position-based behavior (FW, MF, DF)
- Match state persistence
- Score history tracking
- Manual event override system
- Realistic minute-by-minute progression
- Reset capability

---

## Realism Improvements

- Position-based probability engine
- Per-minute event limits
- Dynamic rating drift
- Discipline penalties:
  - Yellow card → -10%
  - Red card → -30%
- Attacking and defensive weight balancing
- Performance clamped between 0–100

## What This Project Demonstrates

End-to-end ML workflow

Synthetic dataset engineering

Model training and deployment

Real-time API integration

React state management

Backend simulation architecture

Production-style project structuring
---

## 🛠 Installation

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

### Backend runs at port http://127.0.0.1:8000
### Frontend runs at port http://localhost:5173
