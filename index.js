const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json());

app.post('/run', (req, res) => {
  const { code, input } = req.body;
  fs.writeFileSync('main.py', code);
  fs.writeFileSync('input.txt', input);
  exec('python3 main.py < input.txt', (err, stdout, stderr) => {
    if (err) return res.json({ output: stderr });
    res.json({ output: stdout });
  });
});

app.listen(3001, () => console.log('Backend running on port 3001'));