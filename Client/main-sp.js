window.onload = function(){
  var milkcocoa = new Milkcocoa({
    appId: 'BJBop-Szz',
    accessToken:  'sh/+h9jiB0zJBGp1aJzdDGgF6Tbg0AvO3JERBrRpTLs='
  });
  var currentMode = 'portrait';
  var ds = milkcocoa.dataStore('AccData');
  ds.on('send', function (mes) { console.log(mes) })
  window.addEventListener('devicemotion', function(e){
    g = e.acceleration;
    ds.send({x: g.x, y: g.y, z: g.z});
  },true);
};