
var nav = $(".nav.main-nav li")
nav.each(function () {
        $(this).removeClass("active")
})
nav.each(function () {
	
  //  $(this).click(function () {
	cururl = location.href.split("/")[3]
	pos = $(this).find('a')[0].href.split("/")
	darken = pos[3]
	console.log(pos)
	if (darken === '' || darken === undefined)
	{
		darken = "urlsaver"
	}
	if (darken === cururl){
		$(this).addClass("active")

		if (pos[4] !== ""){
			$(this).removeClass("active")
			$(this).css({backgroundColor: "blue !important"})
		}
	}

        // nav.each(function () {
        //     $(this).removeClass("active")
        // })

        // $(this).addClass("active")
        // //console.log($(this))
 //   })
})
