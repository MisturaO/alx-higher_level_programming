/* global $ */

$('DIV#toggle_header').on('click', function () {
  const header = $('header');

  header.toggleClass('red green');
});
