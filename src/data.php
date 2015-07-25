<?php
function connect_db() {
  $conn = mysql_connect('localhost', 'root', 'edison123');
  if (!$conn) {
    die("Connection failed: " . $conn->connect_error);
  }
  mysql_select_db('edison', $conn);
  return $conn;
}

function get_nodes() {
  $query = "SELECT * FROM nodes";
  $res = mysql_query($query);
  $res_array = array();
  while ($row = mysql_fetch_array($res)) {
    $tmp_array = array("id" => $row[0],
		       "lat" => $row[1],
		       "lon" => $row[2],
		       "name" => $row[3]);
    array_push($res_array, $tmp_array);
  }

  return $res_array;
}

function get_last_data($nodes, $type_mea) {
  /* The user must specify the type of measurement that wants to query */
  $meas = array();
  foreach ($nodes as $node) {
    $node_id = $node['id'];
    $query = "SELECT * FROM meas WHERE node_id =".
      $node_id.
      " and type_mea = ".
      $type_mea.
      " ORDER by id DESC LIMIT 1";
    $res = mysql_query($query);
    $row = mysql_fetch_array($res);
    $tmp_array = array("id" => $row[0],
		       "node_id" => $row[1],
		       "date" => $row[2],
		       "mea" => $row[3],
		       "type_mea" => $row[4]
		       );
    array_push($meas, $tmp_array);
  }
  return $meas;
}

if (!isset($_GET['nodes']) && !isset($_GET['data'])) {
    echo "Action not specified";
}

$con = connect_db();

if (isset($_GET['nodes'])) {
    echo json_encode(get_nodes());
}
else if (isset($_GET['data'])) {
  $type_data = $_GET['data'];
  $nodes = get_nodes();
  $data = get_last_data($nodes, $type_data);
  echo json_encode($data);
}

?>
