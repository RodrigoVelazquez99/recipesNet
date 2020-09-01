// Hide alert on load page
$('#alert_username_edit').hide();

// Insert current username in modal on load
$('#edit_name_modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var username = button.data('username');
    $('#input_new_username').val(username);
    $('#input_old_username').val(username);
});

// Delete values in modal form when close and close alert if exist
$('#edit_name_modal').on('hidden.bs.modal', function() {
  $('#input_new_username').val('');
  $('#input_old_username').val('');
  $('#alert_username_edit').hide();
});

// When form submit check is username is unique
$('#form_edit_username').on('submit', function () {
  var post_url = '/profile/edit_username/';
  var formData = new FormData(this);

  $.ajax({
    url : post_url,
    type : 'POST',
    data : formData,
    processData : false,
    contentType : false,
    success : function(response) {
      if (response.content.repeated_username) {
        $('#alert_username_edit').show();
      } else {
        window.location.href = response.content.redirect_url;
      }
    }
  });

  return false;
});

// Hide alert instead destroy
$('#close_alert_edit_username').on('click', function() {
  $('#alert_username_edit').hide();
});
