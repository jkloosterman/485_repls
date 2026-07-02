function requestData() {
  const nameSpan = document.getElementById("name");
  const nationalitySpan = document.getElementById("nationality");
  
  // fetch an astronaut from a URL
  fetch(`https://jkloosterman.net/485/astronauts/1.json`)
    .then((response) => {
      // this interprets the text as JSON
      return response.json();
    })
    .then((data) => {
      // this does something with the data
      console.log(data);

      // Exercise 1: print the name and nationality of the astronaut
      // your code here
      nameSpan.innerHTML = "Name goes here";
      nationalitySpan.innerHTML = "Nationality goes here";
    });
}

// Exercise 2: add an input box that allows you to request a different astronaut ID.
// Hints:
// 1. <input type="number" value="1"/> creates an input field for a number
// 2. if astronautIdInput is a reference to this HTML element, you can read the number with
//      astronautIdInput.value
// 3. JavaScript format strings look like this: `the value of number is: ${number}`