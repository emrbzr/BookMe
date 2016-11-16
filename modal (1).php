<div id="modal1" class="modal fade" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h2 class="modal-title text-center"><span style="color: #93DC69;">Room 1</span></h2>
      </div>
      <div class="modal-body">
        <div id="rider" class="container-fluid">
          <div class="row-fluid">
            <h2>
              <div class="defaultCountdown col-xs-offset-6 col-sm-offset-6 col-md-offset-6 col-lg-offset-6 col-xs-6 col-sm-6 col-md-6 col-lg-6 text-center divider-countDown">
              </div>
            </h2>
          </div>
          <br><br><br>
          <!-- <div class="row-fluid">&nbsp;</div> not used for now-->
          <div class="row-fluid">
            <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 text-center">
              <p style="color: #333; font-weight: bold;">Please select the box next to the available time slots.</p><br>
              <p style="color: #333; font-weight: bold;">If the room is not available, you can click on X to be on the waiting list.</p><br>
              <p style="color: #333; font-weight: bold;">You can only reserve the room for 2 consecutive hours.</p><br>
              <p style="color: #333; font-weight: bold;"><font color="red">Warning: You have 2 minutes to complete the reservation</font> .</p>
              <br>
              <p style="color: #333; font-weight: bold;">Please enter a short description of your reservation.</p>
              <input type="text" id="myText" value="">

            </div>
            <br>
          </div>
          <?php
            for ($b = 0; $b < 10; $b++) {
          ?>
              <!-- Looped for now, i'll breake the loop make it static for each so we can dynamically import python -->
              <div class="row-fluid">
                <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6 divider-spec text-center">
                  <p style="color: #333; font-weight: bold;">Times 0:0</p>
                </div>
                <div style="transition: background 1s, color 0.75s;" class="Greenies col-xs-6 col-sm-6 col-md-6 col-lg-6 divider-spec text-center">
                  <p style="color: #333; font-weight: bold; float: left;">Availability</p><span class="text-right" style="float: right; font-weight: bolder; color: red; cursor: pointer;">X</span>
                </div>
              </div>
          <?php
            }
          ?>
        </div>
        <br><br>
        <div class="row">
          <div class="col-md-2 col-md-offset-5">
            <button type="button" class="killer btn btn-default" data-dismiss="modal">Reserve!</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
