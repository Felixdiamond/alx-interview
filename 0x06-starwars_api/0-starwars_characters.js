#!/usr/bin/node
// Import the request module
const request = require('request');
// Get the movie ID from the first positional argument
const movieId = process.argv[2];
// Construct the URL for the API request using the movie ID
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a request to the /films/ endpoint of the Star Wars API
request(url, function (error, response, body) {
  // Handle any errors that may occur
  if (error) {
    console.error(error);
  } else {
    // Parse the response body as JSON
    const characters = JSON.parse(body).characters;
    // Iterate over the array of character URLs
    for (const character of characters) {
      // Make a request to each character's URL to retrieve their name
      request(character, function (error, response, body) {
        // Handle any errors that may occur
        if (error) {
          console.error(error);
        } else {
          // Parse the response body as JSON and print the character's name
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});

