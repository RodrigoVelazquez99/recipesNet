$('#delete_post_modal').on('shown.bs.modal', function(event) {
  var button = $(event.relatedTarget);
  var id = button.data('post');
  document.getElementById('delete_post').href = '/home/post/delete/' + id.toString();
})
