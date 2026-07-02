function pageLoaded() {
  // Get references to HTML elements inside JavaScript
  let incrementButton = document.getElementById("increment");
  let printButton = document.getElementById("print");

  // Notice that both of the inner functions can
  //  access this variable because this is in an
  //  outer scope
  let val = 0;

  // Event handler for Increment button
  const incrementHandler = function() {
    val++;
  };
  incrementButton.onclick = incrementHandler;

  // Event handler for Print button
  const printHandler = function() {
    alert(`The value is ${val}`);
  };
  printButton.onclick = printHandler;

  // Exercise: add a "Clear" button that resets the value to 0
  // You will need to modify both the HTML and JavaScript
}