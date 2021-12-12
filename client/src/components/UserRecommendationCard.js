import React from 'react'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Typography from '@mui/material/Typography'
import CardActionArea from '@mui/material/CardActionArea'

export default function UserRecommendationCard({track, playTrack}) {
  const handlePlayOnClick = () => {
    playTrack(track)
  }

  return (
    <Card sx={{ maxWidth: 128 }} onClick={handlePlayOnClick}>
      <CardActionArea>
      <CardMedia
          component="img"
          height="128"
          image={(track.album.images.reduce((largest, image) => {
                  if (image.height > largest.height) return image
                  return largest
                }, track.album.images[0])).url}
          alt="Album Cover"
        />
        <CardContent>
          <Typography gutterBottom variant="subtitle1" component="div">
            {track.name.length < 22 ? track.name : track.name.substring(0, 22) + "..."}
          </Typography>
          <Typography variant="subtitle2" color="text.secondary">
            {track.artists[0].name}
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  )
}
