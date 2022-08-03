


$.ajax({
  type:'GET',
  url: '/data/bsc/',
  success: function(response){
    console.log(response.tokens);
    const data = response.tokens;
    const table = document.getElementById('list-of-tokens');
    data.forEach(el => {
      table.innerHTML += `
        <tr>
          <td>${el.name}/${el.symbol}</td>
          <td>${el.address}</td>
          <td>
            <a href="${el.scannerLink}">BSC</a>
            <a href="${el.exchangerLink}">POOCOIN</a>
          </td>
        </tr>
      `;
    });
  },
  error: function(error){
    console.log(error);
  }
});
