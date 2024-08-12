# summory-project

pre installed libraries for backend application :-
  -> pip3 install flask
  -> pip3 install transformers
  -> pip3 install flask_cors
  -> pip3 install docx
  -> pip3 install PyPDF2
for frontend install :- 
  -> npm 
  -> nodejs
  -> react

How To Run :-
 - First need to run backend application
    command - python3 app.py
 - Second run front end application
    command - npm start

The application is built with a Flask backend and a React frontend. The backend uses the transformers library for text summarization, leveraging pre-trained models.

Backend (Flask)
- For PDF files, the PyPDF2 library is used to read and extract text from each page.
- For DOCX files, the python-docx library is used to parse the document and extract text from paragraphs.
- The extracted text is passed through a pre-trained summarization pipeline using the transformers library.
- The pipeline("summarisation") function is used to generate a concise summary of the document.


Frontend (React)  - The frontend allows users to upload a document and receive the summarized content in a user-friendly interface.

Challenges Faced

  ===> CORS Issues
* Challenge: Initially, the frontend could not communicate with the backend due to CORS (Cross-Origin Resource Sharing) restrictions.
* Solution: The flask-cors library was integrated into the Flask backend to handle CORS, allowing the frontend and backend to interact seamlessly.
* 
 ===> Compatibility with Different Document Formats
* Challenge: Ensuring the backend could handle different file formats (PDF, DOCX, TXT) required careful consideration of text extraction methods.
* Solution: Separate functions were implemented for extracting text from PDFs and DOCX files, using PyPDF2 and python-docx, respectively. TXT files were handled by directly reading the content.
