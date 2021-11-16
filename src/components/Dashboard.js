import { useState, useEffect } from "react"
import { TextField, Container } from "@mui/material"
import SpotifyWebApi from "spotify-web-api-node"
import useAuth from "./useAuth"

const spotifyAPI = new SpotifyWebApi({
  clientId: "fc40f86251ce4a378422d00d57473fa1"
})

export default function Dashboard({ code }) {
  const accessToken = useAuth(code)

  const [search, setSearch] = useState("")
  const [searchResults, setSearchResults] = useState("")

  useEffect(() => {
    if (!accessToken) return
    spotifyAPI.setAccessToken(accessToken)
  }, [accessToken])

  useEffect(() => {
    if (!accessToken) return
    if (!search) return setSearchResults([])
    spotifyAPI.searchTracks(search)
      .then(res => {
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

  }, [search, accessToken])
  return (
    <Container className="d-flex flex-column py-2" style={{ height: "100vh" }}>
      <TextField 
        fullWidth 
        margin="normal" 
        label="Search Songs/Artists" 
        value= {search} 
        onChange={s => setSearch(s.target.value)}
      />
      <div className="flex-grow-1 my-2" style={{ overflowY: "auto"}}>
        {searchResults.map(track => {
          <TrackSearchResult track={track} key={track.url} chooseTrack={chooseTrack}/>
        })}
      </div>
      <div>
        Bottom
      </div>
    </Container>
  )
}
