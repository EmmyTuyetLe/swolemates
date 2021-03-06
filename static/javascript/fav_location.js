'use strict';

let locationForms = document.querySelectorAll(".save_location_form")
for (let form of locationForms){
  form.addEventListener("submit", (evt) => {
    evt.preventDefault();
    let locationId = evt.target.id.split("_")[2]
  
    const formInputs = {
      location_id: document.querySelector(`#location_id_${locationId}`).value,
      location_name: document.querySelector(`#location_name_${locationId}`).value,
      // location_url: document.querySelector(`#location_url_${locationId}`).value,
      user_id: document.querySelector("#user_id").value
    };

    fetch("/fav_location.json", {
      method: "POST",
      body: JSON.stringify(formInputs),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then(response => response.json())
      .then(responseJson => {
        alert(responseJson.status);
      });
  });
}


