import {useState, useEffect} from "react"
import Container from "@mui/material/Container"
import Typography from "@mui/material/Typography"
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
    <Container maxWidth="md" style={{minHeight:"100vh"}}>
      <Grid container spacing={1} rowSpacing={0.5} columns={4}>
        <Grid item xs={12} style={{textAlign: "center", fontSize: "30px"}}>
          Song Recommendations
        </Grid>
      {userRecommendations.map(track => (
        <Grid item>
          <UserRecommendationCard track={track} playTrack={playTrack}/>
        </Grid>
      ))}
      </Grid>
    </Container>

      
    
  )
}
