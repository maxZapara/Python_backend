let heart=$('.some-info svg')

console.log(heart)

function sendrequest() {
    $.ajax({
        url: "/profile",
        method: "GET",        
        dataType: "html",        
        success: function (data) {
            console.log(data)
        }
    });
}

sendrequest()

$(heart).click(function (e) {
    e.preventDefault();
    $(this).toggleClass('liked');
});