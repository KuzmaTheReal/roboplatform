$(document).ready(function () {
    $(".ellipse2").click(function () {
        $(this).attr("src", "images/ellipse-bottom.svg");
        $(".menu-lear-in").addClass("d-none");
        $(".menu-lear-in").removeClass("d-block");
        $(".menu-lear-in[data-id='" + $(this).parent().attr('data-id') + "']").addClass("d-block");
        $(".ellipse2").attr("src", "images/ellipse-bottom.svg");
        $(this).attr("src", "images/ellipse-top.svg");
    });

    $(".ellipse").click(function () {
        $(".ellipse").attr("src", "images/ellipse-bottom.svg");
        $(this).attr("src", "images/ellipse-top.svg");
        $(".all-learns").addClass("d-none");
        $(this).parent().parent().parent().children(".all-learns").removeClass("d-none");
    });

    $(".all-learns div").click(function () {
        $(".first-block").addClass("d-none");
        $(".description").removeClass("d-none");

        var titleBlock = $(".text-area[data-block-id='" + $(this).attr('data-block-id') + "']").text();
        $(".description-title").text(titleBlock + " / " + $(this).text());

        $(".menu-lear-in[data-id='" + $(this).attr('data-id') + "']").removeClass("d-none");
        $(".ellipse2").attr("src", "images/ellipse-bottom.svg");
        $(".learn[data-id='" + $(this).attr('data-id') + "']").children(".ellipse2").attr("src", "images/ellipse-top.svg");

        $(".menu-right div").attr("data-block-id", $(this).attr('data-block-id'));
    });

    $(".menu-right .learn").click(function () {
        $(".first-block").addClass("d-none");
        $(".description").removeClass("d-none");

        var titleBlock = $(".text-area[data-block-id='" + $(this).attr('data-block-id') + "']").text();
        $(".description-title").text(titleBlock + " / " + $(this).text());

        $(".menu-lear-in").hide();
    });
});