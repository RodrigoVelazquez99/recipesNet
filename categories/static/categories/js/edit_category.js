$('#alert_error_category_edit').hide();

/**
* When submit form, send an AJAX request for checking if new_name is unique.
*/
$('#form_category_edit').on('submit', function () {
  var post_url = '/categories/edit/';
  var formData = new FormData(this);

  $.ajax({
    url : post_url,
    type : 'POST',
    data : formData,
    processData : false,
    contentType : false,
    success : function(response) {
      if (response.content.repeated_category) {
        $('#alert_error_category_edit').show();
      } else {
        window.location.href = response.content.redirect_url;
      }
    }
  });
  return false;
});

$('#close_alert_edit').on('click', function() {
  $('#alert_error_category_edit').hide();
});

$('#edit_category_modal').on('shown.bs.modal', function(event) {
  var button = $(event.relatedTarget);
  var old_name = button.data('name');
  $('#input_name_edit').val(old_name);
  $('#input_old_name_edit').val(old_name);
})

$('#edit_category_modal').on('hidden.bs.modal', function() {
  $('#input_name_edit').val("");
  $('#input_old_name_edit').val("");
  $('#alert_error_category_edit').hide();
})
