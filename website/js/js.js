$(document).ready(function () {

    function registerClickHandler() {
        // Implement the click handler here for button of class 'remove'
        $('.trash').click(function() {
          $(this).parent().parent().parent().parent().remove();
        });
      }
      
      registerClickHandler();});