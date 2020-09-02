list_coments = document.getElementById('coments_post');

// Add the message to modal
function add_coment(message) {
  str = "<h5>" + message + "</h5>";
  list_coments.insertAdjacentHTML('beforeend', str);
}

// Get all coments of post
$('#coment_post_modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var post = button.data('post');
  var url = "/home/post/coment/" + post.toString();
  $.ajax({
    url : url,
    type : 'GET',
    success: function(response) {
      var list = response.content.coments;
      for (var key in list) {
        item = list[key];
        add_coment(item.message);
      }
    }
  });
});

// Delete all coments when close modal
$('#coment_post_modal').on('hidden.bs.modal', function () {
  list_coments.innerHTML = "";
});
