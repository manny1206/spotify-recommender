import { useState, useEffect } from "react"
import { TextField, Container } from "@mui/material"
import SpotifyWebApi from "spotify-web-api-node"
import axios from "axios"

import useAuth from "../useAuth"
import SearchResult from "./SearchResult"
import TrackPlayer from "./TrackPlayer"
import UserRecommendations from "./UserRecommendations"

const spotifyAPI = new SpotifyWebApi({
  clientId: "fc40f86251ce4a378422d00d57473fa1"
})

export default function Dashboard({ code }) {
  const accessToken = useAuth(code)

  const [search, setSearch] = useState("")
  const [searchResults, setSearchResults] = useState([])
  const [playingTrack, setPlayingTrack] = useState()
  const [recommendations, setRecommendations] = useState([])

  useEffect(() => {
    if (!accessToken) return
    spotifyAPI.setAccessToken(accessToken)
    console.log(accessToken)
    axios.get(`/recommend/${accessToken}`)
      .then(res => setRecommendations(res.data.tracks))
      
  }, [accessToken])

  useEffect(() => {
    if (!accessToken) return
    if (!search) return setSearchResults([])

    let cancel = false
    spotifyAPI.searchTracks(search)
      .then(res => {
        if (cancel) return
        setSearchResults(res.body.tracks.items.map(track => {
          const smallAlbumImage = track.album.images.reduce((smallest, image) => {
            if (image.height < smallest.height) return image
            return smallest
          }, track.album.images[0])

          return {
            artist: track.artists[0].name,
            title: track.name,
            uri: track.uri,
            albumUrl: smallAlbumImage.url
          }
        }))
      })

    return () => (cancel = true)
  }, [search, accessToken])

  const playTrack = (track) => {
    setPlayingTrack(track)
    setSearch("")
  }

  return (
    <>
      <Container className="d-flex flex-column py-2" style={{ height: "100vh" }}>
        <TextField
          fullWidth
          margin="normal"
          label="Search Songs/Artists"
          value={search}
          onChange={s => setSearch(s.target.value)} />
        <div className="flex-grow-1 my-2" style={{ overflowY: "auto" }}>
          {searchResults.map(track => (
            <SearchResult track={track} key={track.url} playTrack={playTrack} />
          ))}
          {searchResults.length === 0 && (
            <UserRecommendations recommendations={recommendations} playTrack={playTrack}/>
          )}

        </div>
        <div>
          <TrackPlayer accessToken={accessToken} trackUri={playingTrack?.uri} />
        </div>
      </Container>
    </>
  )
}
