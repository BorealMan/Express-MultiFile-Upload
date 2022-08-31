const express = require("express");
const cors = require("cors")
let formidable = require('express-formidable');
let path = require('path');

let app = express();

app.use(cors());

app.get('/', (req, res) => {
    res.send(`<html>
    <head>
        <title>Upload Imgs App</title>
        <style>
            h1 {
                font-size:2.5rem;
                font-family: "Arial";
                text-align:center;
            }
            #Image_Form {
                display:flex;
                flex-direction:column;
                gap:1rem;
                font-size:1.25rem;
                padding: .5rem;
                width:fit-content;
                margin-left:auto;
                margin-right:auto;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the test site!</h1>

        <form id="Image_Form" method='POST' name="Image_Form" action="/submit" enctype="multipart/form-data">
            <label>Please Upload Your Images:</label>
            <input name="images" type="file" webkitdirectory directory multiple></input>
            <input type="submit"></input>
        </form>
    </body>
</html>`).status(200);
})

app.post('/submit', formidable({
    encoding: 'utf-8',
    uploadDir: path.join(__dirname, 'uploads'),
    multiples: true,
    keepExtensions: true // req.files to be arrays of files
  }), 
  (req, res) => {
    console.log('Files '+JSON.stringify(req.files));// contains data about file fields

    res.send(`<html>
    <head>
        <title>Upload Imgs App</title>
    </head>
    <body>
        <h2>Request Recieved.</h2>     
    </body>
</html>`).status(201);
})

const PORT = 8888
app.listen(PORT, () => {
    console.log(`Listening at http://localhost:${PORT}`)
})