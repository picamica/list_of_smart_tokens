let visible = 20
let globalNetwork = '';
let globalScanner = '';
let globalExchanger = '';

body = document.body;

body.onload = showTokens('bsc', 'BSCscan', 'POOCOIN');

const bscdiv = document.getElementById('bscdiv');
const ethdiv = document.getElementById('ethdiv');
const maticdiv = document.getElementById('maticdiv');
const ftmdiv = document.getElementById('ftmdiv');

const table = document.getElementById('list-of-tokens');


bscdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('bsc', 'BSCscan', 'POOCOIN');
});

ethdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('eth', 'EtherScan', 'Uniswap');
});

maticdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('matic', 'PolygonScan', 'QuickSwap');
});

ftmdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('ftm', 'FtmScan', 'SpookySwap');
});



function getAge(age) {
  if (age >= 3600) {
    return `<td>${~~(age/3600)}h</td>`
  } else if (age >= 60) {
    return `<td>${~~(age/60)}m</td>`
  } else {
    return `<td>${age}s</td>`
  }
}




function showTokens(endpoint, scanner, exchanger) {
  globalNetwork = endpoint;
  globalScanner = scanner;
  globalExchanger = exchanger;
  $.ajax({
    type:'GET',
    url: `/data/${endpoint}/${visible}/`,
    success: function(response){
      console.log(response.tokens);
      const data = response.tokens;
      data.forEach(el => {
        table.innerHTML += `
          <tr>
            <td>${el.name}/${el.symbol}</td>
            <td>${el.address}</td>
            <td>
              <a href=${el.Scanner}>${scanner}</a>
              <a href=${el.Exchange}>${exchanger}</a>
            </td>
            ${getAge(el.age)}
          </tr>
        `;
      });
    },
    error: function(error){
      console.log(error);
  }
});
}


let btn = document.getElementById('load-btn');
btn.addEventListener('click', ()=> {
  visible += 20;
  showTokens(globalNetwork, globalScanner, globalExchanger);
});







