$(document).on('click', '[data-toggle="lightbox"]', function(event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});

var last_image_index = 0;
var captions = {};

$(document).ready(function(){
  //console.log("ASDASD!");
  $.ajax({
    url: '/get_page_data',
    type: 'POST',
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    data: JSON.stringify({"last_image_index": last_image_index}),
    success: function(data, status) {
      console.log("Data: " + data );
      // data = sample_json
      if('images' in data) {
        load_images(data['images'])
      }
      else {
        alert('No Images, Please Upload an image!')
      }
      if('last_image_index' in data) {
        var new_last_image_index = data['last_image_index']
        if (new_last_image_index == last_image_index) {
          alert('All images loaded!')
        }
        last_image_index = new_last_image_index
      }
      else {
        console.log('Something wrong in JSON response.');
      }
    },
    error: function() {
      console.log("Error in getting data!!");
    }
  });
});

function load_images(images) {
  console.log(images.length);
  var single_html = "<div class=\"col-md-3 portfolio-item\">\
    <a class=\"lightbox_img\" href=\"{0}\" id=\"{1}\" data-toggle=\"lightbox\" data-gallery=\"example-gallery\" data-title=\"{2}\" data-footer=\"<div><span class='cptn-btn'><button class='btn btn-default' onclick='caption_img({3})'>Caption Button</button></span></div>\">\
      <img class=\"img-responsive\" src=\"{0}\"></a></div>"
  for(var i=0; i<images.length; i++) {
    var link = images[i]['img_url']
    var img_id = images[i]['img_id']
    var caption = images[i]['caption'] || "<span id='img_cptn_"+img_id+"'></span>"
    var h = $.validator.format(single_html,[link, 'img_'+img_id, caption, img_id])
    console.log(h);
    $('.images-div').append(h)
  }
}


function caption_img(img_id) {
  var caption = 'Caption for image '+ img_id
  console.log(caption);
  captions[img_id] = caption
  $('#img_cptn_'+img_id).text(caption)
}
