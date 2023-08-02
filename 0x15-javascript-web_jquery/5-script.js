/* global $ */

$('DIV#add_item').on('click', function () {
  const newElement = $('<li>Item</li>');

  $('UL.my_list').append(newElement);
});
