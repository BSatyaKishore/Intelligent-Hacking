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
</head>


<body>
	<script src='https://cdn.mlkcca.com/v0.6.0/milkcocoa.js'></script>
	<script>
		var milkcocoa = new MilkCocoa('dogjb65ykxo.mlkcca.com'); 
		var clickData = milkcocoa.dataStore('ClickData');		
		function reply_click(clicked_id) {
			alert(clicked_id);
			clickData.push({clickedId: clicked_id});
		}
	</script>
	<script src="main-sp.js"></script>
	<div  id = "output" > </ div> 


<div class="container">'''


for i in range(a):
	print '''	<div class="btn-group btn-group-justified">'''
	for j in range(b):
		print '''		<a href="#" class="btn btn-primary" id= "'''+str(i)+'_'+str(j)+'''" onClick="reply_click(this.id)">'''+str(i)+str(j)+'''</a>'''
	print '''	</div>'''
print '''</div>
</body>
</html>
'''

a = '''
<script>
	// var milkcocoa = new MilkCocoa('readjb3dzzdc.mlkcca.com');
	var milkcocoa = MilkCocoa.connectWithApiKey('readjb3dzzdc.mlkcca.com', 'PMMHNDOCJLEMPJIG', 'SWbahFCKEKPhTHOVXhTAUGCRifCNaNKjDTFCJIBK');
	console.log("Wprlomg");
	var ds  =  milkcocoa.dataStore('gravity') ;
	ds.on("push")
	ds.send({mode: 'connected'});
	console.log("Wprlomg sent");
	
</script>
'''
	
		
