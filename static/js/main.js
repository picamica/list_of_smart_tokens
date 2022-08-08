body = document.body;
body.onload = showTokens('bsc', 'BSCscan', 'POOCOIN');

const bscdiv = document.getElementById('bscdiv');
const ethdiv = document.getElementById('ethdiv');
const maticdiv = document.getElementById('maticdiv');
const ftmdiv = document.getElementById('ftmdiv');


bscdiv.addEventListener('click', function() {
  showTokens('bsc', 'BSCscan', 'POOCOIN');
});

ethdiv.addEventListener('click', function() {
  showTokens('eth', 'EtherScan', 'Uniswap');
});

maticdiv.addEventListener('click', function() {
  showTokens('matic', 'PolygonScan', 'QuickSwap');
});

ftmdiv.addEventListener('click', function() {
  showTokens('ftm', 'FtmScan', 'SpookySwap');
});

function showTokens(endpoint, scanner, exchanger) {
  const table = document.getElementById('list-of-tokens');
  table.replaceChildren();

  $.ajax({
    type:'GET',
    url: `/data/${endpoint}/`,
    success: function(response){
      console.log(response.tokens);
      const data = response.tokens;
      data.forEach(el => {
        const date = new Date(el.age);
        table.innerHTML += `
          <tr>
            <td>${el.name}/${el.symbol}</td>
            <td>${el.address}</td>
            <td>
              <a href=${el.Scanner}>${scanner}</a>
              <a href=${el.Exchange}>${exchanger}</a>
            </td>
            <td>${moment(el.created).fromNow()}</td>
          </tr>
        `;
      });
    },
    error: function(error){
      console.log(error);
  }
});
}








