function addTraveller() {
  const travellerDetails = document.getElementById("traveller-details");

  const newTraveller = document.createElement("div");
  newTraveller.classList.add("traveller");
  newTraveller.innerHTML = `
            <select>
                <option>Mr</option>
                <option>Ms</option>
                <option>Mrs</option>
            </select>
            <input type="text" placeholder="First Name *">
            <input type="text" placeholder="Last Name *">
        `;

  travellerDetails.appendChild(newTraveller);
}
