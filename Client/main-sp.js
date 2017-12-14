window.onload = function(){

  var currentMode = 'portrait';
  var output = document.getElementById('output');

  // app_id, API_Key, API_Secretは自分のものに書き換えてください
  var milkcocoa = new MilkCocoa('dogjb65ykxo.mlkcca.com'); 
  var ds = milkcocoa.dataStore('AccData');
  ds.on('send', function (mes) { console.log(mes) })
  window.addEventListener('devicemotion', function(e){
    g = e.accelerationIncludingGravity;
    ds.send({x: g.x, y: g.y, z: g.z});
  },true);
};