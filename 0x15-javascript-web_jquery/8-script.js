/* script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json */

const moviesList = $('UL#list_movies');

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (data) {
    $.each(data.results, function (i, film) {
      const item = '<li>' + film.title + '</li>';
      moviesList.append(item);
    });
  }
});
