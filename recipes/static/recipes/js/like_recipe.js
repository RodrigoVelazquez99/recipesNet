$('#like_button').on('click', function () {
  var id = $(this).data('recipe');
  var url = "/recipes/like/" + id.toString();
  var form = {'id_recipe' : id }

  $.ajax({
    url : url,
    type : "GET",
    data: form,
    success:function(response){
      if (response.content.flag) {
        document.getElementById('like_button').className = "btn btn-outline-success";
        document.getElementById('like_button').innerHTML = "Unlike";
      } else {
        document.getElementById('like_button').className = "btn btn-success";
        document.getElementById('like_button').innerHTML = "Like";
      }
      document.getElementById('likes_count').innerHTML = response.content.likes_count;
    },
  });
})
