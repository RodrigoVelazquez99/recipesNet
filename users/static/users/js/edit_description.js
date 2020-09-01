// Insert chef description in modal load
$('#edit_description_modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var description = button.data('description');
  $('#input_description').val(description);
});

// Delete values in modal when close
$('#edit_description_modal').on('hidden.bs.modal', function () {
  $('#input_description').val('');
});
