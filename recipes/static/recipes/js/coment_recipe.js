$('#coment_modal').on('shown.bs.modal', function(event) {
  var button = $(event.relatedTarget);
  var id = button.data('recipe');
  document.getElementById('input_recipe_coment').value = id;
})
