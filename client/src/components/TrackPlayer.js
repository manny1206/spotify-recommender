import {useState, useEffect} from 'react'
import SpotifyPlayer from "react-spotify-web-playback"

export default function TrackPlayer({accessToken, trackUri}) {
  const [play, setPlay] = useState(false)

  useEffect(() => {
    setPlay(true)
  },[trackUri])

  return (
    <>
      {accessToken && 
        <SpotifyPlayer 
          showSaveIcon 
          token={accessToken} 
          uris={trackUri ? [trackUri] : []} 
          play={play}
          callback={playState => {if (!playState.isPlaying) setPlay(false)}}
        />
      }
    </>
  )
}
