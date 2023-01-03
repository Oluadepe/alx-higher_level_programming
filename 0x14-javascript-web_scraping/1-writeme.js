#!/usr/bin/node
# Script that writes a string to a file

const fs = require('fs');
const args = process.argv;
fs.writeFile(args[2], args[3], (err) => {
  if (err) console.log(err);
});
