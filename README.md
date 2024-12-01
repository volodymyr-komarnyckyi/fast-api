# CVE API Service

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Endpoints](#endpoints)
- [Presentation](#presentation)

## Introduction

Teams API Service is designed to streamline the management of teams-related data.


## Installation

1. Clone the repository:

   ```
   git clone https://github.com/volodymyr-komarnyckyi/fast-api
   ```

2. Run command:
   ```
   uvicorn app.main:app --reload --port 8001
   ```
3. App will be available at: ```127.0.0.1:8001```

## Endpoints
   ```
   "info" : 
                   "http://127.0.0.1:8001/info/"
   "CVEs" : 
                   "http://127.0.0.1:8001/get/all/"
                   "http://127.0.0.1:8001/get/known/"
                   "http://127.0.0.1:8001/get?query="
   ```
