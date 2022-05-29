$(document).ready(function() {
    console.log( "NitishPravinTalekar");
    $("#experiance-title").css('opacity', '1');
});
$(document).on('click', '#exp-toggle', function () {
  $("#exp-panel").slideToggle();
  $("#exp-panel1").slideToggle();
  $("#exp-toggle").toggleClass("fa-chevron-down");
  $("#exp-toggle").toggleClass("fa-chevron-up");
});
$(document).on('click', '#expedu-toggle', function () {
    $("#exp-slide").toggle('slide');
    $("#edu-slide").toggle('slide');
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

$(document).on('click', '.artwork', function () {
  // console.log("HELLO");
  $("#artwork-name").text($(this).children(".art-name").text() + " - " + $(this).children(".art-date").text());
  $("#artwork-img").attr("src",$(this).children(".art-src").text());
  $("#artworkmodal").modal("show");
});

$(document).on('click', '.project', function () {
  // console.log("HELLO");
  $("#project-git").show();
  $("#project-link").show()
  $("#project-name").text($(this).children().children().children(".proj-name").text());
  $("#project-topic").text($(this).children().children().children(".proj-topic").text());
  $("#project-timeline").text($(this).children().children(".proj-timeline").text());
  $("#project-desc").text($(this).children().children(".proj-desc").text());
  $("#project-lang").text($(this).children().children().children(".proj-lang").text());
  $("#project-git").attr("href",$(this).children().children(".proj-git").text());
  $("#project-link").attr("href",$(this).children().children(".proj-link").text());
  if($(this).children().children(".proj-git").text() == ""){
    $("#project-git").hide();
  }
  if($(this).children().children(".proj-link").text() == ""){
    $("#project-link").hide();
  }
  $("#projectmodal").modal("show");
});