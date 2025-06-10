# Excel Tools Project

This repository separates the Python backend from the React frontend.

```
backend/   # Python scripts and dependencies
frontend/  # React application
```

A simple Flask API (`backend/api.py`) exposes the Excel processing functions so
Electron/React can call them.

To run the API:
```bash
cd backend
pip install -r requirements.txt
python api.py
```

Start the development environment:
```bash
npm run dev
```
