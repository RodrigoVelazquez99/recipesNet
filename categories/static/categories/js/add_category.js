$('#alert_error_category').hide();
/**
* When submit form, send an AJAX request for checking if name is unique.
*/
$('#form_category').on('submit', function () {

  var post_url = '/categories/new/';
  var formData = new FormData(this);

  $.ajax({
    url : post_url,
    type : 'POST',
    data : formData,
    processData : false,
    contentType : false,
    success: function(response){
      if (response.content.repeated_category){
        $('#alert_error_category').show();
      } else {
        window.location.href = response.content.redirect_url;
      }
    },
  });
  return false;
});

$('#close_alert').on('click', function(){
  $('#alert_error_category').hide();
});

$('#new_category_modal').on('hidden.bs.modal', function () {
  $('#input_name').val("");
});
