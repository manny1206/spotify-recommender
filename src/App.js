import React, { useState, useEffect } from 'react'
import './App.css'

function App() {
  // Initialize state
  const [cities, setCities] = useState([])

  const citez = ["Fairfax", "Vienna", "Falls Church", "Arlington"]
  useEffect(() => {
    setCities(citez)
  })

  return (
    <div className="App">
      {/* Render the cities*/}
      <div>
        <h1>Cities</h1>
        <ul className="cities">
          {cities.map((city, index) =>
            <li key={index}>
              {city}
            </li>
          )}
        </ul>
      </div>
    </div>
  )
}

export default App
