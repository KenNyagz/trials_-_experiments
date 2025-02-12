<?php
$servername = "localhost";
$username = "ken";
$password = "@Kennyaga";
$db = "php_prac";

$conn = new mysqli($servername, $username, $password, $db);
if ($conn) { echo "Very nice \n";}
//$db = $conn->query("CREATE DATABASE php_prac");
/*$db = $conn->query("CREATE TABLE Guests (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    firstname VARCHAR(30) NOT NULL,
                    lastname VARCHAR(30) NOT NULL,
                    email VARCHAR(50),
                    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                    )"); */
/*$db = $conn->query("INSERT INTO Guests(firstname, lastname, email)
                    VALUES ('Fazul', 'Obi', 'fazobi@yahoo.com'),
                           ('Fatima', 'Mene', 'fatimen@yahoo.com')
                    ") */
echo $conn->insert_id;
echo "\n";
$prep = $conn->prepare("INSERT INTO Guests (firstname, lastname, email) VALUES (?, ?, ?)");
$prep->bind_param("sss", $firstname, $lastname, $email);

$firstname = 'Kene';
$lastname = 'Dene';
$email = 'kenedene@email.com';

//$prep->execute();

$result = $conn->query("SELECT id, email FROM  Guests LIMIT 2 OFFSET 5");
$conn->query("UPDATE Guests SET firstname='My', lastname='Omy', email='myOmyy@me.com' WHERE id IN (11, 12)");
if ($result->num_rows > 0) {
    echo "<table border='1'><tr><th>ID</th><th>Email</th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>". $row["id"] . "</td><td>" . $row["email"] . "</td></tr>";
    };
    echo "</table>";
}
echo "<input type='text' onkeyup=showText() id='inp'>
      <p id='out'></p>
        <script>
            function showText() {
                let inputValue = document.getElementById('inp').value;
                document.getElementById('out').innerText = inputValue;
            }
        </script>
      </form>
"
?>      