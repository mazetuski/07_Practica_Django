document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(elems);
    var elems = document.querySelectorAll('select');
    M.FormSelect.init(elems );
  });