const express = require('express');
const app = express();
const port = 8080;

const data = {
  message: true
}

app.get('/', (req, res) => {
  res.json(data);
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
