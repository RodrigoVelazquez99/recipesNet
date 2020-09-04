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
        var buttons = document.querySelectorAll("[id='like_button_" + id.toString() + "']");
        for (var i = 0; i < buttons.length; i++) {
          buttons[i].className = "btn btn-outline-success";
          buttons[i].innerHTML = "Unlike";
        }
      } else {
        var buttons = document.querySelectorAll("[id='like_button_" + id.toString() + "']");
        for (var i = 0; i < buttons.length; i++) {
          buttons[i].className = "btn btn-success";
          buttons[i].innerHTML = "Like";
        }
      }
      var likes_count_text = document.querySelectorAll("[id='likes_count_" + id.toString() + "']")
      for (var i = 0; i < likes_count_text.length; i++) {
        likes_count_text[i].innerHTML = 'Likes : ' + response.content.likes_count;
      }
    }
  });
}

// Get all buttons for like and set a listener
$("button[id^='like_button_']").on('click', like)
