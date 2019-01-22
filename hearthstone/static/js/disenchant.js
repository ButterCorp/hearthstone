$('#disenchantCardModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    recipient = button.data('whatever') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    modal.find('.modal-title').text('Désenchanter la carte : ' + recipient)
    //modal.find('.modal-body input').val(recipient)

  });

  
$('#disenchantCards').on('click', function() {
    disenchantCards(recipient);
});

function disenchantCards(recipient) {
    $.ajax({
        type: "GET",
        url: "/disenchant-cards/" + recipient,
        success: function (response) {
            console.log(response);
            $('div.row#zoneCardDisenchant div#disenchantCards').remove();
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
