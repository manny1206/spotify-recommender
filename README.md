# CS484 Final Project

## Submission Information

### Student Information

*Please fill in this information before submission*

* **Student Name: Emmanuel Jones** 
* **Student G-Number: G01124882** 

* **Student Name: Ron Phung** 
* **Student G-Number: G01194319** 
* **Heroku Deployment URL: https://spotify-recommender-ejrp.herokuapp.com/ **

### Documentation of the Recommender Components

*Here please describe your (at least) 5 different React components as well as the overall purpose of your web application. We provide an example below of what we expect this documentation to look like.*

**General App Description:** Loads a recent list of liked tracks from a users Spotify library, that they can play. Also let's users search for and play specific songs

* **App:** Displays the Login component or Dashboard component, depending on whether user is logged in
  * *Functionality:* Houses the login and dashboard 
  * *Interactivity:* The user doesn't directly interact with this, since it immediately renders Login or Dashboard

* **Login:** Displays the login button and start screen
  * *Functionality:* Lets users login to their Spotify account before accessing the app.
  * *Interactivity:* The user clicks the Login button

* **Dashboard:** The main screen for displaying all of the Spotify content
  * *Functionality:* Lets users search for tracks and displays their recommended tracks
  * *Interactivity:* The user searchs for tracks and clicks them. The users clicks on recommended tracks from the Recommendations component

* **SearchResult:** Displays a particular search result from the list of searchResults retrieved in Dashboard
  * *Functionality:* Shows simple information about search result
  * *Interactivity:* The user can click on it to start playing the song

* **UserRecommendations:** The current user's recommeded tracks
  * *Functionality:* Lets users immediately see songs recommended, without having to search
  * *Interactivity:* The user can click on a song's UserRecommendationsCard in the grid of songs to play it

* **UserRecommendationsCard:** Display a card of a particular song to be used in the grid in UserRecommendations
  * *Functionality:* Shows simple information about a song in UserRecommendations
  * *Interactivity:* The user can click the card to play the song

* **TrackPlayer:** A player where the user can play songs from spotify
  * *Functionality:* Lets the user play the songs clicked on from search or their UserRecommendations
  * *Interactivity:* The user can play/pause or like/unlike a song they clicked on from searching or their recommendations

## Running this Project Locally

Make sure you have [Node.js](http://nodejs.org/) and (optionally) the [Heroku CLI](https://cli.heroku.com/) installed. You only need the Heroku CLI installed if you plan to deploy the project from the CLI instead of the Heroku web interface.

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

