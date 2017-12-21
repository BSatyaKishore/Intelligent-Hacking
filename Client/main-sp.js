window.onload = function(){
  var milkcocoa = new Milkcocoa({
    appId: 'BJBop-Szz',
    apiKey: 'QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU' //accessToken:  'sh/+h9jiB0zJBGp1aJzdDGgF6Tbg0AvO3JERBrRpTLs='
  });
  var currentMode = 'portrait';
  var ds = milkcocoa.dataStore('AccData');
  //ds.on('send', function (mes) { console.log(mes) })
  //ds.push('satya');
  window.addEventListener('devicemotion', _.throttle(function(e){
    g = e.acceleration;
    ds.send({x: g.x, y: g.y, z: g.z});
  },50), true);
};