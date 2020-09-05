list_coments = document.getElementById('coments_post');

// Add the message to modal
function add_coment(message) {
  str = "<h5>" + message + "</h5>";
  list_coments.insertAdjacentHTML('beforeend', str);
}


$('#coment_post_modal').on('shown.bs.modal', function (event) {
  document.getElementById('new_coment').focus();
});

// Get all coments of post when open modal
$('#coment_post_modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var post = button.data('post');
  var url = "/home/post/coment/" + post.toString();
  $.ajax({
    url : url,
    type : 'GET',
    success: function(response) {
      var list = response.content.coments;
      if (list.length == 0) {
        str = "<h5 id='empty_coments'> No tiene comentarios </h5>";
        list_coments.insertAdjacentHTML('beforeend', str);
        return;
      }
      for (var key in list) {
        item = list[key];
        add_coment(item.message);
      }
    }
  });
});

// Get the id from button and set the input in form.
function setIdPost() {
  var button = $(this);
  var id = button.data('post');
  $('#id_post_coment').val(id);
}

// For every button coment, asign a function which send the id_post to form.
$("button[id^='coment_button_']").on('click', setIdPost);


// Send coment to server
$('#form_coment_post').on('submit', function () {
  var post = document.getElementById('id_post_coment').value;
  var url_post = "/home/post/coment/" + post.toString();
  var new_coment = document.getElementById('new_coment').value;
  var formData = new FormData(this);
  $.ajax({
    url : url_post,
    type : 'POST',
    data : formData,
    processData : false,
    contentType : false,
    success: function (response) {
      if (response.ok) {
        document.getElementById('new_coment').value = "";
        var empty = document.getElementById('empty_coments');
        if (empty) {
          empty.parentNode.removeChild(empty);
        }
        add_coment(new_coment);
      }
    }
  });

  return false;
});

// Delete all coments when close modal
$('#coment_post_modal').on('hidden.bs.modal', function () {
  list_coments.innerHTML = "";
  document.getElementById('new_coment').value = "";
});
