const http = require('http');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    console.log(req)

    res.status = 200;
    res.setHeader('Content-Type', 'text/html')
    res.end('<h1> This is Node Practice </h1> <p> This is some paragraph </p>')
})

server.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});