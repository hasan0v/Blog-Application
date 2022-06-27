$(document).ready(function() {
user_input = {
    user: 3,
    profile: 2
}


let HOST_URL = 'http://localhost:8000/'
var TOKEN = document.querySelector('[name=csrfmiddlewaretoken]').value;
console.log(TOKEN, user_input['user'])
// $('.statsbtn').on('click', function(){
//     $.ajax({
//         type: "POST",
//         dataType: "json",
//         url: HOST_URL + "members/" + id + "/stats/",
//         headers: {
//             "X-CSRFToken": TOKEN
//         },
//         crossDomain: true,
//         data: {
//             'user': JSON.stringify(user_input['user']),
//         },
//         success: (response) => {
//             console.log(response)
//             response = response['data'];
//             console.log(response)
//         },
//         error: function(err) {
//             if (err.status == "398") {
//                 console.log(err.responseJSON.error); // the message
//                 // window.open(HOST_URL + "?redirect_uri=report.html", "_self")
//             } else {
//                 console.log("Error in Ajax Reports:", err);
//             }
//         }
//     })
// })
})
