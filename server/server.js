const express = require("express")
const cors = require("cors")
const SpotifyWebAPI = require("spotify-web-api-node")

const app = express()
app.use(cors())
app.use(express.json())

app.post("/login", (req, res) => {
  const code = req.body.code
  const spotifyAPI = new SpotifyWebAPI({
    redirectUri: "http://localhost:3000",
    clientId: "fc40f86251ce4a378422d00d57473fa1",
    clientSecret: "fc84316bd37244a58a4327916855496d"
  })

  spotifyAPI.authorizationCodeGrant(code)
    .then(data => {
      res.json({
        accessToken: data.body.access_token,
        refreshToken: data.body.refresh_token,
        expiresIn: data.body.expires_in
      })
    })
    .catch((err) => {
      console.log(err)
      res.sendStatus(400)
    })
})

app.post("/refresh", (req, res) => {
  const refreshToken = req.body.refreshToken

  const spotifyAPI = new SpotifyWebAPI({
    redirectUri: "http://localhost:3000",
    clientId: "fc40f86251ce4a378422d00d57473fa1",
    clientSecret: "fc84316bd37244a58a4327916855496d",
    refreshToken
  })

  spotifyAPI.refreshAccessToken()
    .then(data => {
      res.json({
        accessToken: data.body.accessToken,
        expiresIn: data.body.expiresIn
      })
    })
    .catch(err => {
      console.log(err)
      res.sendStatus(400)
    })
})

app.listen(3001)