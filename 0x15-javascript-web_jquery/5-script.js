/* global $ */

$('DIV#toggle_header').on('click', function () {
    const newElement = $('<li>Item</li>');

    $('UL.my_list').append(newElement)
})