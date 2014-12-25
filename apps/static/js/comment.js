$(document).ready(function() {
    var pusher = new Pusher('971380d4cd5e93a08113')
    var channel = pusher.subscribe('likelion')

    channel.bind('event_msg', function(data){
        $('#chatpanel').append("<div>"+data.name+" : "+data.msg+"</div>");
        $('#chatpanel').scrollTop($("#chatpanel")[0].scrollHeight);
    });

    $('#send').click(function(){
        var name = $("#chat_name").val();
        var msg = $("#chat_msg").val();
        $.get("/send",{
            name_data : name,
            msg_data : msg
        },function(data){});
        $('#chat_msg').attr('value')='';
    });

});