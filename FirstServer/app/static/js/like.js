let heart=$('.some-info svg')

console.log(heart)

function sendrequest(film_id) {
    $.ajax({
        url: `/likes_movies/${film_id}`,
        method: "GET",
        dataType: "json",
        success: function (data) {
            console.log(data);
            $(heart).toggleClass('liked');
        }
    });
}


$(heart).click(function (e) {
    e.preventDefault();
    let film_id=$(this).data('film_id')
    // console.log(film_id) 
    sendrequest(film_id)
});