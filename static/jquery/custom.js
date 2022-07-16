$(document).ready(function() {
    console.log( "NitishPravinTalekar");
    $("#experiance-title").css('opacity', '1');
    $("#experiance-title").removeClass("display-6");
    $("#experiance-title").addClass("display-4");
    $("#prof-title").css('font-weight', 'bold');
    $("#prof-title").css('opacity', '1');
});
$(document).on('click', '#prof-title', function () {
  $("#exp-panel").fadeOut("fast",function(){
      $("#exp-panel1").fadeIn("fast")
  });
  $("#prof-title").css('font-weight', 'bold');
  $("#curr-title").css('font-weight', 'normal');
  $("#prof-title").css('opacity', '1');
  $("#curr-title").css('opacity', '0.3');
  $("#exp-desc-word").text("Professional");
});
$(document).on('click', '#curr-title', function () {
  $("#exp-panel1").fadeOut("fast",function(){
      $("#exp-panel").fadeIn("fast")
  });
  $("#curr-title").css('font-weight', 'bold');
  $("#prof-title").css('font-weight', 'normal');
  $("#curr-title").css('opacity', '1');
  $("#prof-title").css('opacity', '0.3');
  $("#exp-desc-word").text("Volunteering");
});
$(document).on('click', '#education-title', function () {
  $("#exp-slide").fadeOut("fast",function(){
    $("#skill-slide").fadeOut("fast",function(){
      $("#edu-slide").fadeIn("fast")
    })
  });
  $("#exp-desc").fadeOut("fast",function(){
    $("#skill-desc").fadeOut("fast",function(){
      $("#edu-desc").fadeIn("fast")
    })
  });
  $("#education-title").css('opacity', '1');
  $("#experiance-title").css('opacity', '0.3');
  $("#skills-title").css('opacity', '0.3');
  $(".display-4.info-hover").addClass("display-6");
  $(".display-4.info-hover").removeClass("display-4");
  $("#education-title").removeClass("display-6");
  $("#education-title").addClass("display-4");
});
$(document).on('click', '#experiance-title', function () {
  $("#edu-slide").fadeOut("fast",function(){
    $("#skill-slide").fadeOut("fast",function(){
      $("#exp-slide").fadeIn("fast");
    })
  });
  $("#edu-desc").fadeOut("fast",function(){
    $("#skill-desc").fadeOut("fast",function(){
      $("#exp-desc").fadeIn("fast");
    })
  });
  $("#education-title").css('opacity', '0.3');
  $("#experiance-title").css('opacity', '1');
  $("#skills-title").css('opacity', '0.3');
  $(".display-4.info-hover").addClass("display-6");
  $(".display-4.info-hover").removeClass("display-4");
  $("#experiance-title").removeClass("display-6");
  $("#experiance-title").addClass("display-4");
});
$(document).on('click', '#skills-title', function () {
  $("#exp-slide").fadeOut("fast",function(){
    $("#edu-slide").fadeOut("fast",function(){
      $("#skill-slide").fadeIn("fast");
    })
  });
  $("#exp-desc").fadeOut("fast",function(){
    $("#edu-desc").fadeOut("fast",function(){
      $("#skill-desc").fadeIn("fast");
    })
  });
  $("#education-title").css('opacity', '0.3');
  $("#experiance-title").css('opacity', '0.3');
  $("#skills-title").css('opacity', '1');
  $(".display-4.info-hover").addClass("display-6");
  $(".display-4.info-hover").removeClass("display-4");
  $("#skills-title").removeClass("display-6");
  $("#skills-title").addClass("display-4");
});

$(document).on('click', '.carousel-next', function () {
  var index = $(this).parent().children(".carousel-index").text();
  index2 = (parseInt(index)+1)%2;
  var id = $(this).parent().children(".carousel-name").text();
  if($("#"+id+"_"+index2).length){
    $("#"+id+"_"+index).fadeOut("fast",function(){
      $("#"+id+"_"+index2).fadeIn("fast")
    });
    $(this).parent().children(".carousel-index").text(index2)
  }
  else{
    return
  }
});

// $(document).on('click', '.artwork', function () {
//   // console.log("HELLO");
//   $("#artwork-name").text($(this).children(".art-name").text() + " - " + $(this).children(".art-date").text());
//   $("#artwork-img").attr("src",$(this).children(".art-src").text());
//   $("#artworkmodal").modal("show");
// });
