<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Make a New Reservation</title>

    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="bootstrap/css/font-awesome.min.css">
    <link rel="stylesheet" href="CustomCss/Content.css">

  </head>
  <body>
    <!-- Main Page Content -->
    <div class="container-fluid">

      <!-- Page Heading -->
      <div class="page-header text-center">
        <h1>Room Selection</h1>
      </div>
      <div id="textcolorcorrector" class="row-fluid">
        <div class="text-center">Please Select the Room You Wish To Reserve</div>
          <br>
          <div class="text-center">Warning: After you select the room, you have 2 minutes to complete your reservation.</div>
      </div>
      <br>

      <!-- Table Type View -->
      <div class="row-fluid">
        <div class="panel panel-default">
          <div id="month" class="panel-body">
              <div id="relax" class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">&nbsp;</div>
              <div class="clickable col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center" data-toggle="modal" data-target="#modal1">Room 1</div>
              <div class="clickable col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center" data-toggle="modal" data-target="#modal2">Room 2</div>
              <div class="clickable col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center" data-toggle="modal" data-target="#modal3">Room 3</div>
              <div class="clickable col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center" data-toggle="modal" data-target="#modal4">Room 4</div>
              <div class="clickable col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center" data-toggle="modal" data-target="#modal5">Room 5</div>


              <!-- NOTE : WE WILL ONLY MAKE ROOM AVAILABILITY COLUMNS DYNAMIC. TIME COLUMN CAN BE HARD CODED. AND NO NEED TO GET THE VALUE
              BECAUSE WE WILL GET THE TIME VALUE IN THE MODAL PAGE(AKA POPUP) YOU CAN DELETE THIS COMMENT AFTER YOUR READ IT HYJAZ LOL-->

              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 09.00</div>
                  <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
                  <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
                  <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
                  <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
                  <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 10:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 11:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 12:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 13:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 14:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 15:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 16:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 17:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 18:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 19:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 20:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Time: 21:00</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room1 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room2 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room3 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 divider text-center">Room4 Availability</div>
              <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2 text-center">Room5 Availability</div>
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

    <?php
      include 'modal (2).php';
      include 'modal (1).php';
      include 'modal (3).php';
      include 'modal (4).php';
      include 'modal (5).php';
    ?>

    <!-- For Fast Loading Of Scripts -->
    <script src="JQuery/js/jquery.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <!--[if lt IE 9]-->
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.2/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <!--[endif]-->

    <script type="text/javascript">
      var clicking = false;
      $(function(){
        $("#rider .Greenies").mouseenter(function(){
          if(!$(this).hasClass("clicked"))
          {
            $(this).css("background", "#93DC69");
            $(this).css("color", "white");
            $(this).css("cursor", "pointer");
          }
        });


          $("#rider .Greenies").mouseleave(function(){
            if(!$(this).hasClass("clicked"))
            {
              $(this).css("background", "#FFFFFF");
              $(this).css("color", "#333333");
            }
          });
      });

      $("#rider .Greenies p").click(function(){
        if(!$(this).parent().hasClass("clicked"))
        {
          $(this).parent().addClass("clicked");
          $(this).parent().css("background", "#93DC69");
        }
        else
        {
          $(this).parent().removeClass("clicked");
          $(this).parent().css("background", "#FFFFFF");
        }
      });

      $("span").click(function() {
        if(!$(this).parent().hasClass("clicked"))
        {
          $(this).parent().addClass("clicked");
          $(this).parent().css("background", "#FF4242");
        }
        else
        {
          $(this).parent().removeClass("clicked");
          $(this).parent().css("background", "#FFFFFF");
        }
      });

      $(function(){
        $("#month .clickable").mouseenter(function(){
          $(this).css("background", "#93DC69");
          $(this).css("color", "white");
          $(this).css("cursor", "pointer");
        });
        $("#month .clickable").mouseleave(function(){
          $(this).css("background", "#FFFFFF");
          $(this).css("color", "#333333");
        });
      });

      $(".killer").click(function(){
        alert("You Are Successful!!");
      });

      var s, m, i;
      var interval

      $("#month .clickable").on("click", function(){
        $("span").parent().css("background", "#FFFFFF");
        $("p").parent().css("background", "#FFFFFF");
        clearInterval(interval);
        s = 60;
        m = 1;

        $(".defaultCountdown").html("02 : 00");
        interval = setInterval(function(){
          if(s == 0)
          {
            m--;
            s= 59;
          }
          else
          {
            s--;
          }
          if(m == -1)
          {
            clearInterval(interval);
          }
          if(s < 10 && m != -1)
          {
            $(".defaultCountdown").html("0" + m + " : 0" + s);
          }
          else if(m != -1)
          {
            $(".defaultCountdown").html("0" + m + " : " + s);
          }
          if(m == 0 && s == 0 && $(".modal").hasClass("in"))
          {
            $(".defaultCountdown").html("00 : 00");
            alert("You Ran Out Of Time!");
            $(".close").trigger('click');
          }
        }, 1000);
      });

      $(function(){
        $("#relax").mouseenter(function(){
          $(this).css("background", "#FFFFFF");
          $(this).css("color", "#333333");
        });

        $("#relax").mouseleave(function(){
          $(this).css("background", "#FFFFFF");
          $(this).css("color", "#333333");
        });
      });

      $(document).ready(function() {
        $("#month .col-md-2").css("border", "1px solid #ddd");
      });
    </script>
  </body>
</html>
