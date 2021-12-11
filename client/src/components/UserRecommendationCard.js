import React from 'react'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

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
          <Typography gutterBottom variant="h5" component="div">
            {track.name.substring(0, 20)}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {track.artist}
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  )
}
