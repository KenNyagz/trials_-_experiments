<?php
//php on the browser side
$cookie_name = "Ken";
$cookie_value = "10";
setcookie($cookie_name, $cookie_value, time() - 3600, "/");
session_start();
?>

<!DOCTYPE html>

<html>
<head>

</head>
<body>
    <h1>Hi!</h1>
    <?php
     echo "Hello"."<br>";
     echo sizeof($_SESSION) . "<br>";
     $_SESSION['favcolor'] = "Yellow";
     //print_r($_SESSION);
     //print_r(filter_list());
$number = 0;
if (filter_var($number, FILTER_VALIDATE_INT) === false) {
    echo "Invalid number!";
} else {
    echo "Valid number!";
}

    ?>
</body>
</html>
