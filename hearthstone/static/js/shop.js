$('#buyCardModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    recipient = button.data('whatever') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    modal.find('.modal-title').text('Acheter un paquet de cartes extenstion : ' + recipient)
    //modal.find('.modal-body input').val(recipient)

  });

  
$('#buyCards').on('click', function() {
    buyCardsByExtension(recipient);
});

function buyCardsByExtension(recipient) {
    $.ajax({
        type: "GET",
        url: "/buy-cards/" + recipient,
        success: function (response) {
            console.log(response);
            $('div.row#zoneCard div#buy').remove();
            $.each(response, function(i, item) {
                console.log(item.card);
            });
        },
        error: function (xhr, status, error) {
            alert("La requête n'a pas abouti. (status:" + xhr.status + ")");
        }
    });
}

  

  console.log("here");