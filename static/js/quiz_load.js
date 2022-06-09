const url = window.location.href

$(document).ready(function () {
    $('.quiz_desc_button').click(function (event) {

        var clickedIndex = $(this).index();
        var quiz_id = $(this).data("id");

/*        console.log("clicked Index: " + clickedIndex);
        console.log("data id" + quiz_id);*/

        $('.quiz_desc_box').hide();
        $('.quiz_desc_box').eq(clickedIndex).show();

        var id = $('.quiz_desc_box').eq(clickedIndex).data("id");
        // console.log("quiz id: " + id);

        $('.start-quiz').on("click", function () {
            // console.log("Clicked!");
            window.location.href = url + quiz_id;
        })
})
});