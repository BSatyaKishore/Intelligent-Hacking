a = 20
b = 7

print '''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <script  src = "https://cdn.mlkcca.com/v0.6.0/milkcocoa.js"> </script>
</head>


<script>
	var milkcocoa = new MilkCocoa('readjb3dzzdc.mlkcca.com');
	
	window . onload  =  function () {
	  var  output  =  document . getElementById ( 'output' );

	  window . addEventListener ( 'devicemotion' ,  function ( e ) { 
	    gravity  =  e . accelerationIncludingGravity ;

	    output . innerHTML 
	    =  'x direction:' + gravity . x 
	    +  '<br> y direction:' + gravity . y ;
	  }, true );
	};


</script>

<body>

<div class="container">'''


for i in range(a):
	print '''	<div class="btn-group btn-group-justified">'''
	for j in range(b):
		print '''		<a href="#" class="btn btn-primary">'''+str(i)+str(j)+'''</a>'''
	print '''	</div>'''
print '''</div>
</body>
</html>
'''
	
		
