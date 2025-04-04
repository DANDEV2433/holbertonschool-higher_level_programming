document.querySelector('#add_item').addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'item';
  document.querySelector('ul.my_list').appendChild(li);
});
