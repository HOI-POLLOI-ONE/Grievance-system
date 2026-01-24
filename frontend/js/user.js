async function loadMyComplaints() {
  const token = localStorage.getItem("token");

  const response = await fetch(
    "http://127.0.0.1:8000/api/v1/complaints/my-complaints",
    {
      method: "GET",
      headers: {
        "Authorization": "Bearer " + localStorage.getItem("token")  
      }
    }
  );

  if (!response.ok) {
    alert("Failed to load complaints");
    return;
  }

  const complaints = await response.json();
  console.log(complaints);

  const list = document.getElementById("complaintList");
  list.innerHTML = "";

  complaints.forEach(c => {
    list.innerHTML += `
      <div class="card">
        <h3>${c.title}</h3>
        <p>${c.description}</p>
        <p>Status: <b>${c.status}</b></p>
      </div>
    `;
  });
}


window.onload = loadMyComplaints;
