let menu = document.getElementById("menu");
let clear = document.getElementById("close")
let option = document.getElementById("middle-nav")
let user = '{{Request.user}}'


menu.addEventListener("click", open)
function open(){
  option.style.display = "block"
  clear.style.display = "block"
  menu.style.display = "none"
}

clear.addEventListener("click", close)
function close(){
  option.style.display = "none"
  clear.style.display = "none"
  menu.style.display = "block"
}


// function getToken(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== '') {
//       const cookies = document.cookie.split(';');
//       for (let i = 0; i < cookies.length; i++) {
//           const cookie = cookies[i].trim();
//           // Does this cookie string begin with the name we want?
//           if (cookie.substring(0, name.length + 1) === (name + '=')) {
//               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//               break;
//           }
//       }
//   }
//   return cookieValue;
// }

// const csrftoken = getToken('csrftoken');
// console.log(csrftoken)



// let updateBtn = document.getElementsByClassName('update-cart')

// for (i=0; i < updateBtn.length; i++){
//   updateBtn[i].addEventListener('click', function(){
//     let productId = this .dataset.product
//     let action = this.dataset.action
//     console.log('USER:',user)
//     console.log('productId :',productId, 'action:',action)

//     if (user === 'AnonymousUser'){
//       console.log('user is not authenticated')
//     }
//     else{
//       updateUserOrder (productId, action)
//     }
//   })
// }

// function updateUserOrder (productId, action){
//   console.log('user is logged in')

//   let url = '/update_item'

//   fetch(url, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//       'X-CSRFToken': csrftoken,
//     },
//     body: JSON.stringify ({'productId': productId, 'action': action})
//   })
//   .then ((response)=>{
//     return response.json()
//   })
//   .then ((response)=>{
//     console.log('data:', data)
//   })
// }