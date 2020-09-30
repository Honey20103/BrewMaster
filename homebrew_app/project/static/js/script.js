$(document).ready(function() {
			
			  // Check for click events on the navbar burger icon
			  $(".navbar-burger").click(function() {
			
			      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
			      $(".navbar-burger").toggleClass("is-active");
			      $(".navbar-menu").toggleClass("is-active");
			});
			});
	    
	    
	    // Function to collapse dashboard accordion
				    $('.collapsible').collapsible();
                    


                    /* NOT WORKING FOR SOME REASON FROM HERE
        // Date picker functions 
            $('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 15, // Creates a dropdown of 15 years to control year,
            today: 'Today',
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false // Close upon selecting a date,
        });

	        // function to fix bug within materialise for date picker
			document.getElementById("matfix").addEventListener("click", function(e) {
				e.stopPropagation();
			});
       */
      
       
