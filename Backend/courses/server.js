'use strict';

const express = require('express');
const app = express();
const jwt = require('express=jwt');
const cors = require('cors');
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());


app.get('/Backend/courses', (req, res) => {
  let courseData = [
  {
    id: 99991,
    course: 'CS348'
  },
  {
    id: 99992,
    course: 'EAPS375'
  },
  {
    id: 99993,
    course: 'PHIL210'
  },
  {
    id: 99994,
    course: 'SOC100'
  },
  {
    id: 99995,
    course: 'CS381'
  },
  {
    id: 99996,
    course: 'PHYS221'
  }
  ];
  res.json(foodJokes);
})

app.listen(3000);

console.log('Listening to localhost:3000');
