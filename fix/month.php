<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Select the month | Room Reservation System</title>

    <link rel="stylesheet" href="../static/styles/bootstrap.min.css">
    <link rel="stylesheet" href="../static/styles/font-awesome.min.css">
    <link rel="stylesheet" href="../static/styles/Content.css">

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
      <div class="row-fluid">
        <div class="panel panel-default">
          <div id="linksending" class="panel-body">
            <div style="border-right: 1px solid #ddd;" class="col-md-6 text-center">
              <a href="{{ url_for('dashboard',user=session['user']) }}">My Profile</a>
            </div>
            <div class="col-md-6 text-center">
              <a href="/logout">Logout : Emir</a>
            </div>
          </div>
        </div>
      </div>
      <br>

      <!-- Table Type View -->
      <div class="row-fluid">
        <div class="panel panel-default">
          <div class="panel-body">
            <div id="month" class="row-fluid BottomPadder text-center">
              <a style="text-decoration:none;" class="col-md-2 divider" href="/january"><div>January</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/february"><div>February</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/march"><div>March</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/april"><div>April</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/may"> <div>May</div></a>
               <a style="text-decoration:none;" class="col-md-2" href="/january"><div>June</div></a>
            </div>
            <div id="month" class="row-fluid">
              <div class="col-md-12 text-center">Please Select the Month!</div>
            </div>
            <div id="month" class="row-fluid TopPadder text-center">
              <a style="text-decoration:none;" class="col-md-2 divider" href="/july"><div>July</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/august"><div>August</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/september"><div>September</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/october"><div>October</div></a>
              <a style="text-decoration:none;" class="col-md-2 divider" href="/november"><div>November</div></a>
              <a style="text-decoration:none;" class="col-md-2" href="/december"><div>December</div></a>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- For Fast Loading Of Scripts -->
    <script src="../static/javascript/jquery.min.js"></script>
    <script src="../static/javascrit/bootstrap.min.js"></script>
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
    </script>
  </body>
</html>
