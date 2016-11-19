<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>January Reservation</title>

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
        <h1>Reservation for January</h1>
      </div>
      <div id="textcolorcorrector" class="row-fluid">
        <div class="text-center">Please Click on the Day</div>
      </div>
      <br>

      <!-- Table Type View -->
      <div class="row-fluid">
        <div id="month" class="row-fluid BottomPadder text-center">
          <div class="topleft col-xs-offset-1 col-sm-offset-1 col-md-offset-1 col-lg-offset-1 col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">1</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">2</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">3</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">4</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">5</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">6</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">7</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">8</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">9</div>
          <div class="topright col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">10</div>

          <div class="col-xs-offset-1 col-sm-offset-1 col-md-offset-1 col-lg-offset-1 col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">11</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">12</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">13</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">14</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">15</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">16</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">17</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">18</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">19</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">20</div>

          <div class="bottomleft col-xs-offset-1 col-sm-offset-1 col-md-offset-1 col-lg-offset-1 col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">21</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">22</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">23</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">24</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">25</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">26</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">27</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">28</div>
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">29</div>
          <div class="bottomright col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">30</div>
          <div class="bottomleft col-xs-offset-1 col-sm-offset-1 col-md-offset-1 col-lg-offset-1 col-xs-1 col-sm-1 col-md-1 col-lg-1 divider">31</div>
        </div>
      </div>

      <br><br><br><br><br>

      <div class="row-fluid">
        <div class="panel panel-default col-xs-offset-1 col-sm-offset-1 col-md-offset-1 col-lg-offset-1 col-xs-10 col-sm-10 col-md-10 col-lg-10">
          <div id="linksending" class="panel-body">
            <div style="border-right: 1px solid #ddd;" class="col-xs-6 col-sm-6 col-md-6 col-lg-6 text-center">
              <a href="month.php">Go Back</a>
            </div>
            <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6 text-center">
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
        $("#month .divider").mouseenter(function(){
          $(this).css("background", "#93DC69");
          $(this).css("color", "white");
          $(this).css("cursor", "pointer");
        });
        $("#month .divider").mouseleave(function(){
          $(this).css("background", "#FFFFFF");
          $(this).css("color", "#333333");
        });
      });

      $("#month .divider").click(function(){
        if($(this).html() == "1" || "2" || "3" || "4" || "5" || "6" || "7"|| "8" || "9"|| "10" || "11" || "12" || "13" || "14" || "15" || "16" || "17" || "18" || "19" || "20" || "21" || "22" || "23" || "24" || "25" || "26" || "27" || "28" || "29" || "30" || "31")
        {
          window.location.href = "add.php";
        }
      });
    </script>
  </body>
</html>