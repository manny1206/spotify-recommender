import React from "react"
import Button from "@mui/material/Button"
import Container from "@mui/material/Container"
import { Typography } from "@mui/material"

const SPOTIFY_CLIENT_ID = "fc40f86251ce4a378422d00d57473fa1" // change later
const SPOTIFY_REDIRECT_URI = "http://localhost:3000"
const SPOTIFY_SCOPE = "streaming%20user-read-email%20user-read-private%20user-library-read%20user-library-modify%20user-read-playback-state%20user-modify-playback-state%20user-top-read%20user-read-recently-played"
const SPOTIFY_AUTH_URL = `https://accounts.spotify.com/authorize?client_id=${SPOTIFY_CLIENT_ID}&response_type=code&redirect_uri=${SPOTIFY_REDIRECT_URI}&scope=${SPOTIFY_SCOPE}`

export default function Login() {
  return (
    <div style={{margin: 0, position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)"}}>
      <Typography className="row justify-content-center" variant="h2">
        Spotify Recommender!
      </Typography>
      <Container className="d-flex justify-content-center" maxWidth="sm" style={{ minHeight: "100%" }}>
        <Button variant="contained" color="success" style={{ borderRadius: 50 }} href={SPOTIFY_AUTH_URL}>
          Login With Spotify
        </Button>
      </Container>
    </div>
  )
}
