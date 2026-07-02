let handleResolved = (data) => {
  console.log("Promise resolved, data:", data);
}

// Create a new custom promise
let p = new Promise((resolve, reject) => {
  // resolve is a function to call when you want to resolve the Promise
  // reject is a function to call to raise an error if needed

  // your code here. Hint: use setTimeout
});
p.then(handleResolved);

// Add a message to the event queue
setTimeout(() => {
  console.log("Message 1");
}, 0);

// Exercise: make the console print
// Message 1
// Promise resolved, data: Message 2

/////////////////////////////////////

/* Uncomment later

// Promise Generators 
// Returns a promise that resolves by returning message
// after the given number of milliseconds
function wait(msec, message) {
  // your code here
}

// should print second
wait(1000, "2: prints after 1000ms")
.then((message) => {
  console.log(message);
});

// should print first
wait(500, "1: prints after 500ms")
.then((message) => {
  console.log(message);
});

*/
