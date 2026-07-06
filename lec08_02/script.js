function pageLoaded() {
  const startButton = document.getElementById("start");
  const clickme = document.getElementById("clickme");
  const results = document.getElementById("results");
  
  // Define some variables here if you need to
  let clicks = 0;
  
  startButton.onclick = () => {
    startButton.disabled = true;
    clickme.disabled = false;

    // Reset the number of times the user clicked the button
    // your code here

    const time_msec = 3000; // 3 seconds
    setTimeout(() => {
      // Disable the "Click Me!" button and enable the "Start" button
      // Tell the user how well they did
      
      // your code here
      results.innerHTML = `Message goes here!`;
    }, time_msec);
  };
  
  clickme.onclick = () => {
    // Track how many times the user clicked the button
    // your code here
  };
}

// Exercise 2: Add a high score tracker. You will need to modify the HTML
//  and JavaScript for this.  