<?php
if($_SERVER['REQUEST_METHOD'] == 'POST') {
  $username = $_POST['username'];
  $password = $_POST['password'];

  // Connect to the database
  $conn = mysqli_connect('localhost', 'db_username', 'db_password', 'db_name');
  if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
  }

  // Verify the password with the database
  $query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
  $result = mysqli_query($conn, $query);
  if (mysqli_num_rows($result) > 0) {
    // Redirect to home page if password is correct
    header('Location: http://localhost/home.html');
  } else {
    // Display error message if password is incorrect
    echo "Error: Incorrect username or password";
  }

  mysqli_close($conn);
}
?>
