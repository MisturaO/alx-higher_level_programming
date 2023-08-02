/* global $ */

// JavaScript script that updates the text color of the <header> element
// to red (#FF0000) when the user clicks on the tag 'DIV#red_header', using jQuery

// // This will attach a click event listener to the <div> with ID "red_header"
$('DIV#red_header').on('click', function () {
  // Selects update the text color of the <header> element to red (#FF0000)
  // using jQuery selector and css methods.
  $('header').css('color', '#FF0000');
});
