
const dest_name = document.getElementsByClassName("dest_name")
const dest_arr = Array.from(dest_name)
dest_arr.forEach(e=>{
  e.addEventListener('mouseover',(t)=>{
  //console.log(t.target.textContent)
    loadImg(t.target.textContent)
  })

})

function loadImg(destination){
  removeImages()
  const img_col = document.getElementById("img_col")
  const api_key = '72xzGoTm34DvhMeYqfmmGHMlghIifyUfTSCGHowbZg0'
  // const url = `https://api.unsplash.com/search/photos/?query=car&per_page=3&client_id=${api_key}`
  const url = `https://api.unsplash.com/search/photos/?query=${destination}&per_page=4&client_id=${api_key}`
  fetch(url)
    .then(response=>{
      if (response.ok){
        return response.json()
      }else {
        alert(response.status)
      }
    })
    .then(data=>{
      const imageNodes = []
      for (let i =0;i<data.results.length;i++){
        //create main card div
        imageNodes[i] = document.createElement('div')
        imageNodes[i].className = 'card'
        imageNodes[i].style.width = "18rem"
        //create image tag to be placed inside the card
        let img_ele = document.createElement('img')
        img_ele.src = data.results[i].urls.raw
        img_ele.height = 200
        imageNodes[i].appendChild(img_ele)
        //card footer
        let card_ft = document.createElement('div')
        card_ft.className = 'card-footer'
        card_ft.textContent = destination
        imageNodes[i].appendChild(card_ft)

        img_col.appendChild(imageNodes[i])
      }
    })
}

function removeImages(){
  const img_col = document.getElementById("img_col")
  img_col.innerHTML = ''

}