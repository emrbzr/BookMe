<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Select the month | Room Reservation System</title>

    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="bootstrap/css/font-awesome.min.css">

    <link rel="stylesheet" href="CustomCss/Content.css">

    <!--[if lt IE 9]-->
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.2/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <!--[endif]-->
  </head>
  <body>
    <!-- Main Page Content -->
    <div class="container-fluid">

      <!-- Page Heading -->
      <div class="page-header text-center">
        <h1>Month Selection</h1>
      </div>
      <div id="textcolorcorrector" class="row-fluid">
        <div class="text-center">.</div>
      </div>
      <br>

      <!-- Table Type View -->
      <div class="row-fluid">
        <div class="panel panel-default">
          <div class="panel-body">
            <div id="month" class="row-fluid BottomPadder text-center">
              <div class="col-md-2 divider">January</div>
              <div class="col-md-2 divider">February</div>
              <div class="col-md-2 divider">March</div>
              <div class="col-md-2 divider">April</div>
              <div class="col-md-2 divider">May</div>
              <div class="col-md-2">June</div>
            </div>
            <div id="month" class="row-fluid">
              <div class="col-md-12 text-center">Please Select the Month!</div>
            </div>
            <div id="month" class="row-fluid TopPadder text-center">
              <div class="col-md-2 divider">July</div>
              <div class="col-md-2 divider">August</div>
              <div class="col-md-2 divider">September</div>
              <div class="col-md-2 divider">October</div>
              <div class="col-md-2 divider">November</div>
              <div class="col-md-2">December</div>
            </div>
          </div>
        </div>
      </div>

      <div class="row-fluid">
        <div class="panel panel-default">
          <div id="linksending" class="panel-body">
            <div style="border-right: 1px solid #ddd;" class="col-md-6 text-center">
              <a href="index.php">My Profile</a>
            </div>
            <div class="col-md-6 text-center">
              <a href="logout.php">Logout : Emir</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- For Fast Loading Of Scripts -->
    <script src="JQuery/js/jquery.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <script type="text/javascript">
      $(function(){
        $("#month .col-md-2").mouseenter(function(){
          $(this).css("background", "#93DC69");
          $(this).css("color", "white");
          $(this).css("cursor", "pointer");
        });
        $("#month .col-md-2").mouseleave(function(){
          $(this).css("background", "#FFFFFF");
          $(this).css("color", "#333333");
        });
      });

      $("#month .col-md-2").click(function(){
        if($(this).html() == "January")
        {
          window.location.href = "january.php";
        }
        if($(this).html() == "February")
        {
          window.location.href = "february.php";
        }
        if($(this).html() == "March")
        {
          window.location.href = "march.php";
        }
        if($(this).html() == "April")
        {
          window.location.href = "april.php";
        }
        if($(this).html() == "May")
        {
          window.location.href = "may.php";
        }
        if($(this).html() == "June")
        {
          window.location.href = "june.php";
        }
        if($(this).html() == "July")
        {
          window.location.href = "july.php";
        }
        if($(this).html() == "August")
        {
          window.location.href = "august.php";
        }
        if($(this).html() == "September")
        {
          window.location.href = "september.php";
        }
        if($(this).html() == "October")
        {
          window.location.href = "october.php";
        }
        if($(this).html() == "November")
        {
          window.location.href = "november.php";
        }
        if($(this).html() == "December")
        {
          window.location.href = "december.php";
        }
      });
    </script>
  </body>
</html>
