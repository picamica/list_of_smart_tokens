let visible = 20
let visibleAll = 0;
let globalNetwork = 'bsc';
let globalScanner = 'BscScan';
let globalExchanger = 'PooCoin';
let globalScnLogo = 'bscscan';
let globalExcLogo = 'poocoin';

body = document.body;

body.onload = showTokens(globalNetwork, globalScanner, globalExchanger, globalScnLogo, globalExcLogo);

const bscdiv = document.getElementById('bscdiv');
const ethdiv = document.getElementById('ethdiv');
const maticdiv = document.getElementById('maticdiv');
const ftmdiv = document.getElementById('ftmdiv');
const table = document.getElementById('list-of-tokens');




let clicked = bscdiv;
clicked.style.backgroundColor = '#DCDCDC';

function changeColor() {
  if (event.target.style.backgroundColor == '' && clicked == undefined) {
    event.target.style.backgroundColor = '#DCDCDC';
    clicked = event.target;
  } else {
    clicked.style.backgroundColor = '';
    clicked = event.target;
    clicked.style.backgroundColor = '#DCDCDC';
  }
}

bscdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('bsc', 'BscScan', 'PooCoin', 'bscscan', 'poocoin');

  changeColor();

});

ethdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('eth', 'EtherScan', 'Uniswap', 'etherscan', 'uniswap');

  changeColor();
});

maticdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('matic', 'PolygonScan', 'QuickSwap', 'polygonscan', 'quickswap');

  changeColor();
});

ftmdiv.addEventListener('click', function() {
  visible = 20;
  table.replaceChildren();
  showTokens('ftm', 'FtmScan', 'SpookySwap', 'ftmscan', 'spookyswap');

  changeColor();
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




function showTokens(endpoint, scanner, exchanger, scannerLogo, exchangerLogo) {
  globalNetwork = endpoint;
  globalScanner = scanner;
  globalExchanger = exchanger;
  globalScnLogo = scannerLogo;
  globalExcLogo = exchangerLogo;
  $.ajax({
    type:'GET',
    url: `/data/${endpoint}/${visible}/`,
    success: function(response){
      visibleAll = response.size;
      console.log(response.tokens);
      const data = response.tokens;
      data.forEach(el => {
        table.innerHTML += `
          <tr>
            <td>${el.name}/${el.symbol}</td>
            <td class='overflow'>
              <span class='addresses'>
                <span>${el.address}</span>
              </span>
            </td>
            <td class='links'>
              <a href=${el.Scanner} target='_blank'>
                <img src="/static/images/${scannerLogo}-logo.png">
                <span>
                  ${scanner}
                </span
              </a>
              <a href=${el.Exchange}>
                <img src="/static/images/${exchangerLogo}-logo.png">
                <span>
                  ${exchanger}
                </span>
              </a>
            </td>
            ${getAge(el.age)}
          </tr>
        `;
      });
      copyToClipboard();
    },
    error: function(error){
      console.log(error);
  }
});
}

function showAllTokens(endpoint, scanner, exchanger, scannerLogo, exchangerLogo) {
  $.ajax({
    type:'GET',
    url: `/data/${endpoint}/${visibleAll}/`,
    success: function(response){
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
    error: function(err) {
      console.log(err);
    }
  });
};




let btn = document.getElementById('load-btn');
btn.addEventListener('click', ()=> {
  visible += 20;
  showTokens(globalNetwork, globalScanner, globalExchanger, globalScnLogo, globalExcLogo);
});

let allBtn = document.getElementById('load-all-btn');
allBtn.addEventListener('click', ()=> {
  table.replaceChildren();
  showAllTokens(globalNetwork, globalScanner, globalExchanger, globalScnLogo, globalExcLogo);
})

function copyToClipboard() {
  const addresses = document.querySelectorAll('.addresses');
  addresses.forEach(address => {
    address.addEventListener('click', (event)=> {
      let child = address.children[0];
      console.log(child);
      child.classList.add("opa");

      let range = document.createRange();
      range.selectNode(address);
      window.getSelection().removeAllRanges();
      window.getSelection().addRange(range);
      document.execCommand('copy');
      window.getSelection().removeAllRanges();
      setTimeout(() => {
        child.classList.remove('opa');
      }, 150);
  });
});
}






