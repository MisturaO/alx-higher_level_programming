/* global $ */

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const unorderedList = $('UL#list_movies');
  unorderedList.append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
