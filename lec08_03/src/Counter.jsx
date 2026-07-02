import React, { useState, useEffect } from "react";

export default function Counter({ startValue }) {
   const [val, setVal] = useState(startValue);
  
   const reset = () => {
      setVal(startValue);
   };

   const increment = () => {
      setVal(val + 1);
   };

   return (
      <div>
         <button onClick={reset}>Reset</button>
         <button onClick={increment}>Increment</button>
         <p>{val}</p>
      </div>
   );
}
