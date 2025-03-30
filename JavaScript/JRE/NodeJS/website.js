const http = require('http');
const fs = require('fs')
const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    console.log(req.url)

    res.setHeader('Content-Type', 'text/html')

    if (req.url == '/') {
        res.status = 200;
        res.end('<h1> This is Node Practice </h1> <p> This is some paragraph </p>')
    }
    else if (req.url == '/about') {
        res.status = 200;
        res.end('<h1> This is about code practice</h1> <p>This is some about code</p>')
    }
    else if (req.url == '/hello') {
        res.status = 200;
        const data = fs.readFileSync('index.html');
        res.end(data.toString());
    }
    else {
        res.status = 404;
        res.end('<h1>Not Found</h1>')
    }

})

server.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});