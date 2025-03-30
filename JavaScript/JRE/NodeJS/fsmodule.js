const fs = require('fs')

// fs.readFile('file.txt', 'utf-8', (err, data)=>{
//   console.log(err, data)
// })

// const a = fs.readFileSync('file.txt')
// console.log(a.toString())

// fs.writeFile('file2.txt', "This is data", () => {
//   console.log("written to the file")
// })

const b = fs.writeFileSync('file3.txt', "This is data")
console.log(b)
console.log("Finished reading file")
