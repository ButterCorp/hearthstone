$(".follow").click(function () {
    $target = $(this);
    $recipient = $target.attr('data-user');
    $.ajax({
        type: "POST",
        url: "" + $target.attr('data-follow') + "/" + $recipient,
        success: function (response) {
            if ($target.attr('data-follow') == 'follow') {
                $target.attr('data-follow', 'unfollow');
                $target.text('unfollow');
                $(".followers-number").text(parseInt($(".followers-number").text()) + 1);
            }
            else {
                $target.attr('data-follow', 'follow')
                $target.text('follow');
                $(".followers-number").text(parseInt($(".followers-number").text()) - 1);
            }
        },
        error: function (xhr, status, error) {
            alert("La requête n'a pas abouti. (status:" + xhr.status + ")");
        }
        });
    });