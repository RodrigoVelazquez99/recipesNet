$('#delete_category_modal').on('shown.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var id = button.data('category');
  document.getElementById('button_delete_category').href = '/categories/delete/' + id.toString();
});
