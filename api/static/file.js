
$("form").submit(function(e){
    e.preventDefault();
    $.ajax({
        url: "/search",
        type: "GET",
        data: $(this).serializeArray(),
        success: function(data, status, xhr) {

            insert_data(data);
        },
        error: function(xhr, status, err) {
            console.log('fail');
            console.log(err);
        }
    });
});

function insert_data(data){
    dLen = data.length;
    $('div.list').empty();
    for (i = 0; i < dLen; i++) {
        $('div.list').append("<h4>" + data[i].title + "</h4>")
        $('div.list').append("<p><a href=" + data[i].url + ">" + data[i].url + "</a></p>")
    }
}
