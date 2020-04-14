<?php
    $name = $POST['name'];
    $user_email = $POST['email'];
    $phone = $POST['phone number'];
    $message = $POST['message'];
    $email_from = 'mohittasks@gmail.com'
    $subj='New form Submission';
    $body= "User name: $name\n"
            "User email: $user_email\n"
            "User message:\n $message";
    $to = "moh.nov16@gmail.com"
    $headers = "From: $email_from \r\n";
    $headers .= "Reply-To: $user_email \r\n";
    mail($to, $subj, $body, $headers);
    header("Location: HTML_website.html");
?>