# Application Tracker System

This repository contains the source code for an Application Tracker System (ATS) that helps in analyzing resumes and job descriptions. The system uses natural language processing techniques to calculate the similarity between the resume and job description, allowing for efficient application screening.

## Features

- Upload and process resumes and job descriptions.
- Calculate the similarity score between the uploaded files using cosine similarity.
- Determine the selection status based on the similarity score threshold.
- Web interface to access and interact with the ATS.

## Technologies Used

- Python: Used for the backend logic, file processing, and machine learning tasks.
- Flask: Backend web framework for serving the application.
- Streamlit: Frontend web framework for the interactive web interface.
- scikit-learn: Machine learning library for cosine similarity calculation.
- docx2txt: Library for extracting text from Word documents.

## Setup and Usage

1. Clone the repository:


2. Install the required dependencies:


3. Run the Flask application:


4. Access the application by navigating to `http://localhost:5000/` in your web browser.

5. Upload resumes and job descriptions using the provided interface and view the similarity score and selection status.

## Folder Structure

- `app.py`: Backend Flask application file.
- `streamlit_app.py`: Streamlit frontend application file.
- `templates/index.html`: HTML template for the web interface.
  
## Contribution

Contributions to the Application Tracker System project are welcome. If you find any bugs, have suggestions for improvements, or want to add new features, please submit an issue or create a pull request.

## License

This project is licensed under the [MIT License].

