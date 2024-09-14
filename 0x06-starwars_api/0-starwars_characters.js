#!/usr/bin/node

// Import the request module.
const request = require('request');

// Import Movie ID number when passed from CLI.
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please, input a Movie ID.');
  process.exit(1);
}

// Build API url.
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie character data from the API.
request(apiUrl, (err, resp, body) => {
  if (err) {
    console.error('Error fetching data:', err);
    return;
  }

  if (resp.statusCode !== 200) {
    console.error('Movie data fetch failed:', resp.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Now fetch character list data in /films/ endpoint.
  const charPromises = characters.map((charUrl) => {
    return new Promise((resolve, reject) => {
      request(charUrl, (er, res, charBody) => {
        if (er) {
          reject(er);
          return;
        }

        if (res.statusCode !== 200) {
          reject(new Error(`Fetch fail: ${res.statusCode}`));
          return;
        }

        const charData = JSON.parse(charBody);
        resolve(charData.name);
      });
    });
  });

  Promise.all(charPromises)
    .then((charNames) => {
      charNames.forEach((name) => console.log(name));
    })
    .catch((err) => {
      console.error('Char fech error:', err);
    });
});
