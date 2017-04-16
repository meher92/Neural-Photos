$(document).on('click', '[data-toggle="lightbox"]', function(event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});

var captions = {}

function caption_img(img_id) {
  var caption = 'Caption for image '+ img_id
  console.log(caption);
  captions[img_id] = caption
  $('#img_cptn_'+img_id).text(caption)
}
