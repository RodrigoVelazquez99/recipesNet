// Show alert when modal load
$('#edit_password_modal').on('show.bs.modal', function () {
  $('#alert_password').show();
});

// Clear inputs in form and hide alert on close modal
$('#edit_password_modal').on('hidden.bs.modal', function () {
  $('#password').val('');
  $('#password_confirm').val('');
  $('#alert_password').hide();
});

// Hide alert when button clicked
$('#close_alert_edit_password').on('click', function () {
  $('#alert_password').hide();
});
