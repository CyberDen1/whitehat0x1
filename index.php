<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8" />
  <title></title>
 </head>
 <body>
  <p>File Inclusion</p>
  
<?php
	ini_set('display_errors', 'Off');

	$file = $_GET["file"];
	include $file;
?>

 </body>
</html>