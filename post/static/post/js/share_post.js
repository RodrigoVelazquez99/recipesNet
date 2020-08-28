$('#share_post_modal').on('shown.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var id =  button.data('post');
  document.getElementById('share_post').href = "/home/post/share/" + id.toString();
})
