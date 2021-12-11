import {useState, useEffect} from "react"
import Grid  from "@mui/material/Grid"
import UserRecommendationCard from "./UserRecommendationCard"

export default function UserRecommendations({ recommendations, playTrack }) {
  const [userRecommendations, setUserRecommendations] = useState([])
  

  useEffect(() => {
    if (!recommendations) return
    setUserRecommendations(recommendations)
    console.log(recommendations)
  }, [recommendations])

  return (
    <div className="d-flex m-2 align-items-center" style={{cursor: "pointer"}}>
      <Grid container>
      {userRecommendations.map(track => (
          <UserRecommendationCard track={track} playTrack={playTrack}/>
        ))}
      </Grid>
    </div>
  )
}
