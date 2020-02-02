// form handler for reporting cases of Tusavirus

$(document).ready(function() {

    $('form').on('submit', function(event) {

            $.ajax({
                data : {
                    state_id : $("#state_id").val(),
                    number_infections: $("#number_infections").val()
                },
                type : 'POST',
                url : '/send_report'

            })

            .done(function(data) {

                if (data.error) {
                    $('#error_alert').text(data.error).show();
                    $('#success_alert').hide();
                }
                else {
                    $('#success_alert').text(data.success).show();
                    $('#error_alert').hide();
                }
        });
            event.preventDefault();
    });
});
