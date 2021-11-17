import React from 'react'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

export default function UserLibraryCard({track, playTrack}) {
  const handlePlayOnClick = () => {
    playTrack(track)
  }

  return (
    <Card sx={{ maxWidth: 256 }} onClick={handlePlayOnClick}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="256"
          image={track.albumUrl}
          alt="Album Cover"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {track.title}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {track.artist}
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  )
}
