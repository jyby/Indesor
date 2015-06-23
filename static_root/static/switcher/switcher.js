// Copyright 2015 Christina Arasmo Beymer.

$(function() {
    function e() {
        $.removeCookie("b-different-salmon-blue"), $.removeCookie("b-different-retro"), $.removeCookie("b-different-white"), $.removeCookie("b-different-green-gray"), $.removeCookie("b-different-navy"), $.removeCookie("b-different-blue-gray"), $.removeCookie("b-different-stone"), $.removeCookie("b-different-navy-taupe"), $.removeCookie("b-different-red-black")
    }

    function t() {
        $("#base").removeClass("active")
    }

    function s(e) {
        var t = document.createElement("link");
        t.setAttribute("rel", "stylesheet"), t.setAttribute("type", "text/css"), t.setAttribute("class", "clr"), t.setAttribute("href", "assets/css/" + e + ".min.css"), document.getElementsByTagName("head")[0].appendChild(t)
    }
    $(document).height() > $(window).height() && $("body").addClass("body-scroll-fix"), $("<hr><h3><span>Tall Image and Logo Image</span></h3><p>These pages using an <code>img</code> for the logo do not change with the theme colors intentionally.</p>").appendTo("#switcher-wrapper section:last-child"), $(".theme-switcher-toggle, #switcher-wrapper .close").click(function(e) {
        $("html").toggleClass("open-switcher"), $(".theme-switcher-toggle").toggleClass("active-slide-btn"), $(".theme-switcher-toggle i").is(".fa-spin") ? $(".theme-switcher-toggle i").removeClass("fa-spin") : $(".theme-switcher-toggle i").addClass("fa-spin"), e.preventDefault()
    }), $(".colors a").click(function(t) {
        $(this).siblings().hasClass("active") ? ($(this).siblings().removeClass("active"), $(this).addClass("active")) : $(this).addClass("active"), color = this.id.replace("#", ""), e(), $(".clr").remove(), $(".cload").remove(), $.cookie(color, 1, {
            expires: 7
        });
        var s = document.createElement("link");
        s.setAttribute("rel", "stylesheet"), s.setAttribute("type", "text/css"), s.setAttribute("class", "clr"), s.setAttribute("href", "assets/css/" + color + ".min.css"), document.getElementsByTagName("head")[0].appendChild(s), $("html").toggleClass("open-switcher"), $(".theme-switcher-toggle i").toggleClass("fa-spin"), $(".theme-switcher-toggle").toggleClass("active-slide-btn"), t.preventDefault()
    }), $(window).load(function() {
        $.cookie("b-different-retro") ? (s("b-different-retro"), t(), $("#b-different-retro").addClass("active")) : $.cookie("b-different-salmon-blue") ? (s("b-different-salmon-blue"), t(), $("#b-different-salmon-blue").addClass("active")) : $.cookie("b-different-green-gray") ? (s("b-different-green-gray"), t(), $("#b-different-green-gray").addClass("active")) : $.cookie("b-different-navy") ? (s("b-different-navy"), t(), $("#b-different-navy").addClass("active")) : $.cookie("b-different-blue-gray") ? (s("b-different-blue-gray"), t(), $("#b-different-blue-gray").addClass("active")) : $.cookie("b-different-white") ? (s("b-different-white"), t(), $("#b-different-white").addClass("active")) : $.cookie("b-different-stone") ? (s("b-different-stone"), t(), $("#b-different-stone").addClass("active")) : $.cookie("b-different-red-black") ? (s("b-different-red-black"), t(), $("#b-different-red-black").addClass("active")) : $.cookie("b-different-navy-taupe") && (s("b-different-navy-taupe"), t(), $("#b-different-gold-cobalt").addClass("active"))
    }), $(".color-reset, #base").click(function(t) {
        e(), $(".clr").remove(), $(".colors a").removeClass("active"), $("#base").addClass("active"), t.preventDefault()
    }), window.location.href.indexOf("image-logo") > -1 && e(), window.location.href.indexOf("tall-logo") > -1 && e();
    var a = '<link rel="stylesheet" type="text/css" class="cload" />'; - 1 !== window.location.search.search(/[?&]theme=default(?:$|&)/) && (e(), $(".cload").remove(), $(".colors a").removeClass("active"), $("#base").addClass("active")), -1 !== window.location.search.search(/[?&]theme=stone(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-stone.min.css")), e(), $.cookie("b-different-stone", 1)), -1 !== window.location.search.search(/[?&]theme=navy(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-navy.min.css")), e(), $.cookie("b-different-navy", 1)), -1 !== window.location.search.search(/[?&]theme=green(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-green-gray.min.css")), e(), $.cookie("b-different-green-gray", 1)), -1 !== window.location.search.search(/[?&]theme=blue(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-blue-gray.min.css")), e(), $.cookie("b-different-blue-gray", 1)), -1 !== window.location.search.search(/[?&]theme=navy-taupe(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-navy-taupe.min.css")), e(), $.cookie("b-different-navy-taupe", 1)), -1 !== window.location.search.search(/[?&]theme=white-soft-gray(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-white.min.css")), e(), $.cookie("b-different-white", 1)), -1 !== window.location.search.search(/[?&]theme=salmon-blue(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-salmon-blue.min.css")), e(), $.cookie("b-different-salmon-blue", 1)), -1 !== window.location.search.search(/[?&]theme=retro(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-retro.min.css")), e(), $.cookie("b-different-retro", 1)), -1 !== window.location.search.search(/[?&]theme=red-black(?:$|&)/) && ($("head").append($(a).attr("href", "assets/css/b-different-red-black.min.css")), e(), $.cookie("b-different-red-black", 1))
});