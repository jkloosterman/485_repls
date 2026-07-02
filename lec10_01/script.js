function pageLoaded() {
  fetch("https://jkloosterman.net/485/a.json")
    .then((response) => { 
      return response.json();
    })
    .then((data) => {
      console.log("A");
    });

  fetch("https://jkloosterman.net/485/b.json")
    .then((response) => { 
      return response.json();
    })
    .then((data) => {
      console.log("B");
    });

  console.log("C");
}