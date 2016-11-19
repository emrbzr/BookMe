<!DOCTYPE html>
<!--SOEN 343 - Front end made with PHP & HTML/CSS & BOOTSTRAP & JQUERY & JAVASCRIPT-->
<!-- All the functions are made by me, Emir, none of the php or js built in functions are used!-->
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Room Reservation System</title>

    <link rel="stylesheet" href="../static/styles/bootstrap.min.css">
    <link rel="stylesheet" href="../static/styles/font-awesome.min.css">

    <link rel="stylesheet" href="../static/styles/Content.css">

    <!--[for IE9 support]-->
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.2/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <!--[endif]-->
  </head>
  <body>
    <!-- main page div -->
    <div class="container-fluid">

      <!-- heading div in h1, formatted in the css file -->
      <div class="page-header text-center">
        <h1>My Profile</h1>
      </div>
      <div id="textcolorcorrector" class="row-fluid">
        <div class="text-center"><h3>{{user}}</h3></div>
        <br>
        <div class="text-center">My Reservations:</div>
        <br>

        <table class="demo" align="center">

          <thead>
          <tr>
            <th>Time</th>
            <th>Date</th>
            <th>Room</th>
            <th>Modify</th>
            <th>Cancel</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>00:00</td>
            <td>1/1/1111</td>
            <td>Room 1</td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Modify Reservation</div></a>
                  </div>
                </div>
              </div></td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Cancel Reservation</div></a>
                  </div>
                </div>
              </div></td>
          </tr>
          <tr>
            <td>00:00</td>
            <td>1/1/1111</td>
            <td>Room 1</td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Modify Reservation</div></a>
                  </div>
                </div>
              </div></td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Cancel Reservation</div></a>
                  </div>
                </div>
              </div></td>
          </tr>
          <tr>
            <td>00:00</td>
            <td>1/1/1111</td>
            <td>Room 2</td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Modify Reservation</div></a>
                  </div>
                </div>
              </div></td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Cancel Reservation</div></a>
                  </div>
                </div>
              </div></td>
          </tr>
          <tr>
            <td>00:00</td>
            <td>1/1/1111</td>
            <td>Room 3</td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Modify Reservation</div></a>
                  </div>
                </div>
              </div></td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Cancel Reservation</div></a>
                  </div>
                </div>
              </div></td>
          </tr>
          <tr>
            <td>00:00</td>
            <td>1/1/1111</td>
            <td>Room 5</td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Modify Reservation</div></a>
                  </div>
                </div>
              </div></td>
            <td><div class="panel panel-default">
                <div class="panel-body">
                  <div id="month" class="BottomPadder text-center">
                    <a class="col-md-12" style="text-decoration:none;" href="add.php"><div>Cancel Reservation</div></a>
                  </div>
                </div>
              </div></td>
          </tr>
          <tbody>
        </table>
      </div>
      <br>
      <br>
      <!-- table type for the button formatted in css file -->
      <div class="col-md-offset-5 col-md-2">
        <div class="row-fluid">
          <div class="panel panel-default">
            <div class="panel-body">
              <div id="month" class="BottomPadder text-center">
                <a class="col-md-12" style="text-decoration:none;" href="{{ url_for('month')}}"><div>Make A New Reservation</div></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- For Fast Loading Of Scripts -->
    <script src="../static/javascript/jquery.min.js"></script>
    <script src="../static/javascript/bootstrap.min.js"></script>
    <!-- Javascript function for the effect and the clicking -->
    <script type="text/javascript">
      $(function(){
        $("#month .col-md-12").mouseenter(function(){
          $(this).css("background", "#93DC69");
          $(this).css("color", "white");
          $(this).css("cursor", "pointer");
        });
        $("#month .col-md-12").mouseleave(function(){
          $(this).css("background", "#FFFFFF");
          $(this).css("color", "#333333");
        });
      });
      <!-- hiding the page adress from the bottom bar, cannot right click and copy the adress-->
     // !$(".col-md-12").click(function(){
        
      //});
    </script>
    <!--[endif]-->
  </body>
</html>