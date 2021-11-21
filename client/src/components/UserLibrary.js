import {useState, useEffect} from "react"
import Grid  from "@mui/material/Grid"
import SpotifyWebApi from "spotify-web-api-node"
import UserLibraryCard from "./UserLibraryCard";

const spotifyAPI = new SpotifyWebApi({
  clientId: "fc40f86251ce4a378422d00d57473fa1"
})

export default function UserLibrary({ accessToken, playTrack }) {
  const [userLibrary, setUserLibrary] = useState([])

  useEffect(() => {
    if (!accessToken) return
    spotifyAPI.setAccessToken(accessToken)
  }, [accessToken])

  useEffect(() => {
    if (!accessToken) return

    let loaded = true
    spotifyAPI.getMySavedTracks({limit: 50})
      .then(res => {
        console.log(res)
        if (loaded) return
        setUserLibrary(res.body.items.map(track => {
          const largeAlbumImage = track.track.album.images.reduce((largest, image) => {
            if (image.height > largest.height) return image
            return largest
          }, track.track.album.images[0])

          return {
            artist: track.track.artists[0].name,
            title: track.track.name,
            uri: track.track.uri,
            albumUrl: largeAlbumImage.url
          }
        }))
      })

    return () => (loaded = false)
  }, [userLibrary])

  return (
    <div className="d-flex m-2 align-items-center" style={{cursor: "pointer"}}>
      <Grid container spacing={2}>
        {userLibrary.map(track => (
          <UserLibraryCard track={track} playTrack={playTrack}/>
        ))}
      </Grid>
    </div>
  )
}
