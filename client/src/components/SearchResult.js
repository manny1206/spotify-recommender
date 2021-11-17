import React from "react"

export default function SearchResult({track, playTrack}) {
  const handlePlayOnClick = () => {
    playTrack(track)
  }
  
  return (
    <div className="d-flex m-2 align-items-center" style={{cursor: "pointer"}} onClick={handlePlayOnClick}>
      <img src={track.albumUrl} style={{height: "64px", width: "64px"}}/>
      <div className="ml-3">
        <h1>{track.title}</h1>
        <h2 className="text-muted">{track.artist}</h2>
      </div>
    </div>
  )
}
