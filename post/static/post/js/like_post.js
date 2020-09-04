// Send an AJAX request with the given post
function like() {
  var button = $(this);
  var id = button.data('post');
  var url = '/home/post/like/' + id.toString();
  $.ajax({
    url : url,
    type : 'GET',
    success: function (response) {
      if (response.content.flag) {
        document.getElementById('like_button_' + id.toString()).className = "btn btn-outline-success";
        document.getElementById('like_button_' + id.toString()).innerHTML = "Unlike";
      } else {
        document.getElementById('like_button_' + id.toString()).className = "btn btn-success";
        document.getElementById('like_button_' + id.toString()).innerHTML = "Like";
      }
      document.getElementById('likes_count_' + id.toString()).innerHTML = 'Likes : ' + response.content.likes_count;
    }
  });
}

// Get all buttons for like and set a listener
$("button[id^='like_button_']").on('click', like)
