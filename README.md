\# University Student CRUD API



A simple Student CRUD REST API built using FastAPI and Python.



\## Project Description



This project provides APIs to create, read, update, and delete university student records.



Student data is stored using in-memory storage.



\## Technologies Used



\* Python

\* FastAPI

\* Pydantic

\* Uvicorn



\## Project Structure



```text

stu\_crud\_devopsAssign-1/

│

├── main.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── models/

│   └── student\_model.py

│

├── routes/

│   └── student\_route.py

│

└── controllers/

```



\## Installation



Install the required dependencies:



```bash

pip install -r requirements.txt

```



\## Run the Application



Start the FastAPI server using:



```bash

python -m uvicorn main:app --reload

```



The application will run at:



```text

http://127.0.0.1:8000

```



\## API Documentation



FastAPI provides interactive Swagger documentation at:



```text

http://127.0.0.1:8000/docs

```



\## Available API Endpoints



| Method | Endpoint                 | Description      |

| ------ | ------------------------ | ---------------- |

| POST   | `/students`              | Create a student |

| GET    | `/students/{student\_id}` | Get a student    |

| PUT    | `/students/{student\_id}` | Update a student |

| DELETE | `/students/{student\_id}` | Delete a student |

| GET    | `/`                      | Check API status |



\## Student Fields



\* `id`

\* `name`

\* `email`

\* `course`

\* `semester`



\## Author



Arya Rajput



