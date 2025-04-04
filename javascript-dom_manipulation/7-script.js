fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    const list = document.getElementById('list_movies');
    movies.forEach(movie => {
      const ulItem = document.createElement('li');
      ulItem.textContent = movie.title;
      list.appendChild(ulItem);
    });
  })
  .catch(error => {
    console.error('Error fetching movie:', error);
  });
