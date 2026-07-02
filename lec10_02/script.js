let handleResolved = (data) => {
  console.log("Promise resolved, data:", data);
};

let handleError = (error) => {
  console.log("Promise error, error: ", error);
};

// Create a new custom promise
let p = new Promise((resolve, reject) => {
  // resolve is a function to call when you want to resolve the Promise
  // reject is a function to call to raise an error if needed

  // Exercise: make the console print "Promise resolved, data: Hello world"
  // you can't write any console.log statements yourself
  //  or call handleResolved in this function
  
  // your code here
});

p.then(handleResolved)
 .catch(handleError);