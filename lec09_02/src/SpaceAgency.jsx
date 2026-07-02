import React, { useState, useEffect } from "react";
// For next exercise, ignore until then
import Spacecraft from './Spacecraft'

export default function SpaceAgency({id}) {
  const [name, setName] = useState("");
  const [spacecraft, setSpacecraft] = useState([]);

  useEffect(() => {
    fetch(`https://jkloosterman.net/485/agency/${id}.json`)
      .then((response) => { 
          return response.json(); 
      })
      .then((data) => {
          setName(data.name);
          setSpacecraft(data.spacecraft_list)
      });
  }, [id]);

  // Exercise: change this to print out the name and history of each spacecraft
  // Hint: look at the JSON in your browser to see the format

  // Bonus: make a similar list of launchers
  
  return (
    <div>
      <h2>{name} (ID {id})</h2>
      <h3>Spacecraft List</h3>
      <ul>
        {spacecraft.map((craft) => 
          <li key={craft.id}>
            <b>Maiden Flight:</b> {craft.maiden_flight} 
          </li>
        )}
      </ul>
    </div>
  )
}
