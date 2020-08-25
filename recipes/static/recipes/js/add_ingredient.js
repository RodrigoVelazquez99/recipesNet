addButton = document.getElementById('add_ingredient');
list_ingredients = document.getElementById('ingredients_list');

// Counter for button's id
var counter = 0;

// Al buttons for delete input that HTML generated at beginning, add EventListener 'deleteInput'
$("button[id^='delete_ingredient_']").on('click', deleteInput);

// Delete the input asociate with the button clicked
function deleteInput(event) {
  button = event.target;
  div = button.parentNode;
  div.parentNode.removeChild(div);
}

// Add an input with it's button to delete
function addInput() {
  str =
  "<div class='container pt-1'>" +
    "<input type='text' name='ingredient' required>" +
    "<button id='delete_ingredient" + counter.toString() +
    "' class='btn btn-danger' type='button' name='button'>Eliminar</button>" +
  "</div>"
  list_ingredients.insertAdjacentHTML('beforeend', str);
  newButton = document.getElementById('delete_ingredient' + counter.toString());
  newButton.addEventListener('click', deleteInput)
  counter++;
}

addButton.addEventListener('click', addInput);
