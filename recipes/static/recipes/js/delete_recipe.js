$('#delete_recipe_modal').on('shown.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var id = button.data('recipe');
  var name = button.data('name');
  document.getElementById("recipe_modal").innerHTML = name;
  document.getElementById("delete_recipe").href = '/recipes/delete/' + id.toString();
})
