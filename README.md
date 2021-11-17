# SWE-432 HW-4 Starter Application

## Submission Information

### Student Information

*Please fill in this information before submission*

* **Student Name: Emmanuel Jones** 
* **Student G-Number: G01124882** 
* **Heroku Deployment URL: https://emmanuel-jones-swe432-hw4.herokuapp.com/ **

### Documentation of your Web App and React Components

*Here please describe your (at least) 5 different React components as well as the overall purpose of your web application. We provide an example below of what we expect this documentation to look like.*

**General App Description:** Loads a recent list of liked tracks from a users Spotify library, that they can play. Also let's users search for and play specific songs

* **App:** Displays the Login component or Dashboard component, depending on whether user is logged in
  * *Functionality:* Houses the login and dashboard 
  * *Interactivity:* The user doesn't really interact, since it immediately renders Login or Dashboard

* **Login:** Displays the login button on the start screen
  * *Functionality:* Lets users login to their Spotify account before accessing the app.
  * *Interactivity:* The user clicks the Login button

* **Dashboard:** The main screen for displaying all of the Spotify content
  * *Functionality:* Lets users search for tracks and displays their recently liked tracks
  * *Interactivity:* The user searchs for tracks and clicks them. The users clicks on liked tracks from the UserLibrary component

* **SearchResult:** Displays a particular search result from the list of searchResults retrieved in Dashboard
  * *Functionality:* Shows simple information about search result
  * *Interactivity:* The user can click on it to start playing the song

* **UserLibrary:** The current user's library of liked tracks (only shows last 50)
  * *Functionality:* Lets users immediately see songs already in their library, without having to search
  * *Interactivity:* The user can click on a song's UserLibraryCard in the grid of songs to play it

* **UserLibaryCard:** Display a card of a particular song to be used in the grid in UserLibrary
  * *Functionality:* Shows simple information about a song in UserLibrary
  * *Interactivity:* The user can click the card to play the song

* **TrackPlayer:** A player where the user can play songs from spotify
  * *Functionality:* Lets the user play the songs clicked on from search or their UserLibrary
  * *Interactivity:* The user can play/pause or like/unlike a song they clicked on from searching or their library
## Project Overview

This repo contains a barebones React app with a single component. You will use this as the "base" version of your Interactive Front-end application for HW Assignment #4. You will simply create a copy of this repo through GitHub classroom and then work in that repo. 

## Homework Assignment 4 Detailed Instructions

You can find the detailed instructions for HW Assignment #4 on the [course webpage](https://cs.gmu.edu/~kpmoran/teaching/swe-432-f21/hw4). Please read these carefully before getting started.

## Running this Project Locally

Make sure you have [Node.js](http://nodejs.org/) and (optionally) the [Heroku CLI](https://cli.heroku.com/) installed. You only need the Heroku CLI installed if you plan to deploy the project from the CLI instead of the Heroku web interface. See the [HW Assignment #4 instructions](https://cs.gmu.edu/~kpmoran/teaching/swe-432-f21/hw4) for more details.

*Note the following commands assume a Unix-based enviornment. If you are on windows, you may need to use something such as Windows Subsystem for Linux (https://docs.microsoft.com/en-us/windows/wsl/about).*

```sh
$ git clone <repo-name>
$ cd <repo-name>
$ npm install
$ npm start
```

After executing these commands, your express backend and React frontend should now be running on [localhost:5000](http://localhost:5000/). You can visit this page in your web browser to view your front-end user interface. You can also access your microservice endpoints (e.g., [localhost:5000/cities](http://localhost:5000/cities). Please see the [HW #3 instructions](https://cs.gmu.edu/~kpmoran/teaching/swe-432-f21/hw3) for more information on how this works.

## Deploying to Heroku

Check out [our instructions](https://cs.gmu.edu/~kpmoran/teaching/swe-432-f21/hw3) for deploying your application to Heroku. You can use the button below for quick access to your Heroku account.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Testing with Continuous Integration

**Note that you are not required to test your project with Jest for HW3, however, we have enabled this functionality in case you would like to use it. If you would like to remove the tests, you can remove the `.github` directory from the repo.**

Currently, this repo is set up to run the Jest tests in the `App.test.js` file upon each commit to the `main` branch of the repository. If any of the tests fail, the CI process will fail and this will be indicated with red "X" on the main page of your repo, and GitHub will likely also send you a notification email that your automated tests have failed.

Currently, the tests are configured to run by getting deployed to a remote virtual server with an Ubuntu operating system, where the `npm install` and `npm test` commands are executed.

Note that we have included the [`jest-dom`](https://testing-library.com/docs/ecosystem-jest-dom/) library for your tests. This allows you to check DOM elements in your tests.

You can find the [GitHub Actions](https://github.com/features/actions) script for this CI job [here](.github/workflows/ci.yml) if you want to learn more.

## Additional Resources

For more information about using Node.js on Heroku, see these Heroku Dev Center articles:

- [React Tutorial](https://reactjs.org/tutorial/tutorial.html)
- [Express Documentation](https://expressjs.com/en/5x/api.html)
- [Supertest Documentation](https://www.npmjs.com/package/supertest)
- [Getting Started on Heroku with Node.js](https://devcenter.heroku.com/articles/getting-started-with-nodejs)
- [Heroku Node.js Support](https://devcenter.heroku.com/articles/nodejs-support)
- [Node.js on Heroku](https://devcenter.heroku.com/categories/nodejs)
- [Best Practices for Node.js Development](https://devcenter.heroku.com/articles/node-best-practices)
