#!/usr/bin/node
// Import the request and util modules
const request = require('request');
const util = require('util');
// Create a version of request.get that returns a promise
const get = util.promisify(request.get);
// Get the movie ID from the first positional argument
const movieId = process.argv[2];
// Construct the URL for the API request using the movie ID
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

async function main () {
  // Make a request to the /films/ endpoint of the Star Wars API
  const response = await get(url);
  // Parse the response body as JSON
  const characters = JSON.parse(response.body).characters;
  // Iterate over the array of character URLs
  for (const character of characters) {
    // Make a request to each character's URL to retrieve their name
    const res = await get(character);
    // Parse the response body as JSON and print the character's name
    console.log(JSON.parse(res.body).name);
  }
}

// Call the main function to run the script
main();
