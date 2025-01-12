# Doctool


## Description
Doctools is a web application built with React and Express.js that allows users to perform various document and image manipulation tasks. The primary features include :
- Background Removal: Remove backgrounds from images.
- Background Change: Add or change the background of images.
- Document to PDF Conversion: Convert text or documents to PDF format.
- PDF to Document Conversion: Extract text from PDFs and save it as a text document.
- Image Compression: Compress image sizes while maintaining quality.

## Features
- Remove Background: Upload an image, and Doctools will automatically remove the background.
- Add/Change Background: Upload a background image and overlay it on top of the original image.
- Convert to PDF: Convert text or documents into a PDF file format.
- Convert PDF to Text: Extract text from a PDF and save it in a .txt format.
- Compress Images: Compress images to reduce file sizes without losing significant quality.

# Technologies Used
## Frontend:

- React.js
- React Hooks
- Axios (for making API requests)
- HTML/CSS
- Canvas API (for image manipulation)
- File Upload Handling with react-dropzone

## Backend:

- Express.js
- Multer (for file upload handling)
- OpenCV.js (for background removal and image manipulation)
- PDF.js (for PDF to text extraction)
- JS PDF (for converting text to PDF)

## Insrallation
# Prerequisites
Before running the project, you need to have the following installed:

- [Node.js](https://nodejs.org)
- [npm](https://npmjs.com)
- [React](https://reactjs.org)
# Front end setup

# Clone the repository:

`git clone https://github.com/yourusername/doctools.git`
`cd doctools`
Navigate to the frontend folder:

`cd frontend`
`npm install`
 Run the React development server:
 
`npm start`
The frontend should now be available at http://localhost:3000.

# Backend Setup
Navigate to the backend folder:


`cd backend`
Install the necessary dependencies:

`npm install`

Run the Express server:

`node server.js`


The backend server will be running at http://localhost:5000.

## File Uploads
The server uses Multer to handle file uploads. Ensure that the uploads directory exists on your backend folder, or it will be created automatically when a file is uploaded.
API Endpoints
1. POST /remove-bg
- Description: Removes the background from an uploaded image.
- Request: Form-data with key image containing the image file.
- Response: A processed image with the background removed.
2. POST /add-background
- Description: Changes or adds a background to the uploaded image.
- Request: Form-data with key image containing the original image file. Form-data with key background containing the background image file.
- Response: A new image with the added background.
3. POST /convert-to-pdf
- Description: Converts text or a document to a PDF file.
- Request: JSON body containing a text field with the content to be  converted to PDF.
- Response: The generated PDF file.
4. POST /convert-pdf-to-text
- Description: Extracts text from a PDF and returns it as a .txt document.
- Request: Form-data with key pdf containing the PDF file.
- Response: A .txt file containing the extracted text.
5. POST /compress-image
- Description: Compresses an image to reduce its size.
- Request: Form-data with key image containing the image file.
- Response: A compressed image.
## Usage
# Frontend
- The frontend is built with React and allows users to interact with the various tools.
- Users can upload images and documents, trigger the corresponding transformations (like background removal, compression, etc.), and download the resulting files.
# Backend
- The backend handles the API endpoints for image processing, PDF conversion, and file handling.
- The backend uses OpenCV.js and Canvas for image manipulation tasks, along with Multer for file handling.

# Example Usage
- Remove Background:

- Go to the Remove Background tab in the app.
- Upload an image and click Remove Background.
- Download the processed image.
#  Add Background: 
- Go to the Add Background tab.
- Upload both an image and a new background, then click Add Background.
- Download the new image with the changed background.

# Convert to PDF:

- Go to the Convert to PDF tab.
- Paste your text or upload a document.
- Click Convert to PDF and download the PDF file.

# Convert PDF to Text:

- Go to the Convert PDF to Text tab.
- Upload your PDF and click Convert.
- Download the extracted text in .txt format.

# Compress Image:

- Go to the Compress Image tab.
- Upload an image and click Compress.
- Download the compressed image.
## Contributing
- Fork the repository.
- Create a new branch for your feature (git checkout -b feature-name).
- Make your changes and commit (git commit -am 'Add feature').
- Push to the branch (git push origin feature-name).
- Create a new Pull Request.


