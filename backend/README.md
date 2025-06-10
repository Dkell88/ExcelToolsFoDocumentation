# Backend

This directory contains the Python backend for processing Excel files.

## Command Line Usage

You can still run `ExtractIOandCovert.py` directly for interactive command line processing.

## REST API

A small Flask API is provided in `api.py` so the React frontend can trigger the
existing functions.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the API server:
   ```bash
   python api.py
   ```
   The server listens on port 5000 by default.

Endpoints:
- `POST /extract` – JSON body `{ "file_path": "/path/to/file.xlsx" }`
- `POST /convert` – JSON body `{ "file_path": "/path/to/file.xlsx", "output_dir": "optional" }`

Each endpoint returns JSON indicating success and the output location.
